#!/usr/bin/env python3
"""
Complete system test for the debt collection conversation generator
"""

import os
import json
from jsonl_processor import JSONLProcessor
from conversation_generator import ConversationGenerator

def test_complete_pipeline():
    """Test the complete pipeline from JSONL input to JSONL output"""
    print("Testing Complete Conversation Generation Pipeline...")
    
    # Initialize processor
    processor = JSONLProcessor()
    
    # Step 1: Create sample input file
    print("\n1. Creating sample input JSONL file...")
    sample_input_file = "sample_input.jsonl"
    processor.create_sample_input_jsonl(sample_input_file)
    
    # Step 2: Read input file
    print("\n2. Reading input JSONL file...")
    input_prompts = processor.read_input_jsonl(sample_input_file)
    print(f"Loaded {len(input_prompts)} input prompts")
    
    # Step 3: Process prompts (use only 3 scenarios for quick testing)
    print("\n3. Processing prompts (generating 3 scenarios for testing)...")
    conversations = processor.process_all_prompts(input_prompts, num_scenarios=3)
    
    # Step 4: Write output file
    print("\n4. Writing output JSONL file...")
    output_file = "test_output.jsonl"
    processor.write_output_jsonl(conversations, output_file)
    
    # Step 5: Verify output file
    print("\n5. Verifying output file...")
    verify_output_file(output_file)
    
    # Step 6: Print statistics
    print("\n6. Processing statistics:")
    processor.print_statistics()
    
    # Cleanup
    print("\n7. Cleaning up test files...")
    if os.path.exists(sample_input_file):
        os.remove(sample_input_file)
    if os.path.exists(output_file):
        os.remove(output_file)
    
    print("\n✓ Complete pipeline test finished successfully!")

def verify_output_file(output_file: str):
    """Verify the output JSONL file is correctly formatted"""
    print(f"Verifying {output_file}...")
    
    if not os.path.exists(output_file):
        print(f"✗ Output file {output_file} does not exist")
        return False
    
    line_count = 0
    valid_entries = 0
    
    with open(output_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line_count += 1
            line = line.strip()
            
            if not line:
                continue
            
            try:
                data = json.loads(line)
                
                # Check required fields
                required_fields = ['scenario_id', 'variation_id', 'conversation', 'validation_passed']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    print(f"✗ Line {line_num}: Missing fields: {missing_fields}")
                    continue
                
                # Check conversation format
                conversation = data.get('conversation', [])
                if not isinstance(conversation, list):
                    print(f"✗ Line {line_num}: Conversation is not a list")
                    continue
                
                # Check conversation messages
                for msg_idx, msg in enumerate(conversation):
                    if not isinstance(msg, dict):
                        print(f"✗ Line {line_num}, message {msg_idx}: Message is not a dict")
                        continue
                    
                    if 'role' not in msg or 'content' not in msg:
                        print(f"✗ Line {line_num}, message {msg_idx}: Missing role or content")
                        continue
                    
                    if msg['role'] not in ['user', 'assistant']:
                        print(f"✗ Line {line_num}, message {msg_idx}: Invalid role: {msg['role']}")
                        continue
                
                valid_entries += 1
                
            except json.JSONDecodeError as e:
                print(f"✗ Line {line_num}: JSON decode error: {e}")
                continue
            except Exception as e:
                print(f"✗ Line {line_num}: Unexpected error: {e}")
                continue
    
    print(f"✓ Verified {valid_entries}/{line_count} valid entries in output file")
    
    # Show sample entries
    print("\nSample output entries:")
    with open(output_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 2:  # Show first 2 entries
                break
            
            data = json.loads(line.strip())
            print(f"\nEntry {i+1}:")
            print(f"  Scenario: {data['scenario_id']}")
            print(f"  Variation: {data['variation_id']}")
            print(f"  Validation passed: {data['validation_passed']}")
            print(f"  Conversation length: {len(data['conversation'])} messages")
            print(f"  Special tags: {data.get('special_tags_found', [])}")
            
            # Show first message
            if data['conversation']:
                first_msg = data['conversation'][0]
                print(f"  First message: {first_msg['content'][:100]}...")
    
    return True

def test_command_line_interface():
    """Test the command-line interface"""
    print("\n\nTesting Command-Line Interface...")
    
    # Create sample input
    processor = JSONLProcessor()
    sample_input = "cli_test_input.jsonl"
    processor.create_sample_input_jsonl(sample_input)
    
    # Test CLI command
    import subprocess
    
    output_file = "cli_test_output.jsonl"
    cmd = f"python3 jsonl_processor.py --input {sample_input} --output {output_file} --scenarios 2"
    
    print(f"Running command: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✓ CLI command executed successfully")
            print("STDOUT:", result.stdout[-500:])  # Last 500 chars
        else:
            print("✗ CLI command failed")
            print("STDERR:", result.stderr)
            
    except subprocess.TimeoutExpired:
        print("✗ CLI command timed out")
    except Exception as e:
        print(f"✗ CLI command error: {e}")
    
    # Cleanup
    for file in [sample_input, output_file]:
        if os.path.exists(file):
            os.remove(file)

if __name__ == "__main__":
    test_complete_pipeline()
    test_command_line_interface()

