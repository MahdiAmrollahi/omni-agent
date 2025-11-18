# 🤖 Multi-Tool AI Agent

An intelligent AI assistant with the ability to use various tools to perform complex tasks. This project is built using **LangChain** and **Google Gemini**.

## ✨ Features

- 🧮 **Calculator**: Perform mathematical operations
- 📁 **File Search**: Search through PDF, TXT, and Markdown files
- 🗄️ **SQL Database**: Execute SQLite queries
- 🐍 **Python Code Execution**: Run Python code in a secure environment
- 🌐 **Web Scraper**: Extract content from web pages
- 📋 **Task Planner**: Break down goals into actionable steps

## 🛠️ Available Tools

### 1. Calculator
Perform mathematical operations (add, subtract, multiply, divide, percentage)

### 2. File Search
Search for text in `.txt`, `.md`, and `.pdf` files within a specified folder

### 3. SQL Database
Execute SQL queries on a SQLite database

### 4. Python Runner
Execute Python code in a secure and restricted environment

### 5. Web Scraper
Extract content from web pages

### 6. Task Planner
Break down complex goals into executable steps with JSON output

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-tool-ai-agent.git
cd multi-tool-ai-agent
```

### 2. Create Virtual Environment

```bash
python -m venv env

# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

### 3. Install Dependencies

Install all required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**Main dependencies:**
- `langchain` - LangChain framework
- `langchain-google-genai` - Google Gemini integration
- `langchain-community` - Community tools and integrations
- `python-dotenv` - Environment variable management
- `pypdf` - PDF file processing
- `beautifulsoup4` - Web scraping
- `httpx` - HTTP client

See `requirements.txt` for the complete list of dependencies.

### 4. Set Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

To get an API Key, visit [Google AI Studio](https://makersuite.google.com/app/apikey).

## 💻 Usage

### Basic Usage

Run the `one.py` file:

```bash
python one.py
```

Then enter your query. The agent will automatically select and use the appropriate tools.

### Usage Examples

```
Enter your query: Calculate 25 percent of 200
Enter your query: Search for "Python" in the docs folder
Enter your query: SELECT * FROM users WHERE age > 18
Enter your query: Scrape content from https://example.com
Enter your query: I want to build a website
```

## 📁 Project Structure

```
.
├── agent/
│   ├── __init__.py
│   ├── client.py          # Agent configuration and Gemini model setup
│   └── messages.py         # System messages
├── tools/
│   ├── __init__.py
│   ├── calculator_.py     # Calculator tool
│   ├── file_search_.py    # File search tool
│   ├── sql_.py            # Database tool
│   ├── code_executer_.py  # Python code execution tool
│   ├── web_scrapper_.py   # Web scraper tool
│   └── task_planner_.py   # Task planning tool
├── docs/                  # Folder for searchable files
├── database.db           # SQLite database
├── one.py                # Main execution file
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables file (should not be committed)
```

## 🔧 Development

### Adding a New Tool

1. Create a new file in the `tools/` folder
2. Use the `@tool` decorator:

```python
from langchain.tools import tool

@tool
def my_new_tool(param: str) -> str:
    """Tool description"""
    # Tool code
    return result
```

3. Add the tool to `tools/__init__.py`
4. Add the tool to the `agent_tools` list in `one.py`

## 📝 Code Example

```python
from tools import calculator, file_search, sql_database
from agent import agent_create
from langchain_core.messages import HumanMessage

# Create agent with tools
agent_tools = [calculator, file_search, sql_database]
model = agent_create(agent_tools)

# Send message
response = model.invoke({
    "history": [HumanMessage(content="Calculate 10 + 20")]
})

print(response.content)
```

## ⚠️ Security Notes

- **Python Runner**: Code execution is performed in a restricted environment. Some operations like `import os` and `import sys` are blocked.
- **API Key**: Never hardcode your API key. Always use the `.env` file.
- **Database**: Before executing sensitive queries, make sure your database is backed up.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the amazing framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) for the powerful AI model

## 📧 Contact

If you have any questions or suggestions, please open an Issue.

---

⭐ If you find this project useful, please give it a star!
