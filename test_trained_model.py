from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

from peft import PeftModel

import torch

# -----------------------------------
# MODEL
# -----------------------------------

MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

ADAPTER_PATH = "../outputs/qwen_1_5b_qlora/checkpoint-2109"

# -----------------------------------
# 4-BIT CONFIG
# -----------------------------------

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

# -----------------------------------
# TOKENIZER
# -----------------------------------

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# -----------------------------------
# BASE MODEL
# -----------------------------------

print("Loading base model...")

base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map={"": 0},
    torch_dtype=torch.float16
)

# -----------------------------------
# LOAD LORA ADAPTER
# -----------------------------------

print("Loading trained LoRA adapter...")

model = PeftModel.from_pretrained(
    base_model,
    ADAPTER_PATH
)

print("Model ready!")

# -----------------------------------
# PROMPT
# -----------------------------------

prompt = """### Instruction:
Generate BPY code to Create rotating sphere chain.

### Response:
"""

inputs = tokenizer(
    prompt,
    return_tensors="pt"
).to(model.device)

# -----------------------------------
# GENERATION
# -----------------------------------

outputs = model.generate(
    **inputs,
    max_new_tokens=120,
    temperature=0.1,
    do_sample=False,
    repetition_penalty=1.2
)

response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

response = response.replace(prompt, "").strip()

# -----------------------------------
# OUTPUT
# -----------------------------------

print("\nMODEL OUTPUT:\n")
print(response)