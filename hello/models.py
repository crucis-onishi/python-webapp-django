from django.db import models
 
# Articleクラスを定義
class Article(models.Model):
    # contentカラムを定義
    content = models.CharField(max_length=140)

    def __str__(self):
        return self.content