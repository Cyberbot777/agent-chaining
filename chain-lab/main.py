from chains.professor_ted import ted_chain, __timestamp__, __memory__
from langchain_core.messages import HumanMessage, AIMessage

# Step 1 – Get user input
user_idea = input("What's your coding project idea?\n> ")

# Step 2 – Load in-memory chat history (just for current run)
chat_history = __memory__.load_memory_variables({})["chat_history"]

# Step 3 – Run the chain
result = ted_chain.invoke({
    "idea": user_idea,
    "evaluation": "",
    "critique": "",
    "chat_history": chat_history,
})

# Step 4 – Save this turn to memory (temporary/in-memory only)
__memory__.chat_memory.add_user_message(user_idea)
__memory__.chat_memory.add_ai_message(result["refined"])

# Step 5 – Display results
print(f"\nAgent: Professor Ted | Run Timestamp: {__timestamp__}")

print("\n[Part 1] Encouragement:")
print(result["evaluation"].strip())

print("\n[Part 2] Critique:")
print(result["critique"].strip())

print("\n[Part 3] Refined Idea:")
print(result["refined"].strip())

# Step 6 – Show current in-memory history
print("\nChat History stored in memory (this session only):")
for msg in __memory__.chat_memory.messages:
    print(f"{msg.type.capitalize()}: {msg.content}")
