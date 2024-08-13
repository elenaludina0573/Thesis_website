from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия пользователя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    phone = models.CharField(max_length=35, verbose_name='телефонный номер', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)

    verification_code = models.CharField(max_length=100, verbose_name='код', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} - {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            ('can_add_client', 'Может добавлять клиента'),
            ('can_change_client', 'Может изменять клиента'),
            ('can_view_client', 'Может просматривать клиента'),
            ('can_delete_client', 'Может удалять клиента'),
        ]
