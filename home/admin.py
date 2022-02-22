from django.contrib import admin
from .models import vote,vote_likes
# Register your models here.
admin.site.register(vote)
admin.site.register(vote_likes)