from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("products/", include("apps.products.urls")),
]
=======
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
]

>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
