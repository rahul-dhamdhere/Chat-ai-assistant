# AI Chat Assistant with Mistral 7B

![AI Chat Assistant](images/chat_assistant.png)

## Project Overview

 This custom AI chat assistant is a sophisticated conversational agent designed to provide seamless, interactive, and engaging interactions. It leverages the power of Mistral, a versatile large language model, as its base for understanding and responding to user queries effectively. The assistant exhibits a high level of context awareness, enabling it to maintain conversations with coherence and relevance over multiple exchanges. It's equipped to handle a wide range of topics, making it an ideal tool for various applications such as customer service, education, entertainment, and more. The assistant has been finely-tuned for user experience, ensuring that responses are both informative and friendly. This custom AI chat assistant is designed to cater to the unique needs of its users, learning and adapting over time to deliver personalized interactions that feel intuitive and natural.

## Features

- Interactive chat interface
- AI responses generated using the Mistral 7B model
- Responsive design for mobile and desktop
- Easy setup and deployment

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy (if using a database)
- Ollama (for the Mistral model)

### Download Mistral 7B Locally

To use the Mistral 7B model, you need to download it locally. Follow these steps:

1. **Install Ollama**: Visit [Ollama's official website](https://ollama.ai/) and follow the installation instructions for your operating system.

2. **Pull the Mistral Model**:
   ```bash
   ollama pull mistral
### Download Mistral Model

### Installation
**Clone the Repository:**

bash
Insert Code
Run
Copy code
git clone https://github.com/yourusername/ai-chat-assistant.git
cd ai-chat-assistant
Create a Virtual Environment (optional but recommended):

bash
Insert Code
Run
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages:

bash
Insert Code
Run
Copy code
pip install -r requirements.txt
Set Up the Database (if using SQLite):

bash
Insert Code
Run
Copy code
python -c "from app import db; db.create_all()"
Running the Application
To start the Flask application, run the following command:

bash
Insert Code
Run
Copy code
python app.py
The application will be accessible at http://localhost:5000 in your web browser.

### Usage
Open your web browser and navigate to http://localhost:5000.
Type your message in the input box and press "Send".
The AI will respond based on your input.
### Chat Interface
![pc-interface-image](pcview.png)
![mobile-interface-image](mobileview.png)
### Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Ollama for providing the Mistral model.
Flask for the web framework.
SQLite for lightweight database storage.
Contact
For any questions or feedback, feel free to reach out:

Email: your.email@example.com
GitHub: yourusername