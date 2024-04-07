# Generated by Django 4.2.2 on 2024-04-07 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelhrapp', '0012_delete_chatdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatdata',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=255)),
                ('query', models.TextField()),
                ('shortdesc', models.TextField()),
            ],
        ),
    ]