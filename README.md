                         ┌──────────────────────┐
                         │        User          │
                         │  (Web UI - Browser) │
                         └─────────┬───────────┘
                                   │ HTTP (POST /ask)
                                   ▼
                      ┌──────────────────────────┐
                      │     Flask Backend        │
                      │        app.py            │
                      └─────────┬────────────────┘
                                │
                                ▼
                      ┌──────────────────────────┐
                      │   Query Handler Layer    │
                      │     (main.py)            │
                      └─────────┬────────────────┘
                                │
                                ▼
                      ┌──────────────────────────┐
                      │  MCP Decision Layer      │
                      │     (router.py)          │
                      │  LLM decides action:     │
                      │  direct / rag / metrics  │
                      └───────┬───────┬─────────┘
                              │       │
             ┌────────────────┘       └────────────────┐
             ▼                                         ▼
┌──────────────────────────┐              ┌──────────────────────────┐
│     RAG Engine (FAISS)   │              │   Prometheus Tool API     │
│                          │              │                          │
│ embed.py                 │              │ prometheus.py            │
│ retrieve.py              │              │                          │
│                          │              │ Query → PromQL           │
│ Runbooks / Docs          │              │ Fetch real-time metrics  │
└──────────┬───────────────┘              └──────────┬───────────────┘
           │                                          │
           ▼                                          ▼
     Retrieved Context                        Metrics Data (JSON)
           │                                          │
           └──────────────┬───────────────────────────┘
                          ▼
                ┌──────────────────────┐
                │      LLM Layer       │
                │     (Mistral 7B)     │
                │ llama-cpp-python     │
                └─────────┬────────────┘
                          ▼
                  Generated Answer
                          ▼
                ┌──────────────────────┐
                │   Flask Response     │
                └─────────┬────────────┘
                          ▼
                    Web UI Output