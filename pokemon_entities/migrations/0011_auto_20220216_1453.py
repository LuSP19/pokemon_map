# Generated by Django 3.1.14 on 2022-02-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20220216_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=None, verbose_name='Появляется'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=None, verbose_name='Исчезает'),
            preserve_default=False,
        ),
    ]
