from django.urls import path
from simpleapp.views import NewList, NewDetailView, NewUpdateView, NewDeleteView, AddPost

urlpatterns = [
    path('', NewList.as_view()),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail'),
    path('create/', AddPost.as_view(), name='new_create'),
    path('<int:pk>/create/', NewUpdateView.as_view(), name='new_update'),
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),
]














