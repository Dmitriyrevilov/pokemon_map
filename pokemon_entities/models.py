from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name="Покемоны",
        related_name="entities",
    )
    lat = models.FloatField(null=True, verbose_name="Широта")
    lon = models.FloatField(null=True, verbose_name="Широта")
    appeared_at = models.DateTimeField(
        default=timezone.now, verbose_name="Время появления"
    )
    disappeared_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Время исчезновения"
    )
    level = models.IntegerField(blank=True, null=True, verbose_name="Уровень")
    healh = models.IntegerField(blank=True, null=True, verbose_name="Здоровье")
    strenght = models.IntegerField(blank=True, null=True, verbose_name="Атака")
    defence = models.IntegerField(blank=True, null=True, verbose_name="Защита")
    stamina = models.IntegerField(blank=True, null=True, verbose_name="Выносливость")
