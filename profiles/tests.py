import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve

from lettings.models import Letting
from lettings.models import Address



@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    url = reverse('profiles:index')
    response = client.get(url, follow_redirects=True)
    print("réponse", response)
    content = response.content.decode()
    assert '<title>Profiles</title>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")

@pytest.mark.django_db
def test_profile_infos_view():
    client = Client()
    # url = reverse('lettings:letting')
    response = client.get("/profiles/4meRomance/", follow_redirects=True)
    print("réponse2",response)
    content = response.content.decode()
    assert '<title>4meRomance</title>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
