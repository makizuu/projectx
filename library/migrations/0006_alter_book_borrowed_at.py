# Generated by Django 4.0.3 on 2022-03-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_borrowed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
