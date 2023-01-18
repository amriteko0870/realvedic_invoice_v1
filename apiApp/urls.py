from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

import apiApp.views as views
import apiApp.auth.auth_views as auth_views


urlpatterns = [
    
    # path('',auth_views.index,name='index'),
    path('login',auth_views.login,name='login'),
    

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)