from django.db import models
from datetime import datetime, timedelta

BOOK_STATUS = [
    ('Доступна', 'Доступна'),
    ('На Руках', 'На Руках'),
]


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_status = models.CharField(choices=BOOK_STATUS, max_length=255, blank=True)
    isbn = models.PositiveIntegerField(verbose_name='Штрих Код')

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} [{self.phone_number}]'

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


def expiry():
    return datetime.today() + timedelta(days=10)


class BookStatus(models.Model):
    reader = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

    def __str__(self):
        return f'{self.reader}  [{self.book.book_name}]'
