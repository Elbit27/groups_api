# Generated by Django 4.2.7 on 2023-12-04 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_song_group_name_musician_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='feat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feat', to='main.musician'),
        ),
    ]
