from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Timestamp for tracking
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# Load model
llm = ChatOpenAI(temperature=0.7)

# Step 1 – summarize the emotional core
summary_prompt = PromptTemplate.from_template(
    """
You are a journaling companion helping a user reflect on their writing.

They wrote:

"{journal_entry}"

Summarize the emotional theme or core message in one sentence.
Use their tone and words when possible. Be empathetic, not robotic.
""".strip()
)

# Step 2 – offer gentle insight based on summary + entry
insight_prompt = PromptTemplate.from_template(
    """
A user has shared this journal entry:

"{journal_entry}"

And here's a summary of what they're feeling:

"{summary}"

Based on this, offer a short, supportive insight or realization.
Avoid advice. Speak warmly, truthfully, and calmly.
""".strip()
)

# Step 3 – reflection question based on entry + insight
question_prompt = PromptTemplate.from_template(
    """
A user shared this journal entry:

"{journal_entry}"

And here's the insight you offered them:

"{insight}"

Now, ask them one short reflection question that encourages deeper self-awareness or growth.
Keep it kind, personal, and supportive — not generic.
""".strip()
)

# Step 4 – Final response assembly
final_prompt = PromptTemplate.from_template(
    """
The user wrote a journal entry. You've already generated:

Summary:
"{summary}"

Insight:
"{insight}"

Reflection Question:
"{question}"

Now combine these into one warm, emotionally-aware response. Do not label the parts.
Write it as if you're speaking gently and naturally to the user in one message.
""".strip()
)

# Summary step
summary_chain = summary_prompt | llm | StrOutputParser()

# Insight step
insight_chain = insight_prompt | llm | StrOutputParser()

# Question step
question_chain = question_prompt | llm | StrOutputParser()

# Final assembly step
final_chain = final_prompt | llm | StrOutputParser()

# Combine all steps
full_reflection_chain = (
    RunnableLambda(lambda x: x)
    .assign(summary=summary_chain)
    .assign(insight=insight_chain)
    .assign(question=question_chain)
    .assign(final_message=final_chain)
    .with_config({"run_name": "journal_reflection_chain"})
)

# Export for use in run_agent.py
__timestamp__ = timestamp
__chain__ = full_reflection_chain
