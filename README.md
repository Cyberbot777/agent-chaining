# agent-chaining

This project demonstrates how to build modular, memory-aware, multi-step AI agents using [LangChain](https://www.langchain.com/) and OpenAI.

The main agent, **Professor Ted**, is a full-stack coding coach designed to help junior developers shape, critique, and improve their project ideas step-by-step.

---

## Features

- Built with LangChain `0.3.26` using LCEL (`RunnableLambda`)
- Structured 3-part coaching flow:
  - Encouragement
  - Constructive critique
  - Refined next step
- In-memory conversation buffer for multi-step contextual continuity (per session)
- Timestamp and persona baked into output
- Modular chain structure for easy reuse and extension

---

## Memory Behavior

This project uses `ConversationBufferMemory` from LangChain to simulate short-term memory during a single run:

- Memory is manually updated using `.add_user_message()` and `.add_ai_message()` after each chain invocation
- The memory is **in-memory only** — it resets every time you restart the script
- Chat history is passed into each step of the chain using `MessagesPlaceholder("chat_history")`
- At the end of each session, all stored messages are printed to the terminal for visibility

This approach is ideal for testing how conversation context flows through chained steps — no database or file logging is needed.

---

## Project Structure

```
agent-chaining/
├── .venv/                        # Python virtual environment
├── README.md                     # Project documentation (this file)
└── chain-lab/
    ├── chains/
    │   └── professor_ted.py      # Agent chain definition using RunnableLambda
    ├── logs.txt                  # Optional logging output
    ├── main.py                   # Entry point to run Professor Ted
    └── requirements.txt          # Python dependencies
```

---

## Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/agent-chaining.git
   cd agent-chaining
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # On Git Bash or WSL
   ```

3. Navigate into the code directory:

   ```bash
   cd chain-lab
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your-key-here
   ```

6. Run the agent:

   ```bash
   python main.py
   ```

---

## Current Tech Stack

- Python 3.13+
- LangChain `0.3.26`
- `langchain-openai`
- LCEL + `RunnableLambda` chaining
- `ConversationBufferMemory` (in-memory only)

---

## Planned Improvements

- Add streaming and UI layer
- Support follow-up conversations with memory context
- Introduce additional coaching roles (e.g., design mentor, ethics coach)
- Export coaching transcripts to file or database
