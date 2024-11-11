# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
urlpatterns = [
    # path('', include('djangoapp.urls')),
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),
    # path('login/', TemplateView.as_view(template_name='index.html'), name='login'),
    # path('login/', TemplateView.as_view(template_name="/server/frontend/build/index.html")),

    # path for dealer reviews view

    # path for add a review view


    path(route='logout', view=views.logout, name='logout'),

    path(route='register', view=views.registration, name='register'),
    # path('register/', TemplateView.as_view(template_name="index.html"), name='register'),

    path(route='get_cars', view=views.get_cars, name ='getcars'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
