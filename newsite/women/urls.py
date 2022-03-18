from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('recommend/', RecFormView.as_view(), name='recommend'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]