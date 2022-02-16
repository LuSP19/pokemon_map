from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    title_en = models.CharField(
        max_length=50,
        verbose_name='Название (англ.)',
        blank=True
    )
    title_jp = models.CharField(
        max_length=50,
        verbose_name='Название (яп.)',
        blank=True
    )
    evolved_from = models.ForeignKey(
        'self',
        verbose_name='Эволюционировал из',
        related_name='next_evolutions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        related_name='entities',
        on_delete=models.CASCADE
    )
    lat = models.FloatField(verbose_name='Широта', null=True, blank=True)
    lon = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    appeared_at = models.DateTimeField(verbose_name='Появляется')
    disappeared_at = models.DateTimeField(verbose_name='Исчезает')
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(
        verbose_name='Здоровье',
        null=True,
        blank=True
    )
    strength = models.IntegerField(verbose_name='Сила', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(
        verbose_name='Выносливость',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.pokemon.title} ({self.lat}, {self.lon})'
