import pytest

@pytest.mark.django_db
def test_user_login(client, django_user_model):
    user = django_user_model.objects.create_user(
        email='test2@example.com',
        password='testpass456',
        first_name='Test',
        last_name='User'
    )
    login = client.login(email='test2@example.com', password='testpass456')  

    login = client.login(username='test2@example.com', password='testpass456') 
    assert login is True