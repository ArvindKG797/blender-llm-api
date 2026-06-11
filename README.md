Run API:

uvicorn api:app --reload

Endpoint:

POST /generate

Example:

{
  "prompt": "Generate BPY code to create stairs using cubes"
}

Response:

{
  "response": "import bpy ..."
}