import factory
from faker import Faker
from web.models import User, Email


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)

    first_name = Faker().first_name()
    last_name = Faker().last_name()
    is_active = True
    is_confirmed = True


class EmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Email
        django_get_or_create = ('code',)
