# 🧠 Self-Reflective Code Agent

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Agentic-Workflow](https://img.shields.io/badge/Workflow-Agentic-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An autonomous AI agent designed to bridge the gap between natural language requirements and executable Python code. Unlike standard code generators, this agent operates in a **Closed-Loop Reflection** cycle: it writes code, executes it in a sandbox, analyzes errors, and refines the logic until the goal is achieved.

## 🔄 The Reflection Cycle

1. **Decomposition**: Breaks down the user requirement into logical steps.
2. **Implementation**: Generates modular Python code.
3. **Execution**: Runs the code and captures stdout, stderr, and 	racebacks.
4. **Reflection**: If errors occur, the agent analyzes the traceback and "reflects" on why it failed.
5. **Correction**: Generates a patch or rewrite based on the reflection.

## 🏗️ Architecture

`mermaid
graph LR
    Goal([User Goal]) --> Planner[Planner Agent]
    Planner --> Coder[Coder Agent]
    Coder --> Executor[Execution Sandbox]
    Executor -- Success --> Final[Verified Output]
    Executor -- Failure --> Traceback[Error Traceback]
    Traceback --> Reflector[Reflector Agent]
    Reflector -- Debugging Insight --> Coder
`

## 🚀 Installation

`ash
git clone https://github.com/SamruddhiBhor1/Self-Reflective-Code-Agent.git
cd Self-Reflective-Code-Agent
pip install -r requirements.txt
`

## 💻 Example Usage

`python
from agent import ReflectiveCoder

# Initialize agent
agent = ReflectiveCoder(api_key="your_openai_api_key")

# Task
task = "Write a script to calculate word frequency and plot a bar chart."
final_code = agent.run(task)
`

---
Created by **Samruddhi Bhor** - Generative AI Engineer