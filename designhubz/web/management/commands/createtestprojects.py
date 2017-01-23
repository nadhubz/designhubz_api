from django.conf import settings
from django.core.management.base import BaseCommand
from web.models import User
from project.models import Project


class Command(BaseCommand):
    """
    Creates 3 projects for test client
    and 3 projects for test designer.
    """
    def create_clients_projects(self):
        client = User.objects.get(email=settings.TEST_CLIENT_EMAIL)
        names = [
            'Client project1', 'Client project2', 'Client project3']
        for name in names:
            Project.objects.create_project(client.id, name)

    def create_designers_projects(self):
        client = User.objects.get(email=settings.TEST_DESIGNER_EMAIL)
        names = [
            'Designer project1', 'Designer project2', 'Designer project3']
        for name in names:
            Project.objects.create_project(client.id, name)

    def handle(self, *args, **options):
        self.create_clients_projects()
        self.create_designers_projects()
        print('Test projects have been created.')
