from django.urls import path

from . import views

app_name = 'career'
urlpatterns = [
    path('quarter/', views.quarter_list, name='quarter_list'),
    path('quarter/create/', views.quarter_create, name='quarter_create'),
    path('quarter/<int:q_id>/details/', views.quarter_details, name='quarter_details'),
    path('quarter/<int:q_id>/update/', views.quarter_update, name='quarter_update'),
    path('quarter/<int:q_id>/delete/', views.quarter_delete, name='quarter_delete'),

    path('level/', views.LevelListView.as_view(), name='level_list'),
    path('level/create/', views.LevelCreateView.as_view(), name='level_create'),
    path('level/<int:pk>/details/', views.LevelDetailView.as_view(), name='level_details'),
    path('level/<int:pk>/update/', views.LevelUpdateView.as_view(), name='level_update'),
    path('level/<int:pk>/delete/', views.LevelDeleteView.as_view(), name='level_delete'),

    path('career/', views.CareerListView.as_view(), name='career_list'),
    path('career/create/', views.CareerCreateView.as_view(), name='career_create'),
    path('career/<int:pk>/details/', views.CareerDetailView.as_view(), name='career_details'),
    path('career/<int:pk>/update/', views.CareerUpdateView.as_view(), name='career_update'),
    path('career/<int:pk>/delete/', views.CareerDeleteView.as_view(), name='career_delete'),

    path('subject/<int:career_id>/', views.SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:career_id>/create/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:career_id>/<int:pk>/update/', views.SubjectUpdateView.as_view(), name='subject_update'),
]