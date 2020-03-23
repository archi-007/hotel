# Generated by Django 3.0.4 on 2020-03-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_remove_book_a_room_date_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_a_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('table', models.IntegerField()),
                ('time', models.TimeField()),
            ],
        ),
    ]