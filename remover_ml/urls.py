from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("remove-bg", views.remove_bg, name="remove_bg")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
