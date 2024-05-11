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
    name = models.CharField('name', max_length=255)

    class Meta:
        db_table = 'Article'


class Banner(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    button = models.TextField(null=True, blank=True)
    button_link = models.TextField(null=True, blank=True)

    background_picture = models.ForeignKey("files.File", on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name="back_pic_banners")
    focus_picture = models.ForeignKey("files.File", on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name="focus_pic_banners")

    class Meta:
        db_table = 'Banner'
