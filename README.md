# agent-chaining

This project demonstrates how to build modular, multi-step AI agents using [LangChain](https://www.langchain.com/) and OpenAI.

The first working agent, **Professor Ted**, is a friendly full-stack coding coach designed to help junior developers refine their ideas through:

1. Encouragement  
2. Constructive critique  
3. Clear next-step suggestions  

---

## Features

- Clean, sequential chaining using LangChain  
- Structured 3-part output for clarity  
- Dynamic agent name and timestamp per run  
- Easy to extend with memory, persona, or tools  

---

## Project Structure

```
agent-chaining/
├── README.md                # Project documentation
└── chain-lab/
    ├── chains/             # Contains agent logic files
    ├── logs.txt            # Optional logging output
    ├── main.py             # Entry point to run Professor Ted
    └── requirements.txt    # Python dependencies
```

---

## Getting Started

1. Clone the repo:
    ```bash
    git clone https://github.com/your-username/agent-chaining.git
    cd agent-chaining
    ```

2. Navigate into the project:
    ```bash
    cd chain-lab
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate    # On Git Bash or WSL
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

## Planned Improvements

- Add memory so Ted can recall past ideas  
- Introduce more agent roles (e.g., legal, UX, ethics)  
- Support for saving and exporting coaching sessions  
