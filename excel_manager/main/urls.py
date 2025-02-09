from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('beta/', views.beta, name='beta'),
    path('beta/<str:page_name>/', views.beta_page, name='beta_page'),
    path('download/', views.download_excel, name='download_excel'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('excel/<int:file_id>/delete/', views.delete_excel_file, name='delete_excel_file'),
    path('org/<int:org_id>/dashboard/', views.organization_detail, name='organization_detail'),
    path('org/<int:org_id>/download/', views.organization_download_excel, name='organization_download_excel'),
    path('org/<int:org_id>/delete/', views.delete_organization, name='delete_organization'),
    path('org/<int:org_id>/toggle_excel/', views.toggle_excel_access, name='toggle_excel_access'),
    path('logout/', views.user_logout, name='logout'),
]
