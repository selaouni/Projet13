from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve

from lettings.models import Letting
from lettings.models import Address



@pytest.mark.django_db
def test_index_infos_view():
    client = Client()
    response = client.get("", follow_redirects=True)
    content = response.content.decode()
    assert '<title>Holiday Homes</title>' in content
    # assert content.title == 'Holiday Homes'
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")