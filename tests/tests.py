import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_infos_view():
    client = Client()
    response = client.get("", follow_redirects=True)
    content = response.content.decode()
    assert '<title>Holiday Homes</title>' in content
    # assert content.title == 'Holiday Homes'
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
