# Generated by Django 3.0.4 on 2020-03-24 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0005_book_a_room_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_a_room',
            name='purpose',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='book_a_room',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book_a_table',
            name='purpose',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='book_a_table',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
