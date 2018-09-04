from django.db import models
from news.models import Tag, Category
from ckeditor_uploader.fields import RichTextUploadingField



class Masterclass(models.Model):
    """ class masterclass
    """
    upload_to = 'img/MK/%s/%s/%s/%d/%s'

    def _get_upload_to(self, filename):

        filename = self.slug + filename[filename.rfind(".")+1:]
        return self.upload_to % (self.form, self.age_category, self.category_mk, self.id, filename)

    AGE_CATEGORY_CHOICES=(
        ('child', 'для детей'),
        ('old','для взрослых'),
        ('child&old','для всех'),
    )

    CATEGORY_MK_CHOICES=(
        ('hud', 'Художественный'),
        ('candy', 'Кондитерский'),
        ('cook', 'Кулинарный'),
        ('handmade', 'Творческий'),

    )

    FORM_MK_CHOICES = (
        ('ind', 'Индивидуальный'),
        ('group', 'Групповой'),
    )

#FIELDS
    category_mk = models.CharField(
        verbose_name="Категория",
        choices=CATEGORY_MK_CHOICES,
        max_length=10,
        default='hud'
    )
    title = models.CharField("Название МК", max_length=100)
    slug = models.SlugField("Ссылка",max_length=50, default='')
    duration = models.DurationField("Длительность", default='00:00:00')
    age_category = models.CharField(
        verbose_name="Возрастная категория",
        choices=AGE_CATEGORY_CHOICES,
        max_length=10,
        default='child&old'
    )
    form = models.CharField(
        verbose_name="Форма МК",
        choices=FORM_MK_CHOICES,
        max_length=10,
        default='group'
    )
    price = models.PositiveSmallIntegerField("Цена МК")

    text_min = models.TextField("Краткое описание", max_length=400)
    image_main = models.ImageField(
        upload_to=_get_upload_to,
        verbose_name="Фото",
        max_length=100,
        null=True
    )
    text_full = RichTextUploadingField("Полное описание")
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
