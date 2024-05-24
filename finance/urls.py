from django.urls import include, path

from .views import PersonIndex
app_name = 'finance'

urlpatterns = [
    path('person/', PersonIndex.as_view(), name='person'),
   # path('list/', TargetList.as_view(), name='list'),
   # path('create/', TargetCreate.as_view(), name='create'),
   # path('update/<int:pk>/', TargetUpdate.as_view(), name='update'),
    #path('delete/<int:pk>/', TargetDelete.as_view(), name='delete'),
]