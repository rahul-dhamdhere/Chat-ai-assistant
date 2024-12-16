from flask import Flask
from langchain_ollama import OllamaLLM
model = OllamaLLM(model="mistral")
app= Flask(__name__)
@app.route('/')
def hello_world():
    result= model.invoke(input="say hello to project same as notebooklm")
    return result
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)