import factory
import names
from faker import Faker
from django.utils import timezone

from common.factories import UserFactory
from task.models import Task


fake = Faker()


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    user = factory.SubFactory(UserFactory)
    title = fake.sentence(10)
    description = fake.text()
