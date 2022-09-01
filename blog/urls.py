from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:post_id>/post_detail', views.post_detail, name='post_detail')  # noqa
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
