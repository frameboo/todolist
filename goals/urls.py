from django.urls import path

from goals import views


urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view(), name='create_goal_category'),
    path('goal_category/list', views.GoalCategoryListView.as_view(), name='list_goal_category'),
    path('goal_category/<int:pk>', views.GoalCategoryView.as_view(), name='retrieve_goal_category'),
    path('goal/create', views.GoalCreateView.as_view(), name='create_goal'),
    path('goal/list', views.GoalListView.as_view(), name='list_goal'),
    path('goal/<int:pk>', views.GoalView.as_view(), name='retrieve_goal'),
    path('goal_comment/create', views.GoalCommentCreateView.as_view(), name='create_goal_comment'),
    path('goal_comment/list', views.GoalCommentListView.as_view(), name='list_goal_comment'),
    path('goal_comment/<int:pk>', views.GoalCommentView.as_view(), name='retrieve_goal_comment'),
    path('board/<int:pk>', views.BoardView.as_view(), name='retrieve_board'),
    path('board/list', views.BoardListView.as_view(), name='list_board'),
    path('board/create', views.BoardCreateView.as_view(), name='create_board'),

]
