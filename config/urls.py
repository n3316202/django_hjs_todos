from django.contrib import admin
from django.urls import include, path

from config import settings

# http://127.0.0.1:8000/admin
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),  # dev_1
]

# dev_3
# dev_10 배포를 위해 삭제
# if settings.DEBUG:
#    urlpatterns += [
#        path("__debug__/", include("debug_toolbar.urls")),
#    ]
