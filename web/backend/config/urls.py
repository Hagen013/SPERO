from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from demo.views import IndexPageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', IndexPageView.as_view())
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
