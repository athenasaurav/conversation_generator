#!/usr/bin/env python3
"""
Debt Collection Conversation Generator

This program generates diverse debt collection conversation scenarios for training
a phone agent AI model. It takes system prompts and creates 100 different scenarios,
each with 10 variations, resulting in 1000 unique conversations per input prompt.
"""

import json
import random
import re
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import openai
import os
from validation_system import ConversationValidator, RetryManager, ValidationResult
from scenario_definitions import DEBT_COLLECTION_SCENARIOS, SPECIAL_TAGS, CUSTOMER_BEHAVIORS, OUTCOME_TYPES

@dataclass
class ConversationRequest:
    """Represents a request to generate a conversation"""
    scenario_id: str
    variation_id: int
    system_prompt: str
    customer_name: str
    agent_name: str
    debt_amount: str
    due_date: str
    special_requirements: List[str]

@dataclass
class GeneratedConversation:
    """Represents a generated conversation"""
    scenario_id: str
    variation_id: int
    conversation: List[Dict[str, str]]
    special_tags_found: List[str]
    validation_passed: bool
    system_prompt: str

class ConversationGenerator:
    """Main class for generating debt collection conversations"""
    
    def __init__(self, api_key: str = None):
        """Initialize the conversation generator"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.scenarios = DEBT_COLLECTION_SCENARIOS
        self.special_tags = SPECIAL_TAGS
        self.validator = ConversationValidator()
        self.retry_manager = RetryManager(max_retries=3)
        
        # Name pools for variations
        self.agent_names = [
            "Salma", "Ahmed", "Fatima", "Omar", "Layla", "Hassan", "Nour", "Khalid",
            "Amira", "Youssef", "Zara", "Ali", "Maryam", "Saeed", "Lina", "Tariq"
        ]
        
        self.customer_names = [
            "Khalili", "Al-Rashid", "Mansour", "Al-Zahra", "Qasemi", "Al-Mahmoud",
            "Abdulla", "Al-Farisi", "Hamdan", "Al-Mansoori", "Sharif", "Al-Blooshi",
            "Nasser", "Al-Shamsi", "Rashed", "Al-Kaabi", "Salem", "Al-Dhaheri"
        ]
        
        # Amount variations (in AED)
        self.debt_amounts = [
            "three hundred dirhams", "four hundred fifty dirhams", 
            "six hundred dirhams", "seven hundred twenty-five dirhams",
            "eight hundred dirhams", "nine hundred fifty dirhams",
            "one thousand dirhams", "one thousand two hundred dirhams",
            "one thousand five hundred dirhams", "two thousand dirhams"
        ]
    
    def generate_variations(self, base_scenario: Dict[str, Any]) -> List[ConversationRequest]:
        """Generate 10 variations of a base scenario"""
        variations = []
        
        for i in range(10):
            # Create variation with different names, amounts, dates
            variation = ConversationRequest(
                scenario_id=base_scenario["id"],
                variation_id=i + 1,
                system_prompt="",  # Will be filled later
                customer_name=random.choice(self.customer_names),
                agent_name=random.choice(self.agent_names),
                debt_amount=random.choice(self.debt_amounts),
                due_date=self._generate_random_due_date(),
                special_requirements=base_scenario.get("special_tags", [])
            )
            variations.append(variation)
        
        return variations
    
    def _generate_random_due_date(self) -> str:
        """Generate a random due date in the past"""
        days_ago = random.randint(5, 45)
        due_date = datetime.now() - timedelta(days=days_ago)
        
        # Convert to natural format like "August first"
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        
        day_ordinals = {
            1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth",
            6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth",
            11: "eleventh", 12: "twelfth", 13: "thirteenth", 14: "fourteenth", 15: "fifteenth",
            16: "sixteenth", 17: "seventeenth", 18: "eighteenth", 19: "nineteenth", 20: "twentieth",
            21: "twenty-first", 22: "twenty-second", 23: "twenty-third", 24: "twenty-fourth", 25: "twenty-fifth",
            26: "twenty-sixth", 27: "twenty-seventh", 28: "twenty-eighth", 29: "twenty-ninth", 30: "thirtieth", 31: "thirty-first"
        }
        
        month = month_names[due_date.month - 1]
        day = day_ordinals[due_date.day]
        
        return f"{month} {day}"
    
    def create_scenario_prompt(self, base_prompt: str, scenario: Dict[str, Any], variation: ConversationRequest) -> str:
        """Create a specific prompt for generating a conversation scenario"""
        
        # Replace variables in the base prompt
        scenario_prompt = base_prompt.replace("{FirstName}", variation.customer_name.split()[0] if " " in variation.customer_name else variation.customer_name)
        scenario_prompt = scenario_prompt.replace("{LastName}", variation.customer_name.split()[-1] if " " in variation.customer_name else "")
        scenario_prompt = scenario_prompt.replace("{amount}", variation.debt_amount)
        scenario_prompt = scenario_prompt.replace("{DueDate}", variation.due_date)
        scenario_prompt = scenario_prompt.replace("Salma", variation.agent_name)
        
        # Add scenario-specific instructions
        scenario_instructions = f"""

