from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
 
urlpatterns = [
    path('bbs/', include('bbs.urls')),
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # accounts/以下のルーティングはaccounts.urls.pyに任せる
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/bbs/')),
]