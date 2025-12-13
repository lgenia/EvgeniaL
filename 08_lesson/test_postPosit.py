import requests
import json
from urllib.parse import urljoin


def test_create_project_positive():
    # Позитивный тест создания проекта
    
    base_url = 'http://ru.yougile.com'
    endpoint = '/api-v2/projects/'
    full_url = urljoin(base_url, endpoint)
    
    data = {
        "name": "Test Project",
        "description": "This is a test project for automation testing"
    }
    
    response = requests.post(full_url, json=data)
    
    assert response.status_code == 201
    assert "id" in response.json()
