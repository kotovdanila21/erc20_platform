from django.urls import include, path

urlpatterns = [
    path("contracts/", include("app.contracts.urls")),
]