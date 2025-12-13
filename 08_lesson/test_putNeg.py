import requests
from urllib.parse import urljoin


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
