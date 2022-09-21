import csv
import requests

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            date_list = phone['release_date'].split('-')
            print(
                f"{phone['name']} | {date(int(date_list[0]), int(date_list[1]), int(date_list[2]))} | {phone['image']}")

            Phone(
                name=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=date(int(date_list[0]), int(date_list[1]), int(date_list[2])),
                lte_exists=(phone['lte_exists'] == 'True'),
                slug=slugify(phone['name']),
            ).save()
