from django.urls import path
from .views import UserListCreateView, ContactListCreateView

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("contacts/", ContactListCreateView.as_view(), name="contact-list-create"),
]
