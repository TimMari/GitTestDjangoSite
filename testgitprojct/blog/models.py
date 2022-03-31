from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserBlog(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=13, db_index=True)
    content = models.TextField('Содержание', blank=True)
    photo = models.ImageField('Фото', upload_to='blog/photos/%Y/%m/%d', blank=True)
    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now_add=True)
    published = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
