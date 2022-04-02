#URLS: főoldal: gunnar1904/pythonanywhere.com/hophooray/home
#rólunk: gunnar1904/pythonanywhere.com/hophooray/about
#készlet: gunnar1904/pythonanywhere.com/hophooray/inventory
#készlet megtekintése: gunnar1904/pythonanywhere.com/hophooray/inventory/<int:pk>
#készlet hozzáadása: gunnar1904/pythonanywhere.com/hophooray/inventory/create
#készlet módosítása: gunnar1904/pythonanywhere.com/hophooray/inventory/<int:pk>/update
#készlet törlése: gunnar1904/pythonanywhere.com/hophooray/inventory/<int:pk>/delete


from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'hophooray'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home', views.HomeView.as_view()),
    path('about', views.AboutView.as_view()),
    path('inventory', views.InventoryListView.as_view(), name='inventory'),
    path('inventory/<int:pk>', views.InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/create', views.InventoryCreateView.as_view(success_url=reverse_lazy('hophooray:inventory')), name='inventory_form'),
    path('inventory/<int:pk>/update', views.InventoryUpdateView.as_view(success_url=reverse_lazy('hophooray:inventory')), name='inventory_update'),
    path('inventory/<int:pk>/delete', views.InventoryDeleteView.as_view(success_url=reverse_lazy('hophooray:inventory')), name='inventory_confirm_delete'),
]