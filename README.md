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

Subsequent runs use the locally cached model.
