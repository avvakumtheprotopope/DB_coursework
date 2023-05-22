from django.contrib import admin

from .models import *

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patronymic', 'surname', 'club')
    list_editable = ('club',)

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patronymic', 'surname', 'breed', 'club')
    list_editable = ('breed',)

#class BreedAdmin(admin.ModelAdmin):
    #list_display = ('id', 'name', 'ring',)
    #list_display_links = ('id', 'name')

#class RingAdmin(admin.ModelAdmin):
    #list_display = ('id', 'number',)
    #list_display_links = ('id', 'number')

#class DogAdmin(admin.ModelAdmin):
    #list_display = ('id', 'name', 'age', 'breed', 'mom', 'dad', 'owner', 'number', 'grade','club')
    #list_display_links = ('id', 'number')
    #list_editable = ('grade', 'club')


#class ClubAdmin(admin.ModelAdmin):
    #list_display = ('id', 'name', 'lower', 'upper')
    #list_display_links = ('id', 'name')



admin.site.register(Owner, OwnerAdmin)
admin.site.register(Expert, ExpertAdmin)
#admin.site.register(Breed, BreedAdmin)
#admin.site.register(Ring, RingAdmin)
#admin.site.register(Dog, DogAdmin)
#admin.site.register(Club, ClubAdmin)

