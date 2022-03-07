from django.urls import include, path, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

app_name = "contact"

router = routers.DefaultRouter()
#router.register(r"contact", views.ContactViewSet)

urlpatterns = [
    path("", views.contact_view, name="contact"),
    path("api/list/", views.ContactList.as_view(), name="list"),
    path("api/post/", views.ContactCreate.as_view(), name="create"),
    path("api/", include(router.urls)),
]