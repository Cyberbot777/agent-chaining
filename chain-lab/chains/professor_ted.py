from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
llm = OpenAI(temperature=0.7)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")


# Step 1: Encouraging Review
idea_prompt = PromptTemplate(
    input_variables=["idea"],
    template="""
[Professor Ted]

You are a friendly full-stack coding coach.

A junior developer shares this idea: "{idea}"

Offer a brief, supportive review of the idea. Respond like you're encouraging a student.
"""
)
idea_chain = LLMChain(llm=llm, prompt=idea_prompt, output_key="evaluation")

# Step 2: Constructive Critique
critique_prompt = PromptTemplate(
    input_variables=["evaluation"],
    template="""
[Professor Ted]

Based on this evaluation: "{evaluation}"

What are 1–2 challenges or improvements the student might consider?
Be kind but direct.
"""
)
critique_chain = LLMChain(llm=llm, prompt=critique_prompt, output_key="critique")

# Step 3: Refined Suggestion
refine_prompt = PromptTemplate(
    input_variables=["critique"],
    template="""
[Professor Ted]

Based on these thoughts: "{critique}"

Suggest a more refined project idea or next step the student can take.
Keep it short and inspiring.
"""
)
refine_chain = LLMChain(llm=llm, prompt=refine_prompt, output_key="refined")

# Full sequential chain including intro
ted_chain = SequentialChain(
    chains=[idea_chain, critique_chain, refine_chain],
    input_variables=["idea"],
    output_variables=["evaluation", "critique", "refined"],
    verbose=True
)

__timestamp__ = timestamp
