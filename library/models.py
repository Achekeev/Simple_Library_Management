from datetime import datetime, timedelta

from django.db import models

BOOK_STATUS_AVAILABLE = "Доступна"
BOOK_STATUS_TAKEN = "На Руках"

# Tuples are better, cuz it never changes in runtime
BOOK_STATUS_CHOICES = (
    (BOOK_STATUS_AVAILABLE, BOOK_STATUS_AVAILABLE),
    (BOOK_STATUS_TAKEN, BOOK_STATUS_TAKEN),
)


class Book(models.Model):
    author = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    isbn = models.PositiveIntegerField(verbose_name='Штрих Код')
    book_status = models.CharField(
        choices=BOOK_STATUS_CHOICES,
        max_length=255,
        blank=True,
        default=BOOK_STATUS_AVAILABLE
    )

    def is_available(self):
        return self.book_status == BOOK_STATUS_AVAILABLE

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


# Should have different name
class BookStatus(models.Model):
    reader = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        related_name="book_grab"
    )
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

    def __str__(self):
        return f'{self.reader}  [{self.book.book_name}]'
