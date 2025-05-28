from django.apps import AppConfig


class ReviewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews_app'


from django.apps import AppConfig

class UsersAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_app'

    def ready(self):
        import users_app.signals
