import pytest
from movies_app.models import Movie, Genre
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_movie():
    user = User.objects.create_user(
        email='creator@example.com',
        password='pass123',
        first_name='Movie',
        last_name='Creator'
    )

    genre = Genre.objects.create(name='Action')
    movie = Movie.objects.create(
        title='My Test Movie',
        description='Test description',
        release_date='2024-01-01',
        created_by=user
    )
    movie.genres.add(genre)

    assert movie.title == 'My Test Movie'