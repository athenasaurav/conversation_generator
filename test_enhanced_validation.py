#!/usr/bin/env python3
"""
Test script for enhanced validation system
"""

from validation_system import ConversationValidator, RetryManager, ValidationResult
from conversation_generator import ConversationGenerator

def test_validation_system():
    """Test the enhanced validation system"""
    print("Testing Enhanced Validation System...")
    
    validator = ConversationValidator()
    
    # Test 1: Good conversation
    print("\n1. Testing good conversation...")
    good_conversation = [
        {"role": "assistant", "content": "Good afternoon, this is Salma from ClearGrid. Am I speaking to Mr. Khalili?"},
        {"role": "user", "content": "Yes, this is Khalili."},
        {"role": "assistant", "content": "Thank you for confirming. This call is recorded for quality purposes. I'm calling about your CashNow loan of six hundred dirhams that was due on August first. When can you pay this amount?"},
        {"role": "user", "content": "I can pay it today actually."},
        {"role": "assistant", "content": "Excellent! I'll process your payment now. (function_1) Please confirm the amount of six hundred dirhams."},
        {"role": "user", "content": "Yes, confirmed."},
        {"role": "assistant", "content": "Thank you. Your payment has been processed. Have a good day. (disconnect)"}
    ]
    
    result = validator.validate_conversation(good_conversation, ["(function_1)"], "basic_payment_willing")
    print(f"Validation passed: {result.passed}")
    print(f"Quality score: {result.quality_score:.2f}")
    print(f"Found tags: {result.found_tags}")
    print(f"Issues: {result.issues}")
    
    # Test 2: Poor conversation
    print("\n2. Testing poor conversation...")
    poor_conversation = [
        {"role": "assistant", "content": "Hi"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Pay money"}
    ]
    
    result = validator.validate_conversation(poor_conversation, ["(function_1)"], "basic_payment_willing")
    print(f"Validation passed: {result.passed}")
    print(f"Quality score: {result.quality_score:.2f}")
    print(f"Missing tags: {result.missing_tags}")
    print(f"Issues: {result.issues}")
    print(f"Recommendations: {result.recommendations}")
    
    # Test 3: Conversation with wrong person scenario
    print("\n3. Testing wrong person scenario...")
    wrong_person_conversation = [
        {"role": "assistant", "content": "Good afternoon, this is Salma from ClearGrid. Am I speaking to Mr. Khalili?"},
        {"role": "user", "content": "No, this is his wife. He's not home right now."},
        {"role": "assistant", "content": "I understand. I need to speak with Mr. Khalili directly about a personal matter. When would be a good time to reach him?"},
        {"role": "user", "content": "He'll be back around 6 PM."},
        {"role": "assistant", "content": "Thank you. I'll transfer this call to schedule a callback. (transfer) Have a good day."}
    ]
    
    result = validator.validate_conversation(wrong_person_conversation, ["(transfer)"], "wrong_person_family")
    print(f"Validation passed: {result.passed}")
    print(f"Quality score: {result.quality_score:.2f}")
    print(f"Found tags: {result.found_tags}")

def test_retry_manager():
    """Test the retry manager with actual conversation generation"""
    print("\n\nTesting Retry Manager...")
    
    generator = ConversationGenerator()
    retry_manager = RetryManager(max_retries=2)
    
    # Simple test prompt that should succeed
    test_prompt = """You are Salma, a debt collection agent from ClearGrid. Generate a conversation where:
- Customer name is Khalili  
- Debt amount is six hundred dirhams
- Customer agrees to pay
- Include (function_1) tag when processing payment
- Keep conversation realistic and professional
- Generate 6-8 message exchanges"""
    
    conversation, validation_result = retry_manager.generate_with_retry(
        generator.generate_conversation,
        test_prompt,
        required_tags=["(function_1)"],
        scenario_type="basic_payment_willing"
    )
    
    print(f"Generated conversation with {len(conversation)} messages")
    print(f"Validation passed: {validation_result.passed}")
    print(f"Quality score: {validation_result.quality_score:.2f}")
    print(f"Found tags: {validation_result.found_tags}")
    
    if conversation:
        print("\nSample conversation:")
        for i, msg in enumerate(conversation[:4]):
            role = "Agent" if msg["role"] == "assistant" else "Customer"
            print(f"{role}: {msg['content']}")
        if len(conversation) > 4:
            print("...")

if __name__ == "__main__":
    test_validation_system()
    test_retry_manager()

