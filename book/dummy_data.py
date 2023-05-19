from faker import Faker
import random

fake = Faker()

DUMMY_BOOKS = []

for _ in range(20):
    book = {
        'title': fake.catch_phrase(),
        'author': fake.name(),
        'price': round(random.uniform(5.0, 50.0), 2),
    }
    DUMMY_BOOKS.append(book)
