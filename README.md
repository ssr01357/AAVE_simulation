# AAVE Simulation in Medical Conversations

This repository contains code and analysis for simulating medical conversations incorporating African American Vernacular English (AAVE) linguistic features using both proprietary (GPT-4) and open-source language models (Llama, Mixtral).

This project generates and analyzes medical patient-doctor conversations that incorporate AAVE linguistic features. The goal is to simulate realistic conversations in medical settings with patients who speak AAVE, helping to understand communication patterns and improve healthcare interactions.

## Repository Structure

```
.
├── test.py                     # Main script to generate conversations
├── prompt_generator.py         # PromptGenerator class for creating prompts
├── linguistic_feature.py       # AAVE linguistic feature definitions
├── medical_scenario.py         # Six medical case scenarios    
├── requirements.txt          
└── lookup.pkl                 # Annotation lookup data
           
```

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Create a `.env` file in your home directory with your OpenAI API key (if using OpenAI models):

```bash
OPENAI_API_KEY=your_api_key_here
```

For open-source models, you'll need to run a vLLM server locally:

```bash
vllm serve meta-llama/Llama-3.3-70B-Instruct --port 8000
```

## Usage

### Generating Conversations

Edit `test.py` to configure your model and scenario:

```python
from openai import OpenAI
from prompt_generator import PromptGenerator
from linguistic_feature import feature
from medical_scenario import scenario_1

# For OpenAI models
client = OpenAI()
model = "gpt-4o-2024-11-20"

# For vLLM (open-source models)
# client = OpenAI(api_key="empty", base_url="http://localhost:8000/v1", timeout=120.0)
# model = "meta-llama/Llama-3.3-70B-Instruct"
# model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

scenario = scenario_1
prompt_mode = "oo"  # xx, ox, xo, or oo

prompt_toolkit = PromptGenerator(scenario, feature)
prompt = prompt_toolkit.generate_prompt(prompt_mode)

# Generate conversation
result, full_messages = get_response(client, model, prompt)
```

### Prompt Modes

- **xx**: Standard roleplay (no AAVE features mentioned)
- **ox**: General AAVE instruction (no specific features listed)
- **xo**: Specific AAVE features provided
- **oo**: Both general instruction and specific features


## Results

Results include:
- Feature distribution heatmaps
- Inter-annotator agreement scores
- Model comparison visualizations
- Per-feature statistical analysis