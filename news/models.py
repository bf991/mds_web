from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify

User = get_user_model()

class Category(models.Model):
    """ Класс категорий
    """
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField("Ссылка",max_length=50, default='')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title



class Tag(models.Model):
    """Класс тегов статей
    """

    title = models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class News(models.Model):
    """ Класс новостей
    """
    upload_to = 'img/news/%s/%s/%s'

    def _get_upload_to(self, filename):
        filename = self.slug + filename[filename.rfind("."):]
        return self.upload_to % (self.category.slug, self.slug, slugify(filename))

    user = models.ForeignKey(
        User,
        verbose_name = "Автор",
        on_delete = models.CASCADE)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null = True)
    title = models.CharField("Заголовок", max_length=100)
    slug = models.SlugField("Ссылка", max_length=50, default='')
    text_min = models.TextField("Анонс", max_length=400)
    image_main = models.ImageField(
        upload_to=_get_upload_to,
        verbose_name="Фото",
        max_length=100,
        null=True
    )
    text = RichTextUploadingField("Текста статьи")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=100)
    keyword = models.CharField("Ключевае слова", max_length=50)



    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title