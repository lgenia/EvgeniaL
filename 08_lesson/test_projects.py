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


def test_create_project_negative_missing_name():
    # Негативный тест создания проекта без имени
    
    base_url = 'http://ru.yougile.com'
    endpoint = '/api-v2/projects/'
    full_url = urljoin(base_url, endpoint)
    
    data = {
        "description": "Project without name"
    }
    
    response = requests.post(full_url, json=data)
    
    assert response.status_code == 400
    assert "errors" in response.json()


def test_update_project_positive(project_id):
    # Позитивный тест обновления проекта
    
    base_url = 'http://ru.yougile.com'
    endpoint = f'/api-v2/projects/{project_id}'
    full_url = urljoin(base_url, endpoint)
    
    updated_data = {
        "name": "Updated Test Project",
        "description": "This project has been updated via automation tests"
    }
    
    response = requests.put(full_url, json=updated_data)
    
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Test Project"


def test_update_project_negative_nonexistent_id():
    # Негативный тест обновления несуществующего проекта
    
    base_url = 'http://ru.yougile.com'
    non_existent_id = 999999
    endpoint = f'/api-v2/projects/{non_existent_id}'
    full_url = urljoin(base_url, endpoint)
    
    updated_data = {
        "name": "Nonexistent Project Update Attempt"
    }
    
    response = requests.put(full_url, json=updated_data)
    
    assert response.status_code == 404


def test_get_project_positive(project_id):
    # Позитивный тест получения информации о проекте
    
    base_url = 'http://ru.yougile.com'
    endpoint = f'/api-v2/projects/{project_id}'
    full_url = urljoin(base_url, endpoint)
    
    response = requests.get(full_url)
    
    assert response.status_code == 200
    assert "name" in response.json()


def test_get_project_negative_nonexistent_id():
    # Негативный тест получения информации о несуществующем проекте
    
    base_url = 'http://ru.yougile.com'
    non_existent_id = 999999
    endpoint = f'/api-v2/projects/{non_existent_id}'
    full_url = urljoin(base_url, endpoint)
    
    response = requests.get(full_url)
    
    assert response.status_code == 404