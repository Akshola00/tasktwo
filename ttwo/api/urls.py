from . import views
from django.urls import path

urlpatterns = [
    # path("test", views.test, name='test'),  
    path('users/<str:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('organisations', views.ListUserOrganizationsView.as_view(), name='user-organizations'),
    path('organisations/<uuid:org_id>', views.OrganizationDetailView.as_view(), name='organization-detail'),
    path('organisations/create', views.CreateOrganizationView.as_view(), name='create-organization'),


] 