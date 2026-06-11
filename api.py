from fastapi import FastAPI
from pydantic import BaseModel

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

from peft import PeftModel

import torch

app = FastAPI()

# -----------------------------------
# REQUEST MODEL
# -----------------------------------

class PromptRequest(BaseModel):
    prompt: str

# -----------------------------------
# MODEL CONFIG
# -----------------------------------

MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

ADAPTER_PATH = "checkpoint-2109"

# -----------------------------------
# LOAD MODEL ONCE
# -----------------------------------

print("Loading model...")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map={"": 0},
    torch_dtype=torch.float16
)

model = PeftModel.from_pretrained(
    base_model,
    ADAPTER_PATH
)

print("Model Ready!")

# -----------------------------------
# API
# -----------------------------------

@app.post("/generate")
def generate(data: PromptRequest):

    prompt = f"""### Instruction:
{data.prompt}

### Response:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to(model.device)

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

    response = response.replace(
        prompt,
        ""
    ).strip()

    return {
        "response": response
    }