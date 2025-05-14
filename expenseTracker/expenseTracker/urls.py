from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('user.urls')), #apenas debug
    path('expense/', include('expenses.urls')),

    #--endpoint dos tokens--

    #obter access e refresh tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #renovar token usando refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
