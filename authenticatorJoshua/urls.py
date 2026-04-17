# authapp/urls.py

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # UI
    path('', views.home),

    # API
    path('save/', views.save_qr),
    path('accounts/', views.get_accounts),   # ✅ REQUIRED
    path('delete/<int:id>/', views.delete_account),
]