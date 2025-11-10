from django.urls import path
from . import views  # Importa views (donde está CustomLoginView)

app_name = 'auths'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),  # ✅ Usar views.CustomLoginView
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'), 
]