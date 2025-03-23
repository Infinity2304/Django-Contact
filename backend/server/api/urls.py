from django.urls import path
from .views import signUp, login, logout, saveContact, getContact, updateContact, deleteContact, getAll

urlpatterns = [
    path('signup', signUp, name='signUp'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('contact/save/', saveContact, name='save_Contact'),
    path('contact/get/', getContact, name='get_Contact'),
    path('contact/update/<int:pk>/', updateContact, name='update_Contact'),
    path('contact/delete/<int:pk>/', deleteContact, name='delete_Contact'),
    path('contact/getall/', getAll, name='get_all'),

]