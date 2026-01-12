# AgenticAI Introduction Practical

This repository is a practical introduction to agentic AI: what agents are, how they differ from tools, and how modern frameworks like LangChain, LangGraph, LlamaIndex, and CrewAI help you build automated, LLM-powered systems.

The main goal is to clarify the core concepts so we can work effectively with any agent framework, not just a specific library.

## Repository Overview

This repository focuses on:

- Showing how LLMs power agent behavior
- Comparing popular agent frameworks and their typical use cases
- Emphasizing fundamentals and practical experimentation

You will learn to think of agents as autonomous decision-makers that call tools and APIs to achieve goals.

## Core Concepts

### 1. Agentic AI Frameworks

The project introduces several popular frameworks used for building agents:

- LangChain
  - A base framework for building LLM-powered applications, including agents.
  - Common use cases:
    - Chatbots
    - Retrieval-Augmented Generation (RAG)
    - Simple single-agent workflows.

- LangGraph
  - Built on top of LangChain.
  - Designed for complex, multi-agent workflows.
  - Supports:
    - Graph/state-machine style orchestration
    - Communication between agents and tools
    - Iterative and branching workflows.

- LlamaIndex
  - Initially focused on:
    - Data indexing
    - RAG over your own data.
  - Evolved to also support:
    - Agent creation for Q&A
    - Custom document processing workflows.

- CrewAI
  - Focused on role-based, multi-agent systems.
  - Often built on top of LangChain.
  - Suitable for:
    - End-to-end automation
    - Teams of agents with specific roles (e.g., researcher, planner, executor).

### 2. Agents vs Tools

Understanding the distinction between agents and tools is central to this project.

#### Agent

An agent is:

- An entity or system that can:
  - Observe inputs or events
  - Make autonomous decisions based on rules or AI models
  - Trigger actions and execute functions to achieve a goal
- It can:
  - Decide which tool to call and when
  - Plan multiple steps
  - Stop when the goal is reached or a condition is satisfied

You can think of an agent as the decision-maker and orchestrator.

#### Tool

A tool is:

- A callable function, API, or service that performs a specific task, such as:
  - Validating a transaction
  - Calling an external API
  - Querying a database
  - Sending notifications or emails
- Tools are not autonomous; they run when requested by an agent.

You can think of a tool as a utility; the agent decides when and how to use it.

### 3. Role of LLMs in Agentic AI

Large Language Models (LLMs) such as OpenAI models, Gemini, and the Llama series are essential for agentic AI. They provide:

- Natural language understanding:
  - Interpreting user instructions and queries
- Reasoning and planning:
  - Breaking down tasks into steps
  - Choosing which tools to call and with what arguments
- Generation capabilities:
  - Producing text, code, or tool call payloads
- Context handling:
  - Using conversation history and other context to guide decisions

LLMs enable agents to handle open-ended tasks and dynamic workflows instead of just fixed rule-based logic.

### 4. Framework Differences and Use Cases

A simplified view of when each framework is typically used:

- LangChain
  - Good for:
    - Prototyping LLM apps and agents
    - Basic chatbots
    - RAG applications
  - Focus on building blocks: chains, tools, agents.

- LangGraph
  - Good for:
    - Complex workflows
    - Multi-agent systems that need explicit state management
    - Scenarios where agents and tools interact in a graph or state machine.

- LlamaIndex
  - Good for:
    - Document-centric applications
    - Q&A over PDFs, web pages, knowledge bases
    - Agent behavior on top of custom indexes.

- CrewAI
  - Good for:
    - Role-based multi-agent collaboration
    - End-to-end processes where each agent has a specific responsibility.

## Key Takeaways

- Agentic AI is about building autonomous systems that:
  - Make decisions
  - Use tools
  - Execute tasks to achieve defined goals

- LangChain, LangGraph, LlamaIndex, and CrewAI are popular frameworks for building such systems, each with:
  - Different abstractions
  - Different strengths and ideal use cases

- Core concepts you must understand to use any framework effectively:
  - What makes an agent (role, goal, decision-making loop)
  - What tools are available and how they are defined
  - How LLMs are used to connect goals, observations, and tool calls

- Building an agent generally involves:
  1. Defining the agent’s role (what it is responsible for)
  2. Specifying its goal (what success looks like)
  3. Listing its tools (functions/APIs it can call)
  4. Designing prompts and instructions for the LLM
  5. Executing and iterating through practical experiments

- The project emphasizes practice:
  - Running examples
  - Modifying prompts and tools
  - Trying different frameworks to deepen understanding.

## Getting Started

Note: Adjust file names and commands based on the actual repository structure.

### 1. Clone the Repository

```bash
git clone https://github.com/Anurag0798/AgenticAI-Introduction-Practical.git

cd AgenticAI-Introduction-Practical
```

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

If a `requirements.txt` is provided:

```bash
pip install -r requirements.txt
```

Typical dependencies may include:

- langchain
- langgraph
- llama-index
- crewai
- LLM client libraries (e.g., openai)
- python-dotenv (for environment variables)

### 4. Configure Environment Variables

If external LLMs are used, create a `.env` file and set keys like:

```env
OPENAI_API_KEY=your_openai_api_key_here
# or other provider keys
```

Check the code for the exact variable names.

### 5. Run Examples or Notebooks

Look in the repository for:

- Python scripts (`*.py`)
- Jupyter notebooks (`*.ipynb`)

Examples (these are illustrative; use actual filenames from the repo):

```bash
python simple_agent_example.py

jupyter notebook
```

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Open a pull request with a clear description of your modifications.

## License

This project is open-source. See the `LICENSE` file in the repository for full details.