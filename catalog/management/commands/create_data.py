import datetime
import random
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Product


class Command(BaseCommand):
    help = "This help information for this command"

    def add_arguments(self, parser):
        parser.add_argument("first", type=int, help="A number less than 100")
        parser.add_argument("second", nargs=3, type=str, help="Three strings.")
        parser.add_argument("--option1", default="default", help="The optional value")
        parser.add_argument("--option2", action="store_true", help="True if passed")

    def handle(self, *args, **options):
        # print("command ")
        # print("second command")
        # print(f"First {options['first']}")
        # print(f"Option1 {options['option1']}")

        if options["first"] < 100: # python manage.py create_data 50
            self.stdout.write(self.style.SUCCESS("Good job, numbers is lowe than a hundred."))
        else:
            raise CommandError("That number is greater than 100.")

        self.stdout.write(f"The value of --option1 is {options['option1']}")

        for value in options["second"]:
            self.stdout.write(f"Value {value}")

        if options["option2"]:
            self.stdout.write(self.style.SUCCESS("Option2 is TRUE"))
        else:
            self.stdout.write(self.style.WARNING("Option2 is FALSE"))
