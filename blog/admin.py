from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'autor', 'titulo', 'subtitulo', 'data_publicacao'
    ]

    list_editable = [
        'titulo', 'subtitulo', 'data_publicacao'
    ]
