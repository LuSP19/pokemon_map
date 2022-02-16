from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50, blank=True)
    title_jp = models.CharField(max_length=50, blank=True)
    ancestor = models.ForeignKey(
        'self',
        related_name='next_evolutions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        related_name='entities',
        on_delete=models.CASCADE
    )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
