#!/usr/bin/env python3
"""
JSONL Processor for Debt Collection Conversation Generator

This module handles reading input JSONL files containing system prompts
and writing output JSONL files with generated conversations.
"""

import json
import os
from typing import List, Dict, Any, Iterator
from dataclasses import dataclass
from datetime import datetime
from conversation_generator import ConversationGenerator, GeneratedConversation

@dataclass
class InputPrompt:
    """Represents an input system prompt from JSONL"""
    id: str
    system_prompt: str
    language: str
    metadata: Dict[str, Any]

@dataclass
class ProcessingStats:
    """Statistics for processing results"""
    total_prompts: int
    total_conversations: int
    successful_conversations: int
    failed_conversations: int
    average_quality_score: float
    processing_time_seconds: float

class JSONLProcessor:
    """Handles JSONL input/output for conversation generation"""
    
    def __init__(self, generator: ConversationGenerator = None):
        """Initialize the JSONL processor"""
        self.generator = generator or ConversationGenerator()
        self.stats = None
    
    def read_input_jsonl(self, input_file: str) -> List[InputPrompt]:
        """Read and parse input JSONL file containing system prompts"""
        prompts = []
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    data = json.loads(line)
                    
                    # Extract required fields
                    prompt_id = data.get('id', f'prompt_{line_num}')
                    system_prompt = data.get('system_prompt', data.get('prompt', ''))
                    language = data.get('language', 'english')
                    metadata = data.get('metadata', {})
                    
                    if not system_prompt:
                        print(f"Warning: Empty system prompt in line {line_num}")
                        continue
                    
                    prompt = InputPrompt(
                        id=prompt_id,
                        system_prompt=system_prompt,
                        language=language,
                        metadata=metadata
                    )
                    prompts.append(prompt)
                    
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON on line {line_num}: {e}")
                    continue
                except Exception as e:
                    print(f"Error processing line {line_num}: {e}")
                    continue
        
        print(f"Successfully loaded {len(prompts)} prompts from {input_file}")
        return prompts
    
    def process_single_prompt(self, input_prompt: InputPrompt, 
                            num_scenarios: int = 100) -> List[GeneratedConversation]:
        """Process a single input prompt to generate conversations"""
        print(f"\nProcessing prompt: {input_prompt.id}")
        print(f"Language: {input_prompt.language}")
        print(f"Generating {num_scenarios} scenarios...")
        
        # Use only the first N scenarios if num_scenarios < 100
        scenarios_to_use = self.generator.scenarios[:num_scenarios]
        
        all_conversations = []
        
        for i, scenario in enumerate(scenarios_to_use):
            print(f"Processing scenario {i+1}/{num_scenarios}: {scenario['name']}")
            
            # Generate 10 variations for this scenario
            variations = self.generator.generate_variations(scenario)
            
            for variation in variations:
                # Create scenario-specific prompt
                scenario_prompt = self.generator.create_scenario_prompt(
                    input_prompt.system_prompt, scenario, variation
                )
                
                # Generate conversation with enhanced retry logic
                conversation, validation_result = self.generator.retry_manager.generate_with_retry(
                    self.generator.generate_conversation,
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
                quality = validation_result.quality_score if validation_result else 0.0
                print(f"  {status} Variation {variation.variation_id} - Quality: {quality:.2f}")
        
        return all_conversations
    
    def process_all_prompts(self, input_prompts: List[InputPrompt], 
                          num_scenarios: int = 100) -> List[GeneratedConversation]:
        """Process all input prompts"""
        start_time = datetime.now()
        all_conversations = []
        
        for prompt in input_prompts:
            conversations = self.process_single_prompt(prompt, num_scenarios)
            all_conversations.extend(conversations)
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        # Calculate statistics
        successful = len([c for c in all_conversations if c.validation_passed])
        failed = len(all_conversations) - successful
        avg_quality = sum(0.0 for c in all_conversations) / len(all_conversations) if all_conversations else 0.0
        
        self.stats = ProcessingStats(
            total_prompts=len(input_prompts),
            total_conversations=len(all_conversations),
            successful_conversations=successful,
            failed_conversations=failed,
            average_quality_score=avg_quality,
            processing_time_seconds=processing_time
        )
        
        return all_conversations
    
    def write_output_jsonl(self, conversations: List[GeneratedConversation], 
                          output_file: str, include_metadata: bool = True):
        """Write conversations to output JSONL file"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for conv in conversations:
                # Create output entry
                output_entry = {
                    "scenario_id": conv.scenario_id,
                    "variation_id": conv.variation_id,
                    "conversation": conv.conversation,
                    "validation_passed": conv.validation_passed,
                    "special_tags_found": conv.special_tags_found
                }
                
                if include_metadata:
                    output_entry["metadata"] = {
                        "generated_at": datetime.now().isoformat(),
                        "model": "gpt-4.1-mini",
                        "system_prompt_length": len(conv.system_prompt),
                        "conversation_length": len(conv.conversation),
                        "generator_version": "1.0"
                    }
                
                # Optionally include system prompt for debugging
                if not conv.validation_passed:
                    output_entry["debug_system_prompt"] = conv.system_prompt
                
                f.write(json.dumps(output_entry, ensure_ascii=False) + '\n')
        
        print(f"Saved {len(conversations)} conversations to {output_file}")
    
    def create_sample_input_jsonl(self, output_file: str):
        """Create a sample input JSONL file for testing"""
        
        # Read the base prompt from the uploaded file
        try:
            with open('/home/ubuntu/upload/pasted_content_2.txt', 'r', encoding='utf-8') as f:
                base_prompt = f.read()
        except FileNotFoundError:
            base_prompt = "# Sample debt collection prompt\nYou are a debt collection agent..."
        
        sample_prompts = [
            {
                "id": "english_prompt_1",
                "system_prompt": base_prompt,
                "language": "english",
                "metadata": {
                    "source": "cashnow_uae",
                    "version": "1.0",
                    "created_at": datetime.now().isoformat()
                }
            },
            {
                "id": "english_prompt_2", 
                "system_prompt": base_prompt.replace("Salma", "Ahmed").replace("ClearGrid", "DebtSolutions"),
                "language": "english",
                "metadata": {
                    "source": "debtsolutions_uae",
                    "version": "1.0",
                    "created_at": datetime.now().isoformat()
                }
            }
        ]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for prompt in sample_prompts:
                f.write(json.dumps(prompt, ensure_ascii=False) + '\n')
        
        print(f"Created sample input file: {output_file}")
    
    def print_statistics(self):
        """Print processing statistics"""
        if not self.stats:
            print("No statistics available")
            return
        
        print("\n" + "="*50)
        print("PROCESSING STATISTICS")
        print("="*50)
        print(f"Total input prompts: {self.stats.total_prompts}")
        print(f"Total conversations generated: {self.stats.total_conversations}")
        print(f"Successfully validated: {self.stats.successful_conversations}")
        print(f"Failed validation: {self.stats.failed_conversations}")
        print(f"Success rate: {(self.stats.successful_conversations/self.stats.total_conversations)*100:.1f}%")
        print(f"Average quality score: {self.stats.average_quality_score:.2f}")
        print(f"Processing time: {self.stats.processing_time_seconds:.1f} seconds")
        print(f"Conversations per minute: {(self.stats.total_conversations / self.stats.processing_time_seconds * 60):.1f}")

def main():
    """Main function for command-line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate debt collection conversations from JSONL prompts')
    parser.add_argument('--input', '-i', required=True, help='Input JSONL file with system prompts')
    parser.add_argument('--output', '-o', required=True, help='Output JSONL file for conversations')
    parser.add_argument('--scenarios', '-s', type=int, default=10, help='Number of scenarios to generate (default: 10, max: 100)')
    parser.add_argument('--create-sample', action='store_true', help='Create sample input file')
    
    args = parser.parse_args()
    
    processor = JSONLProcessor()
    
    if args.create_sample:
        processor.create_sample_input_jsonl(args.input)
        return
    
    try:
        # Read input prompts
        input_prompts = processor.read_input_jsonl(args.input)
        
        if not input_prompts:
            print("No valid prompts found in input file")
            return
        
        # Process prompts
        conversations = processor.process_all_prompts(input_prompts, args.scenarios)
        
        # Write output
        processor.write_output_jsonl(conversations, args.output)
        
        # Print statistics
        processor.print_statistics()
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())

