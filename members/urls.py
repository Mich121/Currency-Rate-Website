from django.urls import path
from .views import UserRegisterView, CreateProfile, UpdateProfile

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('<int:pk>/update_profile_page', UpdateProfile.as_view(), name="update_profile_page"),
    path('createprofile/', CreateProfile.as_view(), name="create_profile_page"),
]