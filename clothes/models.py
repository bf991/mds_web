from django.db import models
from news.models import Tag
from ckeditor_uploader.fields import RichTextUploadingField

class Bijou(models.Model):
    """ Класс бижютерии
    """
    upload_to = 'img/bijou/%s/%d/%s'

    def _get_upload_to(self, filename):
        return self.upload_to % (self.type, self.id, filename)

    TYPE_CHOICES=(
        ('ring', 'Кольцо'),
        ('earring', 'Серьги'),
        ('pendant', 'Кулон'),
        ('bangle', 'Браслет'),
        ('brooch', 'Брошь'),
    )

    type = models.CharField(
        verbose_name="Тип",
        choices=TYPE_CHOICES,
        default='brooch',
        max_length=10)
    title = models.CharField("Наименование", max_length=100)
    slug = models.SlugField("Ссылка", max_length=50, default='')
    text_min = models.TextField("Краткое описание", max_length=400)
    image_main = models.ImageField(
        upload_to = _get_upload_to,
        verbose_name="Фото",
        max_length=100,
        null=True
        )
    text_full = RichTextUploadingField("Полное описание")
    price = models.PositiveSmallIntegerField("Цена")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=100)
    keyword = models.CharField("Ключевае слова", max_length=50)
    actuality = models.BooleanField("Наличие", default=True)

    class Meta:
        verbose_name = "Бижютерия"
        verbose_name_plural = "Бижютерия"

    def __str__(self):
        return self.title

class Clothe(models.Model):
    """ Класс одежды
    """
    upload_to = 'img/clothes/%s/%s/%d/%s'
    def _get_upload_to(self, filename):
        return self.upload_to % (self.male, self.type, self.id, filename)

    AGE_CATEGORY_CHOICES=(
        ('child', 'детская одежда'),
        ('old','одежда для взрослых'),
    )

    TYPE_CHOICES=(
        ('shirt', 'Рубашка'),
        ('pants', 'Брюки'),
        ('dress', 'Патье'),
        ('blouse', 'Блузка'),
        ('costume', 'Костюм'),
        ('jacket', 'Пиджак'),
        ('shoes', 'Туфли'),
        ('tshirt', 'Футболка'),
        ('headdress', 'Головной убор'),
    )

    MALE_CHOICES = (
        ('male', 'Мужская одежда'),
        ('female', 'Женская одежда'),
    )

    type = models.CharField(
        verbose_name="Тип",
        choices=TYPE_CHOICES,
        default='dress',
        max_length=10)
    title = models.CharField("Наименование", max_length=100)
    slug = models.SlugField("Ссылка", max_length=50, default='')
    text_min = models.TextField("Краткое описание", max_length=400)
    image_main = models.ImageField(
        upload_to = _get_upload_to,
        verbose_name="Фото",
        max_length=100,
        null=True
        )
    text_full = RichTextUploadingField("Полное описание")
    age_category = models.CharField(
        verbose_name="Возрастная категория",
        choices=AGE_CATEGORY_CHOICES,
        default='old',
        max_length=10)
    male = models.CharField(
        verbose_name="Пол",
        choices=MALE_CHOICES,
        default='female',
        max_length=10)
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
