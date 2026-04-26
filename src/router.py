from llm import ask_llm

def decide_action(query):
    print("inside decide action block")
    prompt = f"""
You are an SRE assistant.

Decide what is needed:
- "direct" → general knowledge
- "rag" → runbook/process
- "metrics" → system metrics

Query: {query}

Return ONLY one word.
"""

    decision = ask_llm(prompt, 5).lower()
    print("decision:",decision)
    if "rag" in decision:
        return "rag"
    elif "metrics" in decision:
        return "metrics"
    else:
        return "direct"