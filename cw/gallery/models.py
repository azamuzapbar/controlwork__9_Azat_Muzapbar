from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='photos')
    description = models.CharField(verbose_name='Подпись', null=False, blank=False, max_length=200)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='photos', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    def __str__(self):
        return f'{self.author}'


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', related_name='comments', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, verbose_name='Фото', related_name='comments', null=False,
                              blank=False,
                              on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Комментарий', null=False, blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorite_photos', verbose_name='Избранное', null=False,
                             on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, related_name='favorite_users', verbose_name='Избранное', null=False,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(verbose_name='удалено', default=False, null=False)
