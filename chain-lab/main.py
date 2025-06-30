from chains.professor_ted import ted_chain, __timestamp__

user_idea = input("What's your coding project idea?\n> ")

result = ted_chain.invoke({"idea": user_idea})

print(f"\nAgent: Professor Ted | Run Timestamp: {__timestamp__}")

print("\n[Part 1] Encouragement:")
print(result["evaluation"].strip())

print("\n[Part 2] Critique:")
print(result["critique"].strip())

print("\n[Part 3] Refined Idea:")
print(result["refined"].strip())
