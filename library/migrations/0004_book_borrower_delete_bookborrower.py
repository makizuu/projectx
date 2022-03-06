# Generated by Django 4.0.3 on 2022-03-06 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0003_alter_bookborrower_borrower_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='borrower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BookBorrower',
        ),
    ]