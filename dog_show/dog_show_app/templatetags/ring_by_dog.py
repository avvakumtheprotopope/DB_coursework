from django import template
from dog_show_app.models import Ring,Breed,Dog

register = template.Library()


@register.simple_tag()
def ring_by_dog(nice_dog_id):
    return Ring.objects.get(id=Breed.objects.get(id=Dog.objects.get(id=nice_dog_id).breed_id).ring_id)
