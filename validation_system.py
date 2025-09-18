#!/usr/bin/env python3
"""
Enhanced validation system for debt collection conversations
"""

import re
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Result of conversation validation"""
    passed: bool
    found_tags: List[str]
    missing_tags: List[str]
    quality_score: float
    issues: List[str]
    recommendations: List[str]

class ConversationValidator:
    """Enhanced validator for debt collection conversations"""
    
    def __init__(self):
        # All possible special tags
        self.special_tags = [
            "(disconnect)",
            "(transfer)", 
            "(function_1)",
            "(function_2)",
            "(hold)",
            "(mute)",
            "(conference)",
            "(callback)",
            "(escalate)"
        ]
        
        # Quality indicators
        self.quality_indicators = {
            "agent_professionalism": [
                "good morning", "good afternoon", "good evening",
                "thank you", "please", "may i", "i understand",
                "i appreciate", "professional", "courteous"
            ],
            "debt_collection_terms": [
                "debt", "loan", "payment", "amount", "balance", 
                "due", "overdue", "collection", "account"
            ],
            "regulatory_compliance": [
                "recorded", "quality purposes", "verify", "confirm",
                "legal action", "credit bureau", "background check"
            ],
            "natural_conversation": [
                "how are you", "i see", "i understand", "that's",
                "well", "actually", "really", "sure", "okay"
            ]
        }
        
        # Red flags that indicate poor quality
        self.red_flags = [
            "lorem ipsum",
            "placeholder",
            "example text",
            "sample conversation",
            "test message",
            "[insert",
            "{{",
            "}}"
        ]
    
    def validate_conversation(self, conversation: List[Dict[str, str]], 
                            required_tags: List[str] = None,
                            scenario_type: str = None) -> ValidationResult:
        """Comprehensive validation of a conversation"""
        
        if not conversation:
            return ValidationResult(
                passed=False,
                found_tags=[],
                missing_tags=required_tags or [],
                quality_score=0.0,
                issues=["Empty conversation"],
                recommendations=["Generate a non-empty conversation"]
            )
        
        # Find special tags
        found_tags = self._find_special_tags(conversation)
        
        # Check required tags
        missing_tags = []
        if required_tags:
            for req_tag in required_tags:
                # Normalize tag format - ensure it has parentheses
                normalized_req_tag = req_tag if req_tag.startswith('(') else f"({req_tag})"
                if normalized_req_tag not in found_tags:
                    missing_tags.append(req_tag)  # Keep original format for reporting
        
        # Calculate quality score
        quality_score = self._calculate_quality_score(conversation)
        
        # Identify issues
        issues = self._identify_issues(conversation, scenario_type)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(conversation, missing_tags, issues)
        
        # Determine if validation passed
        passed = (
            len(missing_tags) == 0 and  # All required tags present
            quality_score >= 0.6 and   # Minimum quality threshold
            len(issues) <= 2            # Maximum allowed issues
        )
        
        return ValidationResult(
            passed=passed,
            found_tags=found_tags,
            missing_tags=missing_tags,
            quality_score=quality_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _find_special_tags(self, conversation: List[Dict[str, str]]) -> List[str]:
        """Find all special tags in the conversation"""
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
    
    def _calculate_quality_score(self, conversation: List[Dict[str, str]]) -> float:
        """Calculate overall quality score (0.0 to 1.0)"""
        scores = []
        
        # Check for quality indicators
        for category, indicators in self.quality_indicators.items():
            category_score = self._check_indicators(conversation, indicators)
            scores.append(category_score)
        
        # Check for red flags (negative score)
        red_flag_penalty = self._check_red_flags(conversation)
        
        # Check conversation structure
        structure_score = self._check_conversation_structure(conversation)
        scores.append(structure_score)
        
        # Calculate weighted average
        base_score = sum(scores) / len(scores)
        final_score = max(0.0, base_score - red_flag_penalty)
        
        return min(1.0, final_score)
    
    def _check_indicators(self, conversation: List[Dict[str, str]], indicators: List[str]) -> float:
        """Check for presence of quality indicators"""
        full_text = " ".join([msg.get("content", "") for msg in conversation]).lower()
        
        found_count = sum(1 for indicator in indicators if indicator in full_text)
        return min(1.0, found_count / max(1, len(indicators) * 0.3))  # 30% threshold
    
    def _check_red_flags(self, conversation: List[Dict[str, str]]) -> float:
        """Check for red flags that indicate poor quality"""
        full_text = " ".join([msg.get("content", "") for msg in conversation]).lower()
        
        red_flag_count = sum(1 for flag in self.red_flags if flag in full_text)
        return red_flag_count * 0.3  # Each red flag reduces score by 0.3
    
    def _check_conversation_structure(self, conversation: List[Dict[str, str]]) -> float:
        """Check if conversation has proper structure"""
        if len(conversation) < 3:
            return 0.2  # Too short
        
        if len(conversation) > 30:
            return 0.7  # Too long, but not terrible
        
        # Check role alternation
        roles = [msg.get("role", "") for msg in conversation]
        alternation_score = self._check_role_alternation(roles)
        
        # Check message lengths
        length_score = self._check_message_lengths(conversation)
        
        return (alternation_score + length_score) / 2
    
    def _check_role_alternation(self, roles: List[str]) -> float:
        """Check if roles alternate properly"""
        if not roles:
            return 0.0
        
        # Should start with assistant (agent)
        if roles[0] != "assistant":
            return 0.5
        
        # Check alternation
        alternation_violations = 0
        for i in range(1, len(roles)):
            if roles[i] == roles[i-1]:
                alternation_violations += 1
        
        alternation_score = max(0.0, 1.0 - (alternation_violations / len(roles)))
        return alternation_score
    
    def _check_message_lengths(self, conversation: List[Dict[str, str]]) -> float:
        """Check if message lengths are reasonable"""
        lengths = [len(msg.get("content", "")) for msg in conversation]
        
        # Check for extremely short or long messages
        too_short = sum(1 for length in lengths if length < 10)
        too_long = sum(1 for length in lengths if length > 500)
        
        penalty = (too_short + too_long) / len(lengths)
        return max(0.0, 1.0 - penalty)
    
    def _identify_issues(self, conversation: List[Dict[str, str]], scenario_type: str = None) -> List[str]:
        """Identify specific issues with the conversation"""
        issues = []
        
        # Check for empty messages
        empty_messages = sum(1 for msg in conversation if not msg.get("content", "").strip())
        if empty_messages > 0:
            issues.append(f"{empty_messages} empty messages found")
        
        # Check for very short conversation
        if len(conversation) < 4:
            issues.append("Conversation too short (less than 4 exchanges)")
        
        # Check for missing agent introduction
        first_message = conversation[0].get("content", "") if conversation else ""
        if "cleargrid" not in first_message.lower() and "salma" not in first_message.lower():
            issues.append("Agent introduction missing or incomplete")
        
        # Check for abrupt ending
        last_message = conversation[-1].get("content", "") if conversation else ""
        if len(last_message) < 20:
            issues.append("Conversation ending seems abrupt")
        
        # Check for scenario-specific issues
        if scenario_type:
            scenario_issues = self._check_scenario_specific_issues(conversation, scenario_type)
            issues.extend(scenario_issues)
        
        return issues
    
    def _check_scenario_specific_issues(self, conversation: List[Dict[str, str]], scenario_type: str) -> List[str]:
        """Check for issues specific to the scenario type"""
        issues = []
        full_text = " ".join([msg.get("content", "") for msg in conversation]).lower()
        
        if "wrong_person" in scenario_type:
            if "transfer" not in full_text and "wrong" not in full_text:
                issues.append("Wrong person scenario should mention transfer or wrong person")
        
        elif "hostile" in scenario_type:
            if "angry" not in full_text and "upset" not in full_text and "frustrated" not in full_text:
                issues.append("Hostile scenario should show customer anger or frustration")
        
        elif "payment_willing" in scenario_type:
            if "pay" not in full_text and "payment" not in full_text:
                issues.append("Payment willing scenario should discuss payment")
        
        elif "legal" in scenario_type:
            if "legal" not in full_text and "attorney" not in full_text and "lawyer" not in full_text:
                issues.append("Legal scenario should mention legal terms")
        
        return issues
    
    def _generate_recommendations(self, conversation: List[Dict[str, str]], 
                                missing_tags: List[str], issues: List[str]) -> List[str]:
        """Generate recommendations for improving the conversation"""
        recommendations = []
        
        if missing_tags:
            recommendations.append(f"Include required special tags: {', '.join(missing_tags)}")
        
        if len(conversation) < 4:
            recommendations.append("Extend conversation to at least 4-6 exchanges")
        
        if len(conversation) > 20:
            recommendations.append("Consider shortening conversation for better focus")
        
        # Check for specific improvements
        full_text = " ".join([msg.get("content", "") for msg in conversation]).lower()
        
        if "thank you" not in full_text:
            recommendations.append("Add more polite language and courtesy")
        
        if "payment" not in full_text and "debt" not in full_text:
            recommendations.append("Ensure debt collection purpose is clear")
        
        if not any(tag in full_text for tag in ["(disconnect)", "(transfer)", "(function_1)", "(function_2)"]):
            recommendations.append("Include appropriate special tags for call handling")
        
        return recommendations

# Enhanced retry mechanism
class RetryManager:
    """Manages retry logic for failed conversation generation"""
    
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
        self.validator = ConversationValidator()
    
    def generate_with_retry(self, generator_func, prompt: str, required_tags: List[str] = None, 
                          scenario_type: str = None) -> Tuple[List[Dict[str, str]], ValidationResult]:
        """Generate conversation with retry logic"""
        
        for attempt in range(self.max_retries):
            try:
                # Generate conversation
                conversation, found_tags = generator_func(prompt)
                
                # Validate conversation
                validation_result = self.validator.validate_conversation(
                    conversation, required_tags, scenario_type
                )
                
                if validation_result.passed:
                    return conversation, validation_result
                else:
                    # Modify prompt based on validation feedback
                    prompt = self._enhance_prompt_based_on_feedback(prompt, validation_result)
                    print(f"Attempt {attempt + 1} failed validation. Retrying with enhanced prompt...")
                    
            except Exception as e:
                print(f"Attempt {attempt + 1} failed with error: {str(e)}")
                
        # Return last attempt even if failed
        return conversation if 'conversation' in locals() else [], validation_result if 'validation_result' in locals() else ValidationResult(False, [], [], 0.0, ["All attempts failed"], [])
    
    def _enhance_prompt_based_on_feedback(self, original_prompt: str, validation_result: ValidationResult) -> str:
        """Enhance prompt based on validation feedback"""
        enhancements = []
        
        if validation_result.missing_tags:
            enhancements.append(f"CRITICAL: You MUST include these special tags in the conversation: {', '.join(validation_result.missing_tags)}")
        
        if validation_result.quality_score < 0.6:
            enhancements.append("IMPORTANT: Make the conversation more natural and professional")
        
        if "Conversation too short" in validation_result.issues:
            enhancements.append("REQUIREMENT: Generate at least 6-8 message exchanges")
        
        if validation_result.recommendations:
            enhancements.append("IMPROVEMENTS NEEDED: " + "; ".join(validation_result.recommendations[:3]))
        
        if enhancements:
            enhancement_text = "\n\n## CRITICAL REQUIREMENTS FOR THIS RETRY:\n" + "\n".join(f"- {enhancement}" for enhancement in enhancements)
            return original_prompt + enhancement_text
        
        return original_prompt

