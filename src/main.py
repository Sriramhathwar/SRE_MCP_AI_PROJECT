from router import decide_action
from llm import ask_llm
from rag.embed import build_index
from rag.retrieve import retrieve
from tools.prometheus import get_cpu

# Load runbooks
with open("rag/data/runbooks.txt") as f:
    texts = f.read().split("\n\n")

index, texts = build_index(texts)

def handle_query(query):
    action = decide_action(query)

    if action == "direct":
        return ask_llm(query)

    elif action == "rag":
        context = retrieve(query, index, texts)
        return ask_llm(f"Context:\n{context}\n\nQ:{query}")

    elif action == "metrics":
        data = get_cpu()
        return ask_llm(f"Metrics:\n{data}\n\nQ:{query}")

if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        if q == "exit":
            break
        print(handle_query(q))