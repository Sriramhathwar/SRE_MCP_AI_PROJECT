import requests

PROM_URL = "http://localhost:9090/api/v1/query"

def get_cpu():
    query = '100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'
    res = requests.get(PROM_URL, params={"query": query})
    return res.json()