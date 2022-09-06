from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = RichTextField(null=True, blank=True)
    conteudo = RichTextUploadingField()
    imagem_capa = models.ImageField(
        upload_to='static/blog/img/', null=True, blank=True)
    data_publicacao = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.autor
