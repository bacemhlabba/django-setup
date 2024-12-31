# urls.py

from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views



from .users.views import CompanyViewSet, DirectorViewSet, HistoricalChangeViewSet

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    


     # Manually defining CRUD actions for the CompanyViewSet
    path('api/v1/companies/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='company-list-create'),
    path('api/v1/companies/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='company-detail'),
    
    # Manually defining CRUD actions for the DirectorViewSet
    path('api/v1/directors/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director-list-create'),
    path('api/v1/directors/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='director-detail'),
    
    # Manually defining CRUD actions for the HistoricalChangeViewSet
    path('api/v1/historical-changes/', HistoricalChangeViewSet.as_view({'get': 'list', 'post': 'create'}), name='historicalchange-list-create'),
    path('api/v1/historical-changes/<int:pk>/', HistoricalChangeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='historicalchange-detail'),


    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
