from django.urls import path
from .views import MatchView, MatchAllView

urlpatterns = [
    path('get_recent_matchdata',MatchView.as_view()),
    path('get_all_matchdata',MatchAllView.as_view())
]
