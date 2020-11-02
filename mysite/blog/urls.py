from django.urls import path
from . import views

urlpatterns = [
	# takes empty string and returns result from PostList view, optional param name for name of view
    path('', views.PostList.as_view(), name='home'), 

    # resolves slug; angle brackets capture value from url and returns equivalent post detail page
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    # resolves slug; map the view
    # angle brackets capture value from url and returns equivalent post detail page
    path('<slug:slug>/', views.post_detail, name='post_detail')

]


