import random

import factory
import names
from django.utils import timezone

from common.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyFunction(names.get_first_name)
    last_name = factory.LazyFunction(names.get_last_name)
    email = factory.LazyAttributeSequence(
        lambda u, n: f"{u.first_name}.{u.last_name}.{n}@yopmail.com"
    )
    date_of_birth = factory.Sequence(
        lambda _: timezone.now() - timezone.timedelta(days=365 * random.randint(20, 50))
    )
