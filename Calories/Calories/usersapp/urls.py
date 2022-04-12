from django.urls import path

from Calories.usersapp.views import HomePage, RegistrateUser, Login, Logout, ProfileView, ProfileDetailsView, \
    UpdateProfileView, DeleteProfileView

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
    path('register/', RegistrateUser.as_view(), name='registrate user'),
    path('login/', Login.as_view(), name='login page'),
    path('logout/', Logout.as_view(), name='logout page'),
    path('create/profile/', ProfileView.as_view(), name='create profile'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>/', UpdateProfileView.as_view(), name='edit profile'),
    path('delete/<int:pk>/', DeleteProfileView.as_view(), name='delete account')
]