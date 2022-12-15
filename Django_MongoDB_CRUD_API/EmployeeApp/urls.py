from django.urls import path
from EmployeeApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('department',views.departmentApi),
    path('department/<id>',views.departmentApi),
    path('employee',views.employeeApi),
    path('employee/<id>',views.employeeApi),
    path('employee/savefile',views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
