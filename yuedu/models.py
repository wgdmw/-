from django.db import models
from tinymce.models import HTMLField
from db.base_model import BaseModel


class ReadType(BaseModel):

    type = models.CharField(max_length=10,verbose_name='文章类型')
    index = models.SmallIntegerField(default=0,verbose_name='展示顺序')

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'read_type'
        verbose_name = '类型'
        verbose_name_plural = verbose_name

#
# class ReadTypeClass(BaseModel):
#
#     type_class = models.CharField(max_length=10,verbose_name='文章子类型')
#     read_type = models.ForeignKey('ReadType',verbose_name='文章分类')
#
#
#     def __str__(self):
#         return self.type_class
#
#     class Meta:
#         db_table = 'read_type_class'
#         verbose_name = '子分类'
#         verbose_name_plural = verbose_name
#
class ReadTag(BaseModel):
    read_tag = models.CharField(max_length=12,verbose_name='文章标签')

    # article_tag = models.ManyToManyField('Article',verbose_name='文章标签')

    def __str__(self):
        return self.read_tag

    class Meta:
        db_table = 'read_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Article(BaseModel):


    detail = HTMLField(blank=True,verbose_name='文章')
    title = models.CharField(max_length=25,verbose_name='文章标题')
    readcount = models.IntegerField(default=0,verbose_name='阅读量')
    read_type = models.ForeignKey('ReadType', verbose_name='文章分类')
    # read_type_class = models.ForeignKey('ReadTypeClass',verbose_name='所属分类')
    read_tag_info = models.ManyToManyField('ReadTag',verbose_name='文章的标签')


    def __str__(self):
        return self.title


    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class ReadComment(BaseModel):

    comment = models.CharField(max_length=456, blank=True, verbose_name='评论')
    article = models.ForeignKey('Article',verbose_name='所属文章')

    def __str__(self):
        return self.article.title

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name