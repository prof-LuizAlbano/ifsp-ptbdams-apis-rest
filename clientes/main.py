from fastapi import FastAPI

app = FastAPI()

@app.get("/clientes/{id}")
def get_cliente(id: int):
    return {
        "id": id,
        "nome": "Cliente Exemplo",
        "email": "cliente@email.com"
    }