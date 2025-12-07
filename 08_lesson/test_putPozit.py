import requests
from urllib.parse import urljoin


def test_update_project_positive(project_id):
    # Позитивный тест обновления проекта
    
    base_url = 'http://your-api-url.com'
    endpoint = f'/api-v2/projects/{project_id}'
    full_url = urljoin(base_url, endpoint)
    
    updated_data = {
        "name": "Updated Test Project",
        "description": "This project has been updated via automation tests"
    }
    
    response = requests.put(full_url, json=updated_data)
    
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Test Project"
