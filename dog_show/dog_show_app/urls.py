from django.urls import path

from dog_show_app.views import *

urlpatterns = [
    path('', main_menu, name='main'),
    path('ring/', ring_by_owner_page, name='ring_by_owner'),
    path('ring/<int:owner_id>/', owner_page, name='owner'),
    path('breeds/', breeds_by_club_page, name='breeds_by_club'),
    path('breeds/<int:club_id>/', club_breeds_page, name='club_breeds'),
    path('medals/', medals_by_club_page, name='medals_by_club'),
    path('medals/<int:club_id>/', club_medals_page, name='club_medals'),
    path('experts/', experts_by_breed_page, name='experts_by_breed'),
    path('experts/<int:breed_id>/', breed_page, name='breed'),
    path('dog/', dog_by_expert_page, name='dog_by_expert'),
    path('dog/<int:expert_id>/', expert_page, name='expert'),

]
