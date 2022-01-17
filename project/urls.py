from django.contrib import admin
from django.urls import include, path

import mailinglist.urls
import user.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include(user.urls, namespace="user")),
    path("mailinglist/", include(mailinglist.urls, namespace="mailinglist")),
]
