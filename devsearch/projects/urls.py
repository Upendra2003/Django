from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('project/<str:id>',views.project,name='project'),
    path('publish-project',views.publish,name='publish-project')
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)