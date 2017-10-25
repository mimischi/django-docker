import pytest

from main.models import Visits


@pytest.mark.django_db
def test_database():
    c = Visits.objects.create(count=1)
    assert isinstance(c, Visits)
