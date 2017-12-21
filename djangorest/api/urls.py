from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
	url(r'^nba/stats/', views.NBAStatsView.as_view(), name="nba_stats"),
}

urlpatterns = format_suffix_patterns(urlpatterns)