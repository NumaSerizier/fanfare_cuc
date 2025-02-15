# Generated by Django 2.0.5 on 2018-05-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180509_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date',), 'verbose_name': 'Evenement', 'verbose_name_plural': 'Evenements'},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['title'], 'verbose_name': 'Morceau', 'verbose_name_plural': 'Morceaux'},
        ),
        migrations.AddField(
            model_name='event',
            name='displayed_date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
