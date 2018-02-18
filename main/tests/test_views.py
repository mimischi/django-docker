import pytest

from main.models import Visits


@pytest.mark.django_db
def test_main_view(client):
    """Test functionality of the main app."""

    # Initially we do not expect any object to exist.
    with pytest.raises(Visits.DoesNotExist):
        Visits.objects.get(pk=1)

    # The first request should create an object and set the counter to 1.
    response = client.get('/')
    assert response.status_code == 200
    assert 'count' in response.context
    assert response.context['count'] == 1
    assert response.templates[0].name == 'main/home.html'

    # We should now be able to retrieve the object from the database.
    count = Visits.objects.get(pk=1)
    assert isinstance(count, Visits)
    assert count.count == 1
