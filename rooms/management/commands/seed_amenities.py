
from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    help = "This command created amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me tell you that I love you",
    #     )
        

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Sofa",
            "Stereo",
            "Toilet",
            "Tv",

        ]
        
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))

