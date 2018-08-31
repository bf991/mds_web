from django.db import models
from news.models import Tag, Category
from ckeditor_uploader.fields import RichTextUploadingField


class Masterclass(models.Model):
    """ Класс новостей
    """
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null = True)
    title = models.CharField("Название МК", max_length=100)
    text_min = models.TextField("Краткое описание", max_length=400)
    text_full = RichTextUploadingField("Полное описание")
    duration = models.DurationField("Длительность", default='00:00:00')
    age_category = models.PositiveSmallIntegerField("Возрастная категория")
    price = models.PositiveSmallIntegerField("Цена МК")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=100)
    keyword = models.CharField("Ключевае слова", max_length=50)
    actuality = models.BooleanField("Актуальность МК", default=True)


    class Meta:
        verbose_name = "Мастер-класс"
        verbose_name_plural = "Мастер-классы"

    def __str__(self):
        return self.title
