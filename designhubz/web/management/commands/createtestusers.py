from django.conf import settings
from django.core.management.base import BaseCommand
from web.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_user(
            settings.TEST_CLIENT_EMAIL,
            settings.TEST_CLIENT_PASSWORD,
            User.CLIENT)
        User.objects.create_user(
            settings.TEST_DESIGNER_EMAIL,
            settings.TEST_DESIGNER_PASSWORD,
            User.DESIGNER)
        print('Test users have been created.')
