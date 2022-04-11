from django.urls import path

from . import views

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.index_view),
    path('', views.song_list_view),
    # path('audio/', views.Audio_store)
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)