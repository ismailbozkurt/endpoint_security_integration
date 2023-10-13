from drf_spectacular.generators import SchemaGenerator
from .products import get_products, type_fixer

TITLE = 'Endpoint Security Integration'
TAG = 'Integration'
URL = '/api/integration/{}'
PRODUCTS_ENDPOINT = '/api/products/'


class DynamicSchemaGenerator(SchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)

        schema['info']['title'] = TITLE
        products = get_products()
        paths = schema.get('paths')
        components = schema.get('components')

        for product in products:
            product_name = product.get('name')
            post_schema = {
                'operationId': f'api_integration_create_{product_name}',
                'tags': [TAG],
                'requestBody': {
                    'content': {
                        'application/json': {
                            'schema': {
                                '$ref': f'#/components/schemas/{product_name}'
                            }
                        }
                    }
                },
                'responses': self.post_response_schema(schema)
            }

            delete_schema = {
                'operationId': f'api_integration_delete_{product_name}',
                'tags': [TAG],
                'responses': {
                    '204': {
                        'description': 'No response body'
                    }
                }
            }

            inner_schema = {
                'post': post_schema,
                'delete': delete_schema
            }
            paths[URL.format(product_name)] = inner_schema

            product_schema = self.get_product_body_schema(product)
            components['schemas'][product_name] = product_schema

        return schema

    def get_product_body_schema(self, product):
        properties = {}

        for field in product['fields']:
            properties[field['name']] = {
                'type': type_fixer(field['type']),
                'description': field['display'],
                'required': field['required'],
            }

        schema = {
            "type": "object",
            "properties": properties
        }
        return schema

    def post_response_schema(self, schema):
        paths = schema['paths']
        responses = paths[PRODUCTS_ENDPOINT]['get']['responses']
        return {
            '201': responses['200']
        }