## SCENARIO-SPECIFIC INSTRUCTIONS FOR THIS CONVERSATION:

**Scenario Type:** {scenario['name']}
**Description:** {scenario['description']}
**Customer Behavior:** {scenario['customer_behavior']}
**Expected Outcome:** {scenario['outcome']}
**Required Special Tags:** {', '.join(scenario.get('special_tags', []))}

**Conversation Requirements:**
- The conversation MUST include at least one of these special tags: {', '.join(scenario.get('special_tags', []))}
- Customer should exhibit behavior consistent with: {scenario['customer_behavior']}
- The conversation should naturally lead to outcome: {scenario['outcome']}
- Make the conversation realistic and natural, not scripted
- Include appropriate emotional responses and realistic dialogue
- Ensure the agent follows the guided conversation rules from the base prompt

**Special Instructions:**
{self._get_scenario_specific_instructions(scenario)}
"""
        
        return scenario_prompt + scenario_instructions
    
    def _get_scenario_specific_instructions(self, scenario: Dict[str, Any]) -> str:
        """Get specific instructions based on scenario type"""
        scenario_id = scenario["id"]
        
        if "wrong_person" in scenario_id:
            return "- The person answering is NOT the debtor\n- Agent must handle according to regulations\n- May need to transfer or disconnect"
        elif "hostile" in scenario_id:
            return "- Customer becomes aggressive or angry\n- Agent must remain professional\n- May need to disconnect if too hostile"
        elif "legal" in scenario_id:
            return "- Customer raises legal issues\n- Agent must follow legal protocols\n- May require escalation or transfer"
        elif "payment" in scenario_id and "willing" in scenario_id:
            return "- Customer is cooperative and willing to pay\n- Focus on securing specific payment date\n- Use function_1 tag for payment processing"
        elif "technical" in scenario_id:
            return "- Technical issues affect the call quality\n- May need to disconnect and callback\n- Handle technical problems professionally"
        elif "vulnerable" in scenario["customer_behavior"]:
            return "- Customer needs special handling\n- Be extra careful and considerate\n- May need to transfer to specialist"
        else:
            return "- Follow standard debt collection procedures\n- Adapt to customer responses naturally\n- Include required special tags appropriately"
    
    def generate_conversation(self, prompt: str, max_retries: int = 3) -> Tuple[List[Dict[str, str]], List[str]]:
        """Generate a single conversation using OpenAI API"""
        
        generation_prompt = f"""You are tasked with generating a realistic debt collection phone conversation based on the provided system prompt and scenario requirements.

Generate a complete conversation between the debt collection agent and the customer. The conversation should:
1. Follow the system prompt guidelines exactly
2. Include the required special tags naturally in the conversation
3. Be realistic and natural, not scripted
4. Show appropriate progression through the conversation states
5. Include realistic customer responses and agent handling

Format the output as a JSON array where each message has "role" (either "assistant" for agent or "user" for customer) and "content" (the message text).

The conversation should start with the agent's opening and continue until a natural conclusion.

System Prompt and Scenario:
{prompt}

