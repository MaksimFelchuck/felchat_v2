from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Публикации на стене пользователя."""

    pub_date = models.DateField("Дата публикации", auto_now_add=True)
    headline = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст публикации")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user.get_full_name()}{self.headline}"
