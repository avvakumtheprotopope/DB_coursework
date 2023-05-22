from django.shortcuts import render



from .models import *

def main_menu(request):
    context = {}
    return render(request, 'dog_show_app/Main_t.html', context=context)


def ring_by_owner_page(request):
    owners = Owner.objects.all()
    context = {
        'owners': owners,
    }
    return render(request, 'dog_show_app/ring_t.html', context=context)

def owner_page(request, owner_id):
    nice_dogs = Owner.objects.get(id=owner_id).dogs.all()
    breeds = Breed.objects.all()
    rings = Ring.objects.all()

    context = {
        'nice_dogs': nice_dogs,
        'breeds': breeds,
        'rings': rings
    }
    return render(request, 'dog_show_app/owner_page_t.html', context=context)


def breeds_by_club_page(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs,
    }
    return render(request, 'dog_show_app/breeds_t.html', context=context)

def club_breeds_page(request, club_id):
    dogs = Club.objects.get(id=club_id).dogs.all()
    breeds = Breed.objects.all()

    context = {
        'dogs': dogs,
        'breeds': breeds,
    }
    return render(request, 'dog_show_app/club_breeds_page_t.html', context=context)


def medals_by_club_page(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs,
    }
    return render(request, 'dog_show_app/medals_t.html', context=context)


def club_medals_page(request, club_id):
    dogs = Club.objects.get(id=club_id).dogs.all()
    gold = 0
    silver = 0
    bronze = 0
    for dog in dogs:
        if dog.grade == 1:
            gold += 1
        elif dog.grade == 2:
            silver += 1
        elif dog.grade == 3:
            bronze += 1
    context = {
        'gold': gold,
        'silver': silver,
        'bronze': bronze,
    }
    return render(request, 'dog_show_app/club_medals_page_t.html', context=context)





def experts_by_breed_page(request):
    breeds = Breed.objects.all()
    context = {
        'breeds': breeds,
    }
    return render(request, 'dog_show_app/experts_t.html', context=context)


def breed_page(request, breed_id):
    experts = Breed.objects.get(id=breed_id).experts.all()
    context = {
        'experts': experts,
    }
    return render(request, 'dog_show_app/breed_experts_page_t.html', context=context)

def dog_by_expert_page(request):
    experts = Expert.objects.all()
    context = {
        'experts': experts,
    }
    return render(request, 'dog_show_app/dog_t.html', context=context)


def expert_page(request, expert_id):
    dogs = Breed.objects.get(id=Expert.objects.get(id=expert_id).breed_id).dogs.all()
    context = {
        'dogs': dogs,
    }
    return render(request, 'dog_show_app/expert_page_t.html', context=context)
