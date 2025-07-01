# agent-chaining

This project demonstrates how to build modular, multi-step AI agents using [LangChain](https://www.langchain.com/) and OpenAI — designed for testing, learning, and extending intelligent prompt workflows.

---

## Agents Included

### Professor Ted  
A full-stack coding coach that helps junior developers shape, critique, and refine their project ideas in three steps:

- Encouragement  
- Constructive critique  
- Refined next step

Uses `ConversationBufferMemory` for session awareness.

---

### Nightingale  
A journaling reflection agent that responds to user entries with gentle insight, built from layered understanding. Internally:

- Step 1: Emotional summary  
- Step 2: Gentle insight  
- Step 3: Reflection question  
- Step 4: Final message (summarized from all above)

Returns a **single warm reflection message** as seen in the Nightingale journaling web app.

---

## Features

- Built with LangChain `0.3.26` using LCEL (`RunnableLambda`)
- Structured multi-step chains with intermediate prompt logic
- Modular agent system (selectable via CLI at runtime)
- In-memory or stateless chain patterns (depending on agent)
- Clean output breakdown and message formatting
- Optional output logging for chain evaluation (planned)

---

## Agent Menu Example

```bash
$ python run_agent.py

Which agent would you like to run?

1. Professor Ted (project feedback)
2. Nightingale (journal reflection)
```

---

## Project Structure

```
agent-chaining/
├── .venv/                        # Python virtual environment
├── README.md                     # Project documentation (this file)
└── chain-lab/
    ├── chains/
    │   ├── professor_ted.py      # Ted's chain definition
    │   └── journal_reflection.py # Nightingale's multi-step reflection chain
    ├── run_agent.py              # Dynamic CLI launcher
    ├── logs.txt                  # Optional logging output
    ├── requirements.txt          # Python dependencies
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
   python run_agent.py
   ```

---

## Current Tech Stack

- Python 3.13+
- LangChain `0.3.26`
- `langchain-openai`
- LCEL chaining via `RunnableLambda`
- `PromptTemplate` + `StrOutputParser`
- In-memory message handling (for Professor Ted)

---

## Planned Improvements

- Output logging (`logs.txt`) with structured JSON lines
- Evaluation pipeline to test tone, clarity, usefulness
- A/B testing of different prompt versions or models
- Nightingale RAG-mode: include past journal entries via memory or context injection
- Web-based UI integration (streamed output + token cost monitoring)