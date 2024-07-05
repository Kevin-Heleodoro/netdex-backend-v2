from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ContactViewSet,
    # UserListCreateView,
    # UserDetailView,
    # ContactListCreateView,
    # ContactDetailView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"contacts", ContactViewSet)

urlpatterns = [
    path("", include(router.urls)),
    #     path("users/", UserListCreateView.as_view(), name="user-list-create"),
    #     path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    #     path("contacts/", ContactListCreateView.as_view(), name="contact-list-create"),
    #     path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact-detail"),
]
