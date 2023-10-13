from core.models import Product
from typing import Dict, List
import jsonschema
from .products import type_fixer
from utils.log import log


def remove_keys(name):
    try:
        product = Product.objects.get(name=name)
        product.keys = None
        product.save()
        return True
    except Product.DoesNotExist:
        return False


def set_keys(name, keys: Dict):
    try:
        product = Product.objects.get(name=name)
        product.keys = keys
        product.save()
        return product
    except Product.DoesNotExist:
        log.error('Product not found with name: %s', name)
        return None


def validate_fields(product_name: str, data: Dict) -> bool:
    try:
        product = Product.objects.get(name=product_name)
        if product.fields:
            schema = generate_json_schema(product.fields)
            jsonschema.validate(instance=data, schema=schema)
            return True
    except Product.DoesNotExist:
        pass
    except jsonschema.exceptions.ValidationError:
        pass
    except jsonschema.exceptions.SchemaError:
        pass

    return False


def generate_json_schema(fields: List[Dict]) -> Dict:
    json_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {},
        "required": []
    }

    for field in fields:
        field_name = field.get('name')
        is_required = field.get('required', False)

        if is_required:
            json_schema['required'].append(field_name)

        _type = type_fixer(field.get('type'))
        json_schema['properties'][field_name] = {
            "type": _type
        }

    return json_schema
