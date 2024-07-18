from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import getNotes, MyTokenObtainPairView, addNote, deleteNote, updateNote, register, logout

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path("notes/", getNotes, name="get_notes"),
    path("addnote/", addNote, name="add_note"),
    path("deletenote/<int:id>", deleteNote, name="delete_note"),
    path("updatenote/<int:id>", updateNote, name="update_note"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]