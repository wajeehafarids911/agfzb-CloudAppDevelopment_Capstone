from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path(route='about/', view=views.getAbout, name='n_about'),

    # path for contact us view
    path(route='contact/', view=views.getContact, name='n_contact'),
    # path for registration

    # path for login
    path(route='login/', view=views.login_request, name='n_login'),
    path(route='logout/', view=views.logout_request, name='n_logout'),

    # path for logout

    path(route='', view=views.get_dealerships, name='n_index'),
    path(route='static/', view=views.getStaticPage, name='n_static'),
    

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)