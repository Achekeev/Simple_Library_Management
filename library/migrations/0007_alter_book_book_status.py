# Generated by Django 4.0 on 2021-12-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_bookstatus_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(blank=True, choices=[('Доступна', 'Доступна'), ('На Руках', 'На Руках')], default='Доступна', max_length=255),
        ),
    ]
