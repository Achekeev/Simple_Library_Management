# Generated by Django 4.0 on 2021-12-29 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(blank=True, choices=[('Доступна', 'Доступна'), ('На Руках', 'На Руках')], max_length=255),
        ),
        migrations.AlterField(
            model_name='bookstatus',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AlterField(
            model_name='bookstatus',
            name='reader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.client'),
        ),
    ]
