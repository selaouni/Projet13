import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


@pytest.mark.django_db
def test_letting_index_view():
    client = Client()
    url = reverse('lettings:index')
    # "/lettings/"
    response = client.get(url, follow_redirects=True)
    print("réponse", response)
    content = response.content.decode()
    assert '<title>Lettings</title>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
