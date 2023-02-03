from django.test import TestCase
import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve

from lettings.models import Letting
from lettings.models import Address



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

# @pytest.mark.django_db
# def test_letting_infos_view():
#     client = Client()
#     # url = reverse('lettings:letting')
#     response = client.get("/lettings/1/", follow_redirects=True)
#     print("réponse2",response)
#     content = response.content.decode()
#     assert '<title>Underground Hygge</title>' in content
#     assert response.status_code == 200
#     assertTemplateUsed(response, "lettings/letting.html")





# url = reverse('chistera:dashboard')
# response = self.client.get(url)
# url = reverse('homepage-url')
# response = client.get(url)


# @pytest.mark.django_db
# def test_letting_infos_view():
#     client = Client()
#     Letting.objects.create(titre="20 milles lieues sous mers",
#                         address="Military Street",)
#     path = reverse('infos', kwargs={'pk': 1})
#     response = client.get(path)
#     content = response.content.decode()
#     expected_content = "<p>20 milles lieues sous mers | Military Street</p>"
#
#     assert content == expected_content
#     assert response.status_code == 200
#     assertTemplateUsed(response, "index.html")



# @pytest.mark.django_db
# def test_letting_infos_view():
#     client = Client()
#     # Letting.objects.create(titre="20 milles lieues sous mers",
#     #                     address="Military Street",)
#     # path = reverse('infos', kwargs={'pk': 1})
#
#     response = client.get("/lettings", follow_redirects=True)
#     # response = client.get(path)
#     content = response.content.decode()
#     expected_content = '<title>Lettings</title>'
#     assert content == expected_content
#     assert response.status_code == 200
#     assertTemplateUsed(response, "letting.html")