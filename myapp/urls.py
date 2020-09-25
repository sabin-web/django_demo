from django.urls import path,include

from . import views


app_name = 'myapp'

urlpatterns = [
	path('',views.MainView.as_view(),name='all'),
	path('create/',views.NewEmployeeInfo.as_view(),name='create'),
	path('update/<int:pk>',views.UpdateEmployeeInfo.as_view(),name='update'),
	path('delete/<int:pk>',views.DeleteEmployeeInfo.as_view(),name='delete'),

]