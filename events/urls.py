from django.urls import path

from .views import HomePageView, EventListView, EventDetailView

urlpatterns = [
    path("", HomePageView.as_view(),name= "home"),
    path("events/", EventListView.as_view(),name= "event_list"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail")
]