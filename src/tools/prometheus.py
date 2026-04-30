import requests

PROM_URL = "http://localhost:9090/api/v1/query"

def get_cpu():
    print("Inside get cpu block")
    query = '100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'
    res = requests.get(PROM_URL, params={"query": query})
    print("res :", res)
    return res.json()