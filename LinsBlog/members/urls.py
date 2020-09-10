from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, UserEditStaffView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('editprofile/', UserEditView.as_view(), name="editprofile"),
    path('editprofilestaff/', UserEditStaffView.as_view(), name="editprofilestaff"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/changepassword.html')),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="showprofile"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="editprofilepage"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="createprofilepage"),

]
