from enum import unique

import factory
from factory.django import ImageField
from computer_hardware_store import models
from random import randint

class BuilderFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    surname = factory.Faker('last_name')

    class Meta:
        model = models.Builder

class ComputerFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    build_date = factory.Faker('date')
    description = factory.Faker('text')
    id_pc = factory.Sequence(lambda n: randint(100,200))
    image = ImageField()
    builder = factory.SubFactory(BuilderFactory)

    class Meta:
        model = models.Computer