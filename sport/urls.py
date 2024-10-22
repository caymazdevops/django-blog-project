from django.contrib import admin
from django.urls import path, include
from spor.views import spor_detail, spor_list, team_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', spor_list, name='spor_list'),
    path('teams', team_list, name='team_list'),
    path('spor/<int:spor_id>/', spor_detail, name='spor_detail'),  # Detay sayfası
]

# Medya dosyalarına erişim sağlamak için bu kısmı ekleyin
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
