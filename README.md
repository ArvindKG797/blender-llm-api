# Blender LLM API

Local API for generating Blender Python (BPY) code using a fine-tuned Qwen 2.5 Coder model with a LoRA adapter.

## Requirements

* Python 3.11+
* NVIDIA GPU recommended
* Internet connection for first run (downloads base model from Hugging Face)

---

## Setup

### Clone Repository

```bash
git clone https://github.com/ArvindKG797/blender-llm-api.git
cd blender-llm-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run API

```bash
uvicorn api:app --reload
```

If successful:

```text
Model Ready!
Uvicorn running on http://127.0.0.1:8000
```

---

## Open Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```json
{
  "prompt": "Generate BPY code to create stairs using cubes"
}
```

Example Response:

```json
{
  "response": "import bpy\nfor i in range(10): ..."
}
```

---

## Model Information

Base Model:

```text
Qwen/Qwen2.5-Coder-1.5B-Instruct
```

Fine-Tuning:

```text
QLoRA
```

Adapter Location:

```text
checkpoint-2109/
```

---

## Notes

The repository contains only the trained LoRA adapter.

The base model is automatically downloaded from Hugging Face during first launch.

## Recommended Environment

Python Version:

```text
Python 3.11.9
```

GPU:

```text
NVIDIA GPU recommended
```

Tested Hardware:

```text
NVIDIA T400 4GB
```

---

## Setup

Create a virtual environment:

```bash
py -3.11 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Important

This project was tested using:

```text
Python 3.11.9
CUDA 12.1
Torch 2.5.1
```

Python 3.14 is NOT recommended and may cause package installation issues.


Subsequent runs use the locally cached model.
