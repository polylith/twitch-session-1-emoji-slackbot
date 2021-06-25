from django.urls import path

from employee import views

urlpatterns = [
    path("internal_api/set_employee_emoji/", views.set_employee_emoji),
]