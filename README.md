# Blender LLM API

Fine-tuned Blender Python (BPY) code generation API using:

* Qwen2.5-Coder-1.5B-Instruct
* QLoRA Fine-Tuning
* FastAPI Backend
* Hugging Face Transformers

### Fine-Tuning Method

QLoRA

### Adapter

checkpoint-2109/

### Purpose

Generate Blender Python (BPY) scripts from natural language instructions.

---

## Tested Environment

### Python

Python 3.11.9

### GPU

NVIDIA T400 4GB

### CUDA

CUDA 12.1

### PyTorch

Torch 2.5.1+cu121

---

## Clone Repository

```bash
git clone https://github.com/ArvindKG797/blender-llm-api.git
cd blender-llm-api
```

---

## Create Virtual Environment

```bash
py -3.11 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.11.x
```

---

## Install CUDA PyTorch

Install the GPU-enabled version first:

```bash
pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121
```

Verify:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

Expected:

```text
2.5.1+cu121
True
```

---

## Install Remaining Dependencies

```bash
pip install -r requirements.txt
```

---

## Run API

```bash
uvicorn api:app --reload
```

Expected:

```text
Loading model...
Model Ready!
```

---

## Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```json
{
  "prompt": "Generate BPY code to create a staircase using cubes"
}
```

---

## Repository Structure

```text
blender-llm-api/
│
├── api.py
├── requirements.txt
├── test_trained_model.py
├── README.md
│
└── checkpoint-2109/
    ├── adapter_config.json
    ├── adapter_model.safetensors
    ├── tokenizer.json
    ├── tokenizer_config.json
    └── training_args.bin
```

---

## Notes

* The repository contains only the LoRA adapter.
* The base model is automatically downloaded from Hugging Face on first run.
* Internet access is required during the first launch.
* Subsequent runs use the cached model locally.
* Python 3.14 is not recommended.
* Python 3.11.9 is the tested environment.

---
