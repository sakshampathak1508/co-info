from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name="home"),
    path('beds/',views.beds,name="beds"),
    path('oxygen/',views.oxygen,name="oxy"),
    path('plasma/',views.plasma,name="plasma"),
    path('medicines/',views.meds,name="medicines"),
]