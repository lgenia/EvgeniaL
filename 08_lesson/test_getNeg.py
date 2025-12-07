import requests
from urllib.parse import urljoin


def test_get_project_negative_nonexistent_id():
    # Негативный тест получения информации о несуществующем проекте
    
    base_url = 'http://your-api-url.com'
    non_existent_id = 999999
    endpoint = f'/api-v2/projects/{non_existent_id}'
    full_url = urljoin(base_url, endpoint)
    
    response = requests.get(full_url)
    
    assert response.status_code == 404