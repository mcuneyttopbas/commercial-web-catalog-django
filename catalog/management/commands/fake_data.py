import os
import random
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE","bookstore.settings")

import django
from django.contrib.auth.models import User 
django.setup()

from faker import Faker


def set_user():
    fake = Faker(["en_US"])
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name.lower()}_{last_name.lower()}"
    email = f"{username}@{fake.domain_name()}"
    print(first_name, last_name, email)

    user_check = User.objects.filter(username=username)

    while user_check.exists():
        username = username + str(random.randrange(1,99))
        user_check = User.objects.filter(username=username)

    user = User(
        username = username,
        first_name = first_name,
        last_name = last_name,
        email = email,
        is_staff = fake.boolean(chance_of_getting_true=50)
    )

    user.set_password("testing123")
    user.save()

from pprint import pprint
from books.api.serializers import BookSerializer

def add_book(subject):
    fake = Faker(["en_US"])
    url = "http://openlibrary.org/search.json"
    payload = {"q":subject}                         # Boşlukarı "+" ifadesi ile doldurmakta.
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print("Hatalı istek yapıldı", response.status_code)
        return 

    jsn = response.json()
    books = jsn.get("docs")
    for book in books:
        data = dict(
            name = book.get("title"),
            author = book.get("author_name")[0],
            description = book.get("text"),
            publish_date = fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None)
        )
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("1 kitap yüklendi")
        else:
            print("yükelmede sıkıntı")
            continue