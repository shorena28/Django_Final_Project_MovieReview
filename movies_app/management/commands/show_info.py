from django.core.management.base import BaseCommand
from movies_app.models import Movie, Genre, Review, Watchlist
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Displays last 10 movies and object counts for all models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('📽 ბოლო 10 ფილმი:'))
        movies = Movie.objects.order_by('-id')[:10]
        for movie in movies:
            self.stdout.write(f'- {movie.title}')

        self.stdout.write(self.style.SUCCESS('\n📊 ობიექტების რაოდენობა თითოეულ მოდელზე:'))
        self.stdout.write(f'👤 მომხმარებლები: {User.objects.count()}')
        self.stdout.write(f'🎬 ფილმები: {Movie.objects.count()}')
        self.stdout.write(f'🏷 ჟანრები: {Genre.objects.count()}')
        self.stdout.write(f'📝 მიმოხილვები: {Review.objects.count()}')
        self.stdout.write(f'📺 Watchlists: {Watchlist.objects.count()}')