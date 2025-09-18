#!/usr/bin/env python3
"""
Debug validation issues
"""

from conversation_generator import ConversationGenerator
from validation_system import ConversationValidator, RetryManager
from scenario_definitions import DEBT_COLLECTION_SCENARIOS

def debug_validation_issue():
    """Debug why validation is failing"""
    print("Debugging validation issue...")
    
    generator = ConversationGenerator()
    validator = ConversationValidator()
    
    # Test with first scenario
    scenario = DEBT_COLLECTION_SCENARIOS[0]  # Customer willing to pay immediately
    print(f"Testing scenario: {scenario['name']}")
    print(f"Required tags: {scenario.get('special_tags', [])}")
    
    # Generate a variation
    variations = generator.generate_variations(scenario)
    variation = variations[0]
    
    # Create prompt
    with open('/home/ubuntu/upload/pasted_content_2.txt', 'r', encoding='utf-8') as f:
        base_prompt = f.read()
    
    scenario_prompt = generator.create_scenario_prompt(base_prompt, scenario, variation)
    
    # Generate conversation
    print("\nGenerating conversation...")
    conversation, found_tags = generator.generate_conversation(scenario_prompt)
    
    print(f"Generated conversation with {len(conversation)} messages")
    print(f"Found tags: {found_tags}")
    
    # Validate conversation
    print("\nValidating conversation...")
    validation_result = validator.validate_conversation(
        conversation, 
        scenario.get("special_tags", []), 
        scenario["id"]
    )
    
    print(f"Validation passed: {validation_result.passed}")
    print(f"Quality score: {validation_result.quality_score:.2f}")
    print(f"Found tags: {validation_result.found_tags}")
    print(f"Missing tags: {validation_result.missing_tags}")
    print(f"Issues: {validation_result.issues}")
    print(f"Recommendations: {validation_result.recommendations}")
    
    # Show conversation
    print("\nGenerated conversation:")
    for i, msg in enumerate(conversation):
        role = "Agent" if msg["role"] == "assistant" else "Customer"
        print(f"{i+1}. {role}: {msg['content']}")
    
    # Test with simpler validation
    print("\n" + "="*50)
    print("Testing with relaxed validation...")
    
    # Check if tags are present
    has_required_tags = any(tag in validation_result.found_tags for tag in scenario.get("special_tags", []))
    print(f"Has required tags: {has_required_tags}")
    
    # Check basic quality
    has_minimum_length = len(conversation) >= 4
    print(f"Has minimum length: {has_minimum_length}")
    
    # Check for basic debt collection content
    full_text = " ".join([msg.get("content", "") for msg in conversation]).lower()
    has_debt_content = any(word in full_text for word in ["debt", "payment", "amount", "loan", "balance"])
    print(f"Has debt collection content: {has_debt_content}")
    
    simple_validation = has_required_tags and has_minimum_length and has_debt_content
    print(f"Simple validation would pass: {simple_validation}")

if __name__ == "__main__":
    debug_validation_issue()

