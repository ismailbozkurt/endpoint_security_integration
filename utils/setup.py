import os
import yaml
from core.integration import IntegrationService
from django.db.utils import IntegrityError, OperationalError
from importlib import import_module
from core.models import Product
from utils.log import log


FOLDER = 'Packs'
CONFIG_FILE = 'config.yml'


def load_product_services():
    for i in os.listdir(FOLDER):
        try:
            module = import_module(
                "%s.%s.service" % (FOLDER, i))
            IntegrationService.add_service(i, module.Service())
        except Exception:
            pass

        add_product_to_db(i)


def add_product_to_db(name):
    with open(os.path.join(FOLDER, name, CONFIG_FILE)) as file:
        config = yaml.load(file, yaml.Loader)
        columns = {
            "name": config.get('name'),
            "display": config.get('display'),
            'fields': config.get('fields')
        }

    try:
        Product.objects.get(name=name)
        log.debug('Product already exists %s' % (name))
    except Product.DoesNotExist:
        try:
            Product.objects.create(**columns)
            log.debug('Product add db %s' % (name))
        except IntegrityError as err:
            log.error('Product integrity error %s | %s' % (name, err))
            pass
    except OperationalError as err:
        log.error('Product operational error %s | %s' % (name, err))
        pass