Generate the conversation now:"""

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "You are an expert at generating realistic debt collection conversations. Always respond with valid JSON format."},
                        {"role": "user", "content": generation_prompt}
                    ],
                    temperature=0.8,
                    max_tokens=2000
                )
                
                content = response.choices[0].message.content.strip()
                
                # Try to extract JSON from the response
                json_match = re.search(r'\[.*\]', content, re.DOTALL)
                if json_match:
                    conversation_json = json_match.group()
                    conversation = json.loads(conversation_json)
                    
                    # Find special tags in the conversation
                    special_tags_found = self._find_special_tags(conversation)
                    
                    return conversation, special_tags_found
                else:
                    print(f"Attempt {attempt + 1}: Could not find valid JSON in response")
                    
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    # Return empty conversation if all attempts fail
                    return [], []
        
        return [], []
    
    def _find_special_tags(self, conversation: List[Dict[str, str]]) -> List[str]:
        """Find special tags in the conversation"""
        found_tags = []
        
        for message in conversation:
            content = message.get("content", "").lower()
            for tag in self.special_tags:
                # Extract tag name without parentheses
                tag_name = tag.strip("()")
                # Check for various formats: (tag), <tag>, or just tag
                if (tag in content or 
                    f"<{tag_name}>" in content or 
                    f" {tag_name}" in content or 
                    f"{tag_name} " in content or
                    content.endswith(tag_name) or
                    content.startswith(tag_name)):
                    found_tags.append(tag)
        
        return list(set(found_tags))  # Remove duplicates
    
    def generate_all_scenarios(self, base_system_prompt: str) -> List[GeneratedConversation]:
        """Generate conversations for all 100 scenarios with 10 variations each"""
        all_conversations = []
        
        print(f"Generating conversations for {len(self.scenarios)} scenarios...")
        
        for i, scenario in enumerate(self.scenarios):
            print(f"Processing scenario {i+1}/100: {scenario['name']}")
            
            # Generate 10 variations for this scenario
            variations = self.generate_variations(scenario)
            
            for variation in variations:
                # Create scenario-specific prompt
                scenario_prompt = self.create_scenario_prompt(base_system_prompt, scenario, variation)
                
                # Generate conversation with enhanced retry logic
                conversation, validation_result = self.retry_manager.generate_with_retry(
                    self.generate_conversation,
                    scenario_prompt,
                    required_tags=scenario.get("special_tags", []),
                    scenario_type=scenario["id"]
                )
                
                # Create result object
                generated_conv = GeneratedConversation(
                    scenario_id=scenario["id"],
                    variation_id=variation.variation_id,
                    conversation=conversation,
                    special_tags_found=validation_result.found_tags if validation_result else [],
                    validation_passed=validation_result.passed if validation_result else False,
                    system_prompt=scenario_prompt
                )
                all_conversations.append(generated_conv)
                
                status = "✓" if generated_conv.validation_passed else "✗"
                print(f"  {status} Variation {variation.variation_id} - Quality: {validation_result.quality_score:.2f}" if validation_result else f"  ✗ Variation {variation.variation_id} - Failed")
        
        return all_conversations
    
    def save_to_jsonl(self, conversations: List[GeneratedConversation], output_file: str):
        """Save conversations to JSONL format"""
        with open(output_file, 'w', encoding='utf-8') as f:
            for conv in conversations:
                jsonl_entry = {
                    "scenario_id": conv.scenario_id,
                    "variation_id": conv.variation_id,
                    "system_prompt": conv.system_prompt,
                    "conversation": conv.conversation,
                    "special_tags_found": conv.special_tags_found,
                    "validation_passed": conv.validation_passed,
                    "metadata": {
                        "generated_at": datetime.now().isoformat(),
                        "model": "gpt-4.1-mini"
                    }
                }
                f.write(json.dumps(jsonl_entry, ensure_ascii=False) + '\n')
        
        print(f"Saved {len(conversations)} conversations to {output_file}")

def main():
    """Main function to run the conversation generator"""
    # Example usage
    generator = ConversationGenerator()
    
    # Read base system prompt from file
    try:
        with open('/home/ubuntu/upload/pasted_content_2.txt', 'r', encoding='utf-8') as f:
            base_prompt = f.read()
    except FileNotFoundError:
        print("Error: Could not find base system prompt file")
        return
    
    # Generate all conversations
    conversations = generator.generate_all_scenarios(base_prompt)
    
    # Save to JSONL
    output_file = f"debt_collection_conversations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
    generator.save_to_jsonl(conversations, output_file)
    
    # Print statistics
    total_conversations = len(conversations)
    successful_conversations = len([c for c in conversations if c.validation_passed])
    
    print(f"\n=== Generation Complete ===")
    print(f"Total conversations generated: {total_conversations}")
    print(f"Successfully validated: {successful_conversations}")
    print(f"Failed validation: {total_conversations - successful_conversations}")
    print(f"Success rate: {(successful_conversations/total_conversations)*100:.1f}%")

if __name__ == "__main__":
    main()

