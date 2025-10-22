from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.addRecipe,name='add'),
    path('update/<int:id>',views.UpdateRecipe,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
]