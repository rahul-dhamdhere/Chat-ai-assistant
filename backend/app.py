from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user message from the request
        data = request.json
        user_message = data.get('message', '')

        # Generate response using Ollama
        response = ollama.chat(
            model='mistral',  # Ensure this matches your installed model
            messages=[
                {
                    'role': 'user', 
                    'content': user_message
                }
            ]
        )

        # Extract the response content
        ai_message = response['message']['content']

        return jsonify({
            'response': ai_message
        })

    except Exception as e:
        return jsonify({
            'response': f'Error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)