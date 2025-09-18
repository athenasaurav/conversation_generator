#!/usr/bin/env python3
"""
Test script for the conversation generator
"""

import json
from conversation_generator import ConversationGenerator
from scenario_definitions import DEBT_COLLECTION_SCENARIOS

def test_basic_functionality():
    """Test basic functionality of the conversation generator"""
    print("Testing Conversation Generator...")
    
    # Initialize generator
    generator = ConversationGenerator()
    
    # Test variation generation
    print("\n1. Testing variation generation...")
    test_scenario = DEBT_COLLECTION_SCENARIOS[0]  # First scenario
    variations = generator.generate_variations(test_scenario)
    
    print(f"Generated {len(variations)} variations for scenario: {test_scenario['name']}")
    for i, var in enumerate(variations[:3]):  # Show first 3
        print(f"  Variation {i+1}: {var.customer_name}, {var.agent_name}, {var.debt_amount}")
    
    # Test prompt creation
    print("\n2. Testing prompt creation...")
    base_prompt = """# CASHNOW PROMPT: Collection Agent Identity & Instructions

## AGENT IDENTITY
You are **{agent_name}**, a professional account specialist from **ClearGrid** calling on behalf of **CashNow**. 

## CORE OBJECTIVES
- Obtain payment commitment for {amount} that was due on {DueDate}
- Customer name: {FirstName} {LastName}
"""
    
    scenario_prompt = generator.create_scenario_prompt(base_prompt, test_scenario, variations[0])
    print("Scenario prompt created successfully")
    print(f"Prompt length: {len(scenario_prompt)} characters")
    
    # Test special tag detection
    print("\n3. Testing special tag detection...")
    test_conversation = [
        {"role": "assistant", "content": "Hello, this is Salma from ClearGrid."},
        {"role": "user", "content": "Hi there."},
        {"role": "assistant", "content": "Thank you. Have a good day. (disconnect)"}
    ]
    
    found_tags = generator._find_special_tags(test_conversation)
    print(f"Found special tags: {found_tags}")
    
    # Test validation
    validation_result = generator.validate_conversation(test_conversation, ["(disconnect)"])
    print(f"Validation passed: {validation_result}")
    
    print("\n✓ All basic tests passed!")

def test_single_conversation_generation():
    """Test generating a single conversation"""
    print("\nTesting single conversation generation...")
    
    generator = ConversationGenerator()
    
    # Simple test prompt
    test_prompt = """You are Salma, a debt collection agent. Generate a conversation where:
- Customer name is Khalili
- Debt amount is six hundred dirhams
- Customer is cooperative and agrees to pay
- Include (function_1) tag when processing payment
- Keep conversation short (5-8 exchanges)"""
    
    conversation, found_tags = generator.generate_conversation(test_prompt)
    
    if conversation:
        print(f"✓ Generated conversation with {len(conversation)} messages")
        print(f"✓ Found tags: {found_tags}")
        
        # Show first few messages
        print("\nSample conversation:")
        for i, msg in enumerate(conversation[:4]):
            role = "Agent" if msg["role"] == "assistant" else "Customer"
            print(f"{role}: {msg['content']}")
        
        if len(conversation) > 4:
            print("...")
    else:
        print("✗ Failed to generate conversation")

if __name__ == "__main__":
    test_basic_functionality()
    test_single_conversation_generation()

