from llama_cpp import Llama

llm = Llama(
    model_path="../models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
    verbose=False 
)

def ask_llm(prompt, max_tokens=200):
    output = llm(prompt, max_tokens=max_tokens, temperature=0.2, stop=["</s>", "[/INST]"])
    return output["choices"][0]["text"].strip()