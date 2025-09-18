


> # Debt Collection Conversation Generator

This project provides a powerful and flexible system for generating large-scale, diverse, and realistic debt collection conversation datasets for training advanced phone agent AI models. It takes a base system prompt and a set of predefined scenarios to produce thousands of unique conversations, each with multiple variations.

This tool is designed to help AI developers create robust training data that covers a wide range of customer behaviors, technical issues, and legal situations commonly encountered in debt collection.

---

## Key Features

*   **100 Diverse Scenarios:** Comes with 100 predefined scenarios covering everything from simple payments to complex legal situations and hostile customers.
*   **10 Variations per Scenario:** Automatically generates 10 slightly different variations for each scenario, modifying names, debt amounts, and due dates.
*   **Multi-language Support:** Can be used with system prompts in any language (e.g., English, Arabic, Spanish).
*   **Special Tag Validation:** Ensures that generated conversations include required special tags like `(disconnect)`, `(transfer)`, `(function_1)`, etc., which are critical for training agent models to perform specific actions.
*   **Enhanced Validation & Retry:** Includes an advanced validation system that scores conversation quality and a retry manager that enhances prompts to fix issues in failed generations.
*   **JSONL Input/Output:** Reads system prompts from a simple JSONL file and writes the generated conversations to a clean JSONL output file.
*   **Customizable:** Easy to add new scenarios, customize variations (names, amounts), and adjust validation rules.
*   **Command-Line Interface:** Simple CLI for easy integration into automated data generation pipelines.





## How It Works

The conversation generation process follows these steps:

1.  **Load System Prompts:** The system reads one or more master system prompts from an input `jsonl` file. Each prompt defines the agent's identity, objectives, and core rules.

2.  **Select a Scenario:** The generator picks one of the 100 predefined debt collection scenarios (e.g., "Customer claims already paid," "Wrong person answers phone").

3.  **Create Variations:** It generates 10 unique variations for the selected scenario by randomizing:
    *   Customer Name
    *   Agent Name
    *   Debt Amount
    *   Due Date

4.  **Build the GPT-4.1-mini Prompt:** It combines the master system prompt with specific instructions for the selected scenario and variation. This new, detailed prompt is then used to guide the `GPT-4.1-mini` model.

5.  **Generate Conversation:** The system sends the detailed prompt to the `GPT-4.1-mini` API, which generates a complete, multi-turn conversation between the agent and the customer.

6.  **Validate and Retry:** The generated conversation is automatically validated against a set of quality rules:
    *   **Special Tag Presence:** Checks if the required special tags (e.g., `(disconnect)`) are included.
    *   **Quality Score:** Rates the conversation's naturalness, professionalism, and structure.
    *   **If validation fails,** the system enhances the prompt with specific feedback and retries the generation up to 3 times.

7.  **Save to JSONL:** All generated conversations (both successful and failed) are saved to an output `jsonl` file, which includes the conversation, validation status, and other metadata.




## How to Use

Follow these steps to set up and run the conversation generator.

### 1. Prerequisites

*   Python 3.8+
*   `pip` for installing packages
*   An OpenAI API key with access to the `gpt-4.1-mini` model

### 2. Installation

Clone the repository and install the required packages:

```bash
# Clone the repository (example)
git clone https://github.com/your-repo/conversation_generator.git
cd conversation_generator

# Install dependencies
pip install -r requirements.txt
```

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=\'your_openai_api_key_here\'
```

### 3. Prepare the Input File

Create an input file named `prompts.jsonl`. Each line in this file should be a JSON object containing a system prompt.

**Example `prompts.jsonl`:**

```json
{"id": "en_prompt_1", "language": "english", "system_prompt": "You are Salma, a professional account specialist from ClearGrid..."}
{"id": "es_prompt_1", "language": "spanish", "system_prompt": "Eres Sofía, una especialista profesional de cuentas de ClearGrid..."}
```

*   `id`: A unique identifier for the prompt.
*   `language`: The language of the prompt (e.g., "english", "arabic", "spanish").
*   `system_prompt`: The full text of the master system prompt.

You can also use the script to generate a sample input file:

```bash
python3 jsonl_processor.py --create-sample --input sample_prompts.jsonl
```

### 4. Run the Generator

Use the `jsonl_processor.py` script to start the generation process.

```bash
python3 jsonl_processor.py --input prompts.jsonl --output conversations.jsonl --scenarios 100
```

*   `--input`: Path to your input `jsonl` file.
*   `--output`: Path where the generated `conversations.jsonl` will be saved.
*   `--scenarios`: (Optional) The number of scenarios to generate (from 1 to 100). Defaults to 10 if not specified.

The script will process each prompt in the input file, generate 10 variations for each of the specified scenarios, and save all conversations to the output file.

### 5. Review the Output

The output file (`conversations.jsonl`) will contain one JSON object per line for each generated conversation.

**Example Output Entry:**

```json
{
  "scenario_id": "basic_payment_willing",
  "variation_id": 1,
  "conversation": [
    {"role": "assistant", "content": "Good afternoon, this is Salma..."},
    {"role": "user", "content": "Yes, I can pay now..."}
  ],
  "validation_passed": true,
  "special_tags_found": ["(function_1)"],
  "metadata": {
    "generated_at": "2023-10-27T10:00:00Z",
    "model": "gpt-4.1-mini",
    ...
  }
}
```

---

## File Structure

```
.
├── conversation_generator.py   # Core class for generating conversations
├── jsonl_processor.py          # Handles JSONL input/output and CLI
├── scenario_definitions.py     # Contains the 100 predefined scenarios
├── validation_system.py        # Enhanced validation and retry logic
├── test_complete_system.py     # End-to-end tests for the pipeline
├── requirements.txt            # Python package dependencies
└── README.md                   # This documentation file
```




## Customization

This system is designed to be easily customizable.

### Adding New Scenarios

To add more scenarios, simply edit the `DEBT_COLLECTION_SCENARIOS` list in the `scenario_definitions.py` file. Follow the existing structure:

```python
{
    "id": "your_new_scenario_id",
    "name": "A descriptive name for the scenario",
    "description": "A longer description of what happens.",
    "customer_behavior": "hostile", # e.g., cooperative, hostile, confused
    "outcome": "negative", # e.g., positive, negative, dispute
    "special_tags": ["(disconnect)"] # Required tags for this scenario
},
```

### Modifying Variations

You can change the names, debt amounts, and other variables used in variations by editing the lists in the `ConversationGenerator` class in `conversation_generator.py`.

### Adjusting Validation

The validation rules can be fine-tuned in `validation_system.py`. You can adjust the `quality_score` thresholds, add or remove `quality_indicators` and `red_flags`, or modify the `issues` that the system checks for.


