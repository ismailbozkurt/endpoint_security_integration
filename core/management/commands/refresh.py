from django.core.management.base import BaseCommand
from utils.setup import delete_products, load_product_services


class Command(BaseCommand):
    help = "Recreates all products from config files to database."

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING(
                'This command will delete all the keys for all products!\n'
                'Do you want to continue? [Y/n]')
        )
        prompt = input()
        if prompt.upper() == 'Y':
            delete_products()
            load_product_services()
