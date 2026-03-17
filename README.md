# IFSP-PTB - PTBDAMS: APIs REST - Tutorial

Autor: Luiz Albano

Esta tutorial exemplifica a implementação de dois microsserviços demonstrando a comunicação direta (síncrona) entre eles. É parte da aula da disciplina "Desenvolvimento de APIs e Microsserviços" do curso TADS - Campus Pirituba.


**💻 Cenário proposto:**

Microsserviço 1 – Pedidos
* Endpoint: /pedidos/{id}
* Deve consultar dados do cliente

Microsserviço 2 – Clientes
* Endpoint: /clientes/{id}
* Retorna dados mockados

---

**✔ Tecnologias sugeridas:**
* FastAPI (Python)
* REST API
* Docker

---

#### Subindo os containers

```
docker-compose up --build
```

**O que acontece aqui?**

* O Docker vai buildar as imagens dos dois serviços
* Criar containers separados
* Criar uma rede interna
* Permitir comunicação entre serviços pelo nome (clientes)

---

#### Testando os serviços

**Serviço de clientes**
Acesse no navegador ou cliente API:
```
http://localhost:8001/clientes/1
```

**Serviço de pedidos**
Acesse no navegador ou cliente API:
```
http://localhost:8000/pedidos/1
```

Resultado esperado:
```
{
  "id": 1,
  "produto": "Notebook",
  "cliente": {
    "id": 1,
    "nome": "Cliente Exemplo",
    "email": "cliente@email.com"
  }
}
```