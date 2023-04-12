from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.home),
    path('create/' ,views.createTodo, name = 'create'),
    path('task/<str:id>' ,views.singleTask , name = 'task' ),
    path('update/<str:id>' ,views.updateTask , name = 'update' ),
    path('delete/<str:id>' ,views.deleteTask , name = 'delete' ),
    path('createItem/<str:id>' ,views.createItem, name = 'createItem'),
    path('updateItem/<str:id>' ,views.updateItem , name = 'updateItem' ),
    path('deleteItem/<str:id>' ,views.deleteItem , name = 'deleteItem' ),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
]
