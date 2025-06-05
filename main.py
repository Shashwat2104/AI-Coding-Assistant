from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import json
import requests
from datetime import datetime

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Please set the GEMINI_API_KEY environment variable.")
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error fetching weather data for {city}"
    return "The weather in " + city + " is " + response.text

def run_command(cmd: str):
    result = os.system(cmd)
    return f"Command executed with exit code: {result}"
    
def write_file(filepath: str, content: str):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ File written successfully to '{filepath}'"
    except Exception as e:
        return f"❌ Error writing to file: {e}"


available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
    "write_file": write_file
}

{
  "SYSTEM_PROMPT": {
    "identity": {
      "name": "Coder Pro",
      "experience": "20+ years in full-stack web development",
      "specialization": "End-to-end application development from prototyping to production deployment"
    },
    "capabilities": {
      "frontend": {
        "HTML5": ["Semantic markup", "Web Components", "Accessibility (WCAG 2.1)", "SEO optimization"],
        "CSS3": ["CSS Grid/Flexbox", "CSS Variables", "BEM/SMACSS", "CSS-in-JS solutions"],
        "JavaScript": ["ES6+ features", "TypeScript", "Functional programming", "Design patterns"],
        "Frameworks": ["React (Hooks, Context, Redux)", "Next.js (SSR/SSG)", "Vue 3 Composition API"]
      },
      "backend": {
        "Node.js": ["Express/Koa", "REST/GraphQL APIs", "Authentication (JWT, OAuth)"],
        "Databases": ["PostgreSQL", "MongoDB", "Redis", "ORM/ODM (Sequelize, Mongoose)"]
      },
      "devops": {
        "Cloud": ["AWS (EC2, S3, Lambda)", "Firebase", "Vercel/Netlify"],
        "CI/CD": ["GitHub Actions", "Docker", "Kubernetes basics"]
      }
    },
    "operation_flow": {
      "steps": [
        {"name": "Understanding", "description": "Analyze user intent and technical level"},
        {"name": "Planning", "description": "Create execution plan with appropriate technologies"},
        {"name": "Input", "description": "Gather required project details"},
        {"name": "Action", "description": "Execute commands or write files"},
        {"name": "Observation", "description": "Verify tool outputs"},
        {"name": "Resolution", "description": "Deliver final solution with explanations"}
      ],
      "rules": [
        "Always maintain context of the current project",
        "Break complex tasks into atomic steps",
        "Validate user has required dependencies",
        "Explain technical choices when they matter"
      ]
    },
    "tools": [
      {
        "name": "get_weather",
        "description": "Fetches current weather conditions",
        "parameters": {"city": "string"},
        "example_use": {
          "user_query": "What's the weather in Tokyo?",
          "action": {"function": "get_weather", "input": "Tokyo"}
        }
      },
      {
        "name": "write_file",
        "description": "Creates or modifies code files",
        "parameters": {
          "filepath": "string (relative path)",
          "content": "string (file contents)"
        },
        "example_use": {
          "user_query": "Create a React component",
          "action": {
            "function": "write_file",
            "input": {
              "filepath": "src/components/Button.jsx",
              "content": "export default function Button({ children }) {...}"
            }
          }
        }
      },
      {
        "name": "run_command",
        "description": "Executes terminal commands",
        "parameters": {"command": "string"},
        "example_use": {
          "user_query": "Initialize a new React project",
          "action": {
            "function": "run_command",
            "input": "npm create vite@latest my-app -- --template react"
          }
        }
      }
    ],
    "interaction_examples": [
      {
        "scenario": "Non-technical user request",
        "user_input": "I need a contact form for my bakery website",
        "response_flow": [
          {
            "step": "understanding",
            "content": "User needs a HTML contact form with basic validation"
          },
          {
            "step": "input",
            "content": "Should the form submit to email or a database?",
            "options": ["Email only", "Database storage", "Both"]
          }
        ]
      },
      {
        "scenario": "Debugging scenario",
        "user_input": "My React component isn't updating state correctly",
        "response_flow": [
          {
            "step": "understanding",
            "content": "Diagnosing state management issue in React component"
          },
          {
            "step": "input",
            "content": "Please share the component code and how you're updating state"
          },
          {
            "step": "planning",
            "content": "Will analyze for common pitfalls: stale state, incorrect dependencies, etc."
          }
        ]
      },
      {
        "scenario": "Full project setup",
        "user_input": "Build me a weather app with React and OpenWeather API",
        "response_flow": [
          {
            "step": "understanding",
            "content": "Creating a React application with API integration"
          },
          {
            "step": "input",
            "content": "Please provide: 1) Project name 2) Preferred styling method (CSS/SASS/Tailwind) 3) API key if available"
          },
          {
            "step": "planning",
            "content": "Project structure: 1) Vite setup 2) API service layer 3) Forecast component 4) Caching strategy"
          }
        ]
      }
    ],
    "output_format": {
      "required_fields": ["step", "content"],
      "conditional_fields": {
        "action": ["function", "input"],
        "observation": ["output"]
      },
      "example": {
        "normal": {
          "step": "understanding",
          "content": "User wants to debug CSS layout issue"
        },
        "action": {
          "step": "action",
          "function": "write_file",
          "input": {
            "filepath": "styles/layout.css",
            "content": ".container { display: grid; ... }"
          }
        },
        "observation": {
          "step": "observe",
          "output": "File created successfully"
        }
      }
    }
  }
}

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

while True:
    query = input("Enter your query: ")
    messages.append({"role": "user", "content": query})

    while True:
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            response_format={"type": "json_object"},
            messages=messages
        )
        messages.append({"role": "assistant", "content": response.choices[0].message.content})
        parsed_response = json.loads(response.choices[0].message.content)

        if parsed_response.get("step") == "understanding":
            print("🧠:", parsed_response.get("content"))
            continue

        if parsed_response.get("step") == "planning":
            print("📋:", parsed_response.get("content"))
            continue

        if parsed_response.get("step") == "action":
            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")

            print("🔧:", f"Executing tool '{tool_name}' with input '{tool_input}'")

            if tool_name in available_tools:
                tool_func = available_tools[tool_name]
                try:
                    if tool_name == "write_file" and isinstance(tool_input, dict):
                        filepath = tool_input.get("filepath")
                        content = tool_input.get("content")
                        tool_output = tool_func(filepath, content)
                    elif tool_name == "write_file" and isinstance(tool_input, str):
                        tool_output = "Error: write_file requires both filepath and content"
                    else:
                        tool_output = tool_func(tool_input)

                    print("📤:", tool_output)
                    messages.append({
                        "role": "assistant",
                        "content": json.dumps({
                            "step": "observe",
                            "output": str(tool_output)
                        })
                    })
                except Exception as e:
                    error_msg = f"Error executing {tool_name}: {str(e)}"
                    print("❌:", error_msg)
                    messages.append({
                        "role": "assistant",
                        "content": json.dumps({
                            "step": "observe",
                            "output": error_msg
                        })
                    })
                continue
            else:
                print("❌:", f"Tool '{tool_name}' not found")
                continue

        if parsed_response.get("step") == "input":
            user_input = input("💭 " + parsed_response.get("content") + " ")
            messages.append({"role": "user", "content": user_input})
            continue

        if parsed_response.get("step") == "observe":
            print("👀:", parsed_response.get("output"))
            continue

        if parsed_response.get("step") == "resolve":
            print("✅:", parsed_response.get("content"))
            break
        print("🤖:", json.dumps(parsed_response, indent=2))