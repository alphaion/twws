from django.contrib import admin
from .models import BookModel,BookOfMonth,Review
# Register your models here.
admin.site.register(BookModel)
admin.site.register(BookOfMonth)
admin.site.register(Review)