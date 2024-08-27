from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    # views
    # path("", trainee_list, name="trainee_list"),
    # path("Add/", trainee_create, name="trainee_create"),
    # class views
    path("", TraineeListG.as_view(), name="trainee_list"),
    path("Add/", TraineeCreate.as_view(), name="trainee_create"),
    path("Update/<int:id>", trainee_update, name="trainee_update"),
    path("Delete/<int:id>", trainee_delete, name="trainee_delete"),
    path("Details/<int:id>", trainee_details, name="trainee_details"),
    # path("Details/<int:id>", TraineeDetailsG.as_view(), name="trainee_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
