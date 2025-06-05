# 🤖 AI Coding Assistant

A powerful AI-powered coding assistant that helps developers with various programming tasks, from debugging to full project setup.

## ✨ Features

- 🤖 AI-powered code generation and assistance
- 🌤️ Weather information retrieval
- 📝 File operations
- 💻 Command execution
- 🔄 Interactive chat interface
- 🛠️ Multiple tool integrations

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Gemini API key

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

## 🛠️ Available Tools

### 1. Weather Information

- Function: `get_weather`
- Description: Fetches current weather conditions for any city
- Usage: `get_weather("city_name")`

### 2. File Operations

- Function: `write_file`
- Description: Creates or modifies code files
- Usage: `write_file("filepath", "content")`

### 3. Command Execution

- Function: `run_command`
- Description: Executes terminal commands
- Usage: `run_command("command")`

## 💻 Usage

1. Start the application:

```bash
python main.py
```

2. Enter your query in the interactive prompt
3. The AI will process your request and execute the appropriate tools

### Example Queries

- "What's the weather in Tokyo?"
- "Create a new React component"
- "Initialize a new project"

## 🔧 System Capabilities

### Frontend Development

- HTML5 (Semantic markup, Web Components)
- CSS3 (Grid/Flexbox, Variables)
- JavaScript (ES6+, TypeScript)
- React, Next.js, Vue.js

### Backend Development

- Node.js
- REST/GraphQL APIs
- Database integration
- Authentication

### DevOps

- Cloud deployment
- CI/CD pipelines
- Docker containerization

## 📝 Project Structure

```
.
├── main.py           # Main application file
├── requirements.txt  # Project dependencies
├── .env             # Environment variables
└── README.md        # Project documentation
```

## 🔒 Security

- API keys are stored in environment variables
- Input validation for all commands
- Secure file operations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for the AI capabilities
- Gemini API for language model integration
- All contributors who have helped shape this project
