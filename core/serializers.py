"""
Deprecated
"""

from core.models import Product
from django.db.models import QuerySet


def _serialize(product: Product):
    fields = {}

    for i in product.fields:
        fields[i['display']] = i['type']

    _json = {
        "display": product.display,
        "name": product.name,
        "fields": fields,
        "keys": product.keys,
        # "ip_list": [
        #     i.ip for i in product.ip_list.all()
        # ]
    }
    return _json


def serialize(object):
    if isinstance(object, QuerySet):
        return [
            _serialize(i) for i in object
        ]
    return _serialize(object)
