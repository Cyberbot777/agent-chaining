def main():
    print("\nWhich agent would you like to run?\n")
    print("1. Professor Ted (project feedback)")
    print("2. Nightingale (journal reflection)")
    
    choice = input("\nEnter the number of the agent to run: ").strip()

    if choice == "1":
        from chains.professor_ted import ted_chain, __timestamp__, __memory__
        run_professor_ted(ted_chain, __timestamp__, __memory__)
    
    elif choice == "2":
        from chains.journal_reflection import __chain__, __timestamp__
        run_journal_agent(__chain__, __timestamp__)
    
    else:
        print("Invalid choice. Please run again and select a valid number.")

# Professor Ted
def run_professor_ted(chain, timestamp, memory):
    print("\nRunning Professor Ted...")
    # placeholder logic

# Nightingale 
def run_journal_agent(chain, timestamp):
    print("\n[Nightingale] Journal Reflection")
    
    journal_input = input("\nWrite your journal entry below:\n> ")

    result = chain.invoke({"journal_entry": journal_input})

    print(f"\nRun Timestamp: {timestamp}")
    print("\nNightingale’s Wisdom:")
    print("“Thank you for sharing. I’m here with you.”\n")

    print("Summary:")
    print(result["summary"].strip(), "\n")

    print("Insight:")
    print(result["insight"].strip(), "\n")

    print("Reflection Question:")
    print(result["question"].strip())

    print("\nNightingale’s Final Message:")
    print(result["final_message"].strip())



if __name__ == "__main__":
    main()
