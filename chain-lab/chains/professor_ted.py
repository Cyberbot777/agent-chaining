from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
llm = ChatOpenAI(temperature=0.7)

# Simple in-memory buffer for current session
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Timestamp for tracking
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# Step 1: Encouragement
encourage_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder("chat_history"),
    ("system", "[Professor Ted] You are a friendly full-stack coding coach."),
    ("human", 'A junior developer shares this idea: "{idea}". Offer a brief, supportive review.')
])
encourage_chain = encourage_prompt | llm | StrOutputParser()

# Step 2: Critique
critique_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder("chat_history"),
    ("system", "[Professor Ted] Based on this evaluation: \"{evaluation}\" What are 1–2 challenges or improvements the student might consider? Be kind but direct.")
])
critique_chain = critique_prompt | llm | StrOutputParser()

# Step 3: Refined Idea
refine_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder("chat_history"),
    ("system", "[Professor Ted] Based on these thoughts: \"{critique}\" Suggest a more refined project idea or next step. Keep it short and inspiring.")
])
refine_chain = refine_prompt | llm | StrOutputParser()

# Chain steps together
ted_chain = (
    RunnableLambda(lambda x: x)
    .assign(evaluation=encourage_chain)
    .assign(critique=critique_chain)
    .assign(refined=refine_chain)
    .with_config({"run_name": "professor_ted"})
)

# Export for use in main.py
__timestamp__ = timestamp
__memory__ = memory
