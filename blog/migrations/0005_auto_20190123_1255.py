# Generated by Django 2.1.5 on 2019-01-23 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
