from django.db import models
from news.models import Tag
from ckeditor_uploader.fields import RichTextUploadingField

class Type(models.Model):
    """ Класс категорий Одежды
    """
    title = models.CharField("тип одежды", max_length=50)

    class Meta:
        verbose_name = "тип одежды"
        verbose_name_plural = "типы одежды"

    def __str__(self):
        return self.title



class Clothe(models.Model):
    """ Класс новостей
    """
    type = models.ForeignKey(
        Type,
        verbose_name="Тип",
        on_delete=models.SET_NULL,
        null = True)
    title = models.CharField("Наименование", max_length=100)
    text_min = models.TextField("Краткое описание", max_length=400)
    text_full = RichTextUploadingField("Полное описание")
    size = models.PositiveSmallIntegerField("Размер")
    price = models.PositiveSmallIntegerField("Цена")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=100)
    keyword = models.CharField("Ключевае слова", max_length=50)
    actuality = models.BooleanField("Наличие", default=True)





    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    def __str__(self):
        return self.title
