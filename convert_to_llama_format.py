#!/usr/bin/env python3
"""
Convert Debt Collection Conversation Data to Llama 3.3 70B Fine-Tuning Format

This program converts the generated conversation data from the debt collection
conversation generator to the proper format for fine-tuning Llama 3.3 70B model.

Supports multiple output formats:
1. ShareGPT format (recommended for Unsloth)
2. ChatML format (alternative)
3. Alpaca format (single-turn)
4. Custom format

Author: Manus AI Assistant
Date: 2025-09-19
"""

import json
import argparse
from typing import List, Dict, Any, Optional
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ConversationConverter:
    """Convert conversation data to various fine-tuning formats."""
    
    def __init__(self, system_prompt: str):
        """
        Initialize converter with system prompt.
        
        Args:
            system_prompt (str): The system prompt to use for all conversations
        """
        self.system_prompt = system_prompt
        
    def load_conversations(self, conversations_file: str) -> List[Dict[str, Any]]:
        """
        Load conversations from JSONL file.
        
        Args:
            conversations_file (str): Path to conversations.jsonl file
            
        Returns:
            List[Dict]: List of conversation objects
        """
        conversations = []
        
        logger.info(f"Loading conversations from {conversations_file}")
        
        with open(conversations_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    conversation = json.loads(line.strip())
                    conversations.append(conversation)
                except json.JSONDecodeError as e:
                    logger.error(f"Error parsing JSON on line {line_num}: {e}")
                    continue
        
        logger.info(f"Loaded {len(conversations)} conversations")
        return conversations
    
    def load_system_prompt(self, prompts_file: str) -> str:
        """
        Load system prompt from prompts.jsonl file.
        
        Args:
            prompts_file (str): Path to prompts.jsonl file
            
        Returns:
            str: System prompt content
        """
        logger.info(f"Loading system prompt from {prompts_file}")
        
        with open(prompts_file, 'r', encoding='utf-8') as f:
            line = f.readline().strip()
            prompt_data = json.loads(line)
            system_prompt = prompt_data['system_prompt']
            
        logger.info(f"Loaded system prompt ({len(system_prompt)} characters)")
        return system_prompt
    
    def convert_to_sharegpt_format(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert conversations to ShareGPT format (recommended for Unsloth).
        
        Format:
        {
            "conversations": [
                {"from": "system", "value": "SYSTEM_PROMPT"},
                {"from": "human", "value": "USER_MESSAGE"},
                {"from": "gpt", "value": "ASSISTANT_RESPONSE"}
            ]
        }
        
        Args:
            conversations (List[Dict]): Original conversation data
            
        Returns:
            List[Dict]: ShareGPT formatted data
        """
        logger.info("Converting to ShareGPT format...")
        
        sharegpt_data = []
        
        for conv in conversations:
            # Extract conversation messages
            messages = conv.get('conversation', [])
            if not messages:
                continue
            
            # Build ShareGPT conversation
            sharegpt_conv = {
                "conversations": [
                    {"from": "system", "value": self.system_prompt}
                ]
            }
            
            # Convert role mappings
            for msg in messages:
                role = msg.get('role', '')
                content = msg.get('content', '')
                
                if role == 'user':
                    sharegpt_conv["conversations"].append({
                        "from": "human",
                        "value": content
                    })
                elif role == 'assistant':
                    sharegpt_conv["conversations"].append({
                        "from": "gpt", 
                        "value": content
                    })
            
            # Add metadata
            sharegpt_conv["metadata"] = {
                "scenario_id": conv.get('scenario_id', ''),
                "variation_id": conv.get('variation_id', ''),
                "validation_passed": conv.get('validation_passed', False),
                "special_tags_found": conv.get('special_tags_found', [])
            }
            
            sharegpt_data.append(sharegpt_conv)
        
        logger.info(f"Converted {len(sharegpt_data)} conversations to ShareGPT format")
        return sharegpt_data
    
    def convert_to_chatml_format(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert conversations to ChatML format.
        
        Format:
        {
            "messages": [
                {"role": "system", "content": "SYSTEM_PROMPT"},
                {"role": "user", "content": "USER_MESSAGE"},
                {"role": "assistant", "content": "ASSISTANT_RESPONSE"}
            ]
        }
        
        Args:
            conversations (List[Dict]): Original conversation data
            
        Returns:
            List[Dict]: ChatML formatted data
        """
        logger.info("Converting to ChatML format...")
        
        chatml_data = []
        
        for conv in conversations:
            # Extract conversation messages
            messages = conv.get('conversation', [])
            if not messages:
                continue
            
            # Build ChatML conversation
            chatml_conv = {
                "messages": [
                    {"role": "system", "content": self.system_prompt}
                ]
            }
            
            # Add conversation messages (roles already match ChatML)
            for msg in messages:
                role = msg.get('role', '')
                content = msg.get('content', '')
                
                if role in ['user', 'assistant']:
                    chatml_conv["messages"].append({
                        "role": role,
                        "content": content
                    })
            
            # Add metadata
            chatml_conv["metadata"] = {
                "scenario_id": conv.get('scenario_id', ''),
                "variation_id": conv.get('variation_id', ''),
                "validation_passed": conv.get('validation_passed', False),
                "special_tags_found": conv.get('special_tags_found', [])
            }
            
            chatml_data.append(chatml_conv)
        
        logger.info(f"Converted {len(chatml_data)} conversations to ChatML format")
        return chatml_data
    
    def convert_to_alpaca_format(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert conversations to Alpaca format (single-turn).
        
        Format:
        {
            "instruction": "SYSTEM_PROMPT + USER_MESSAGE",
            "input": "",
            "output": "ASSISTANT_RESPONSE"
        }
        
        Args:
            conversations (List[Dict]): Original conversation data
            
        Returns:
            List[Dict]: Alpaca formatted data
        """
        logger.info("Converting to Alpaca format...")
        
        alpaca_data = []
        
        for conv in conversations:
            messages = conv.get('conversation', [])
            if not messages:
                continue
            
            # Extract user and assistant messages
            user_messages = [msg['content'] for msg in messages if msg.get('role') == 'user']
            assistant_messages = [msg['content'] for msg in messages if msg.get('role') == 'assistant']
            
            # Create Alpaca entries for each user-assistant pair
            for i, (user_msg, assistant_msg) in enumerate(zip(user_messages, assistant_messages)):
                alpaca_entry = {
                    "instruction": f"{self.system_prompt}\n\nCustomer: {user_msg}",
                    "input": "",
                    "output": assistant_msg,
                    "metadata": {
                        "scenario_id": conv.get('scenario_id', ''),
                        "variation_id": conv.get('variation_id', ''),
                        "turn_number": i + 1,
                        "validation_passed": conv.get('validation_passed', False),
                        "special_tags_found": conv.get('special_tags_found', [])
                    }
                }
                alpaca_data.append(alpaca_entry)
        
        logger.info(f"Converted to {len(alpaca_data)} Alpaca format entries")
        return alpaca_data
    
    def save_data(self, data: List[Dict[str, Any]], output_file: str, format_name: str):
        """
        Save converted data to JSONL file.
        
        Args:
            data (List[Dict]): Converted data
            output_file (str): Output file path
            format_name (str): Format name for logging
        """
        logger.info(f"Saving {len(data)} entries to {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for entry in data:
                json.dump(entry, f, ensure_ascii=False)
                f.write('\n')
        
        logger.info(f"✅ {format_name} format data saved to {output_file}")
    
    def generate_training_stats(self, data: List[Dict[str, Any]], format_name: str) -> Dict[str, Any]:
        """
        Generate statistics about the training data.
        
        Args:
            data (List[Dict]): Training data
            format_name (str): Format name
            
        Returns:
            Dict: Statistics
        """
        stats = {
            "format": format_name,
            "total_entries": len(data),
            "total_tokens_estimate": 0,
            "avg_conversation_length": 0,
            "scenarios_covered": set(),
            "validation_passed_count": 0
        }
        
        total_length = 0
        
        for entry in data:
            # Count tokens (rough estimate: 1 token ≈ 4 characters)
            if format_name == "ShareGPT":
                conversations = entry.get("conversations", [])
                for conv in conversations:
                    stats["total_tokens_estimate"] += len(conv.get("value", "")) // 4
                total_length += len(conversations)
            elif format_name == "ChatML":
                messages = entry.get("messages", [])
                for msg in messages:
                    stats["total_tokens_estimate"] += len(msg.get("content", "")) // 4
                total_length += len(messages)
            elif format_name == "Alpaca":
                instruction = entry.get("instruction", "")
                output = entry.get("output", "")
                stats["total_tokens_estimate"] += (len(instruction) + len(output)) // 4
                total_length += 2  # instruction + output
            
            # Collect metadata
            metadata = entry.get("metadata", {})
            if metadata.get("scenario_id"):
                stats["scenarios_covered"].add(metadata["scenario_id"])
            if metadata.get("validation_passed"):
                stats["validation_passed_count"] += 1
        
        stats["avg_conversation_length"] = total_length / len(data) if data else 0
        stats["scenarios_covered"] = len(stats["scenarios_covered"])
        
        return stats

def main():
    """Main function to convert conversation data."""
    
    parser = argparse.ArgumentParser(description="Convert debt collection conversations to Llama 3.3 70B fine-tuning format")
    parser.add_argument("--conversations", required=True, help="Path to conversations.jsonl file")
    parser.add_argument("--prompts", required=True, help="Path to prompts.jsonl file")
    parser.add_argument("--output-dir", default="./llama_training_data", help="Output directory for converted data")
    parser.add_argument("--format", choices=["sharegpt", "chatml", "alpaca", "all"], default="all", 
                       help="Output format (default: all)")
    parser.add_argument("--stats", action="store_true", help="Generate training statistics")
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    print("🔄 DEBT COLLECTION DATA → LLAMA 3.3 70B FINE-TUNING FORMAT")
    print("=" * 70)
    
    try:
        # Initialize converter
        converter = ConversationConverter("")
        
        # Load system prompt
        system_prompt = converter.load_system_prompt(args.prompts)
        converter.system_prompt = system_prompt
        
        # Load conversations
        conversations = converter.load_conversations(args.conversations)
        
        if not conversations:
            logger.error("No conversations loaded. Exiting.")
            return
        
        # Convert to requested formats
        formats_to_convert = ["sharegpt", "chatml", "alpaca"] if args.format == "all" else [args.format]
        
        stats_data = {}
        
        for format_name in formats_to_convert:
            print(f"\n📊 Converting to {format_name.upper()} format...")
            
            if format_name == "sharegpt":
                converted_data = converter.convert_to_sharegpt_format(conversations)
                output_file = output_dir / "debt_collection_sharegpt.jsonl"
            elif format_name == "chatml":
                converted_data = converter.convert_to_chatml_format(conversations)
                output_file = output_dir / "debt_collection_chatml.jsonl"
            elif format_name == "alpaca":
                converted_data = converter.convert_to_alpaca_format(conversations)
                output_file = output_dir / "debt_collection_alpaca.jsonl"
            
            # Save data
            converter.save_data(converted_data, str(output_file), format_name.upper())
            
            # Generate stats if requested
            if args.stats:
                stats = converter.generate_training_stats(converted_data, format_name.upper())
                stats_data[format_name] = stats
        
        # Save statistics
        if args.stats:
            stats_file = output_dir / "training_statistics.json"
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats_data, f, indent=2, ensure_ascii=False, default=str)
            print(f"\n📈 Training statistics saved to {stats_file}")
        
        print("\n🎉 CONVERSION COMPLETED SUCCESSFULLY!")
        print(f"📁 Output directory: {output_dir}")
        print("\n🚀 NEXT STEPS:")
        print("1. Choose your fine-tuning framework:")
        print("   - Unsloth (recommended): Use ShareGPT format")
        print("   - TorchTune: Use ChatML format")
        print("   - Axolotl: Use ShareGPT or ChatML format")
        print("   - LLaMA-Factory: Use ChatML format")
        print("\n2. Hardware requirements for Llama 3.3 70B:")
        print("   - Minimum: 41GB VRAM (with QLoRA)")
        print("   - Recommended: 80GB VRAM (A100/H100)")
        print("   - Alternative: Multi-GPU setup or cloud platforms")
        print("\n3. Example fine-tuning command (Unsloth):")
        print("   See the generated README.md file for detailed instructions")
        
        # Generate README
        readme_content = generate_readme(output_dir, stats_data if args.stats else {})
        readme_file = output_dir / "README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"\n📚 README with instructions saved to {readme_file}")
        
    except Exception as e:
        logger.error(f"Error during conversion: {e}")
        raise

def generate_readme(output_dir: Path, stats: Dict[str, Any]) -> str:
    """Generate README with fine-tuning instructions."""
    
    readme = f"""# Debt Collection Agent - Llama 3.3 70B Fine-Tuning Data

This directory contains conversation data converted from the debt collection conversation generator, formatted for fine-tuning Llama 3.3 70B model.

## 📁 Files Generated

- `debt_collection_sharegpt.jsonl` - ShareGPT format (recommended for Unsloth)
- `debt_collection_chatml.jsonl` - ChatML format (TorchTune, LLaMA-Factory)
- `debt_collection_alpaca.jsonl` - Alpaca format (single-turn conversations)
- `training_statistics.json` - Dataset statistics
- `README.md` - This file

## 📊 Dataset Statistics

"""
    
    if stats:
        for format_name, stat_data in stats.items():
            readme += f"""### {format_name.upper()} Format
- **Total entries**: {stat_data.get('total_entries', 'N/A')}
- **Estimated tokens**: {stat_data.get('total_tokens_estimate', 'N/A'):,}
- **Scenarios covered**: {stat_data.get('scenarios_covered', 'N/A')}
- **Validation passed**: {stat_data.get('validation_passed_count', 'N/A')}
- **Avg conversation length**: {stat_data.get('avg_conversation_length', 'N/A'):.1f} messages

"""
    
    readme += """## 🚀 Fine-Tuning Instructions

### Option 1: Unsloth (Recommended)

```bash
# Install Unsloth
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

# Example fine-tuning script
python fine_tune_unsloth.py \\
    --model_name "unsloth/Llama-3.3-70B-Instruct" \\
    --dataset_path "debt_collection_sharegpt.jsonl" \\
    --output_dir "./llama-3.3-70b-debt-collection" \\
    --max_seq_length 2048 \\
    --load_in_4bit True \\
    --per_device_train_batch_size 1 \\
    --gradient_accumulation_steps 4 \\
    --warmup_steps 10 \\
    --num_train_epochs 1 \\
    --learning_rate 2e-4 \\
    --fp16 True \\
    --logging_steps 1 \\
    --save_strategy "epoch"
```

### Option 2: TorchTune

```bash
# Install TorchTune
pip install torchtune

# Configure and run fine-tuning
tune download meta-llama/Llama-3.3-70B-Instruct
tune run lora_finetune_single_device \\
    --config llama3_3_70B_lora_single_device \\
    dataset.source=debt_collection_chatml.jsonl
```

### Option 3: LLaMA-Factory

```bash
# Install LLaMA-Factory
pip install llamafactory

# Fine-tune with web UI
llamafactory-cli webui

# Or command line
llamafactory-cli train \\
    --model_name meta-llama/Llama-3.3-70B-Instruct \\
    --dataset debt_collection \\
    --template llama3 \\
    --finetuning_type lora \\
    --output_dir ./llama-3.3-debt-collection \\
    --per_device_train_batch_size 1 \\
    --gradient_accumulation_steps 8 \\
    --lr_scheduler_type cosine \\
    --logging_steps 10 \\
    --save_steps 500 \\
    --learning_rate 5e-5 \\
    --num_train_epochs 1.0 \\
    --max_samples 1000 \\
    --per_device_eval_batch_size 1 \\
    --evaluation_strategy steps \\
    --eval_steps 500 \\
    --fp16
```

## 💾 Hardware Requirements

### Minimum Requirements (QLoRA)
- **GPU**: 41GB VRAM (A6000, RTX 6000 Ada)
- **RAM**: 32GB system RAM
- **Storage**: 200GB free space

### Recommended (Full Fine-tuning)
- **GPU**: 80GB VRAM (A100, H100)
- **RAM**: 64GB system RAM
- **Storage**: 500GB free space

### Cloud Alternatives
- **Google Colab Pro+**: Limited but possible with QLoRA
- **AWS SageMaker**: ml.p4d.24xlarge instances
- **Azure ML**: Standard_ND96asr_v4 instances
- **RunPod**: RTX 4090 or A100 instances

## 🔧 Optimization Tips

1. **Use QLoRA**: Reduces memory usage by ~75%
2. **Gradient Checkpointing**: Trades compute for memory
3. **Mixed Precision**: Use fp16 or bf16
4. **Batch Size**: Start with 1, increase gradually
5. **Sequence Length**: Use 2048 or 4096 max
6. **Learning Rate**: Start with 2e-4 for LoRA

## 📈 Monitoring Training

- **Loss**: Should decrease steadily
- **Perplexity**: Lower is better
- **Validation**: Monitor for overfitting
- **Memory**: Watch GPU utilization
- **Time**: Expect 6-24 hours depending on setup

## 🎯 Expected Results

After fine-tuning, your model should:
- Handle debt collection scenarios professionally
- Follow compliance guidelines
- Use appropriate special tags (function_1, transfer, etc.)
- Maintain conversational flow
- Adapt to different customer behaviors

## 🔍 Evaluation

Test your fine-tuned model with:
- Scenario-specific prompts
- Edge cases from your training data
- Compliance validation
- Response quality assessment
- Special tag usage verification

## 📞 Support

For issues with:
- **Data conversion**: Check the conversion script logs
- **Fine-tuning**: Consult framework-specific documentation
- **Hardware**: Consider cloud alternatives or smaller models
- **Performance**: Adjust hyperparameters and training data

---

Generated by Debt Collection Conversation Generator
Date: {output_dir.stat().st_mtime if output_dir.exists() else 'N/A'}
"""
    
    return readme

if __name__ == "__main__":
    main()
