import requests
import pytest

def test_api_create_post():
    # Cargamos datos
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Mi Post de Prueba QA",
        "body": "Este es el contenido de mi post.",
        "userId": 101
    }
    
    # Hacemos el POST
    response = requests.post(url, json=payload)
    
    # Validamos la respuesta
    print(f"\nStatus Code: {response.status_code}")
    assert response.status_code == 201
    
    response_body = response.json()
    print(f"Título: {response_body['title']}")
    
    assert response_body["title"] == "Mi Post de Prueba QA"