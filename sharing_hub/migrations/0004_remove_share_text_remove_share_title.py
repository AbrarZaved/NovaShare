# Generated by Django 5.1.7 on 2025-03-16 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharing_hub', '0003_remove_share_private_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='text',
        ),
        migrations.RemoveField(
            model_name='share',
            name='title',
        ),
    ]
