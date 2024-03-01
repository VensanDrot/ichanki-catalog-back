from django.db import models

from config.models import BaseModel


class News(BaseModel):
    is_draft = models.BooleanField('is draft', default=False)
    title = models.CharField('title', max_length=155)
    description = models.TextField('description', null=True, blank=True)
    content = models.TextField('content', null=True, blank=True)

    # photos ForeignKey inside File model

    class Meta:
        db_table = 'News'


class Article(BaseModel):
    class Meta:
        db_table = 'Article'
