from django.urls import reverse, resolve


def test_homepage_url(client):
    url = reverse('homepage')
    response = client.get(url)
    assert resolve(url).view_name == 'homepage'
    assert response.status_code == 200

# def test_homepage_url(self):
#     path = reverse('homepage', kwargs={'pk': 1})
#     assert resolve(path).view_name == "content"
