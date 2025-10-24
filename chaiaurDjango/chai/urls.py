from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_chai,name='all_chai'),
    path('<int:chai_id>/',views.chai_detail,name="chai_detail"),
    path("chaistore",views.chai_store_from_view,name="chai_store"),
    path('order/',views.order,name="order"),
]