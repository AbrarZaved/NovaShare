# Generated by Django 5.1.7 on 2025-03-15 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharing_hub', '0002_alter_share_private_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='private_key',
        ),
    ]
