from django.db import models


class Philosopher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    life = models.IntegerField(verbose_name="Даты жизни")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    period = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Период")

    def __str__(self):
        return self.title


class Period(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Период")

    def __str__(self):
        return self.name
