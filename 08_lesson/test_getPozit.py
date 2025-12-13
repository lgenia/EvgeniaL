import requests
from urllib.parse import urljoin


def test_get_project_positive(project_id):
    # Позитивный тест получения информации о проекте
    
    base_url = 'http://ru.yougile.com'
    endpoint = f'/api-v2/projects/{project_id}'
    full_url = urljoin(base_url, endpoint)
    
    response = requests.get(full_url)
    
    assert response.status_code == 200
    assert "name" in response.json()