from django.contrib import admin
from yuedu.models import Article,ReadType,ReadTag,ReadComment
# Register your models here.




admin.site.register(Article)
admin.site.register(ReadTag)
admin.site.register(ReadComment)
admin.site.register(ReadType)