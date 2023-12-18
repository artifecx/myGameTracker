# Generated by Django 5.0 on 2023-12-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collection',
            name='type',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Owned'), (2, 'Playing'), (3, 'Completed')], default=0),
        ),
    ]