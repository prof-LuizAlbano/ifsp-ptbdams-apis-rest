from fastapi import FastAPI
import requests
import os

app = FastAPI()

CLIENTES_URL = os.getenv("CLIENTES_URL")

@app.get("/pedidos/{id}")
def get_pedido(id: int):
    try:
        response = requests.get(f"{CLIENTES_URL}/clientes/{id}", timeout=2)
        cliente = response.json()
    except Exception:
        cliente = {"erro": "Serviço de clientes indisponível"}

    return {
        "id": id,
        "produto": "Notebook",
        "cliente": cliente
    }