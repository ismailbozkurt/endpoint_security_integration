from core.models import (
    Product,
    IPList
)
from api.serializers import ProductSerializer


def get_products() -> dict:
    data = Product.objects.all()
    serialized = ProductSerializer(data, many=True)
    return serialized.data


def populate_test_data():
    IPList.objects.all().delete()
    # Keys.objects.all().delete()
    Product.objects.all().delete()

    cs = Product.objects.create(
        display="Crowdstrike",
        name="crowdstrike",
        credentials={
            "Base URL": "text",
            "Client ID": "text",
            "Client Secret": "password",
        }
    )

    s = Product.objects.create(
        display="Sentinel One",
        name="sentinel_one",
        credentials={
            "Base URL": "text",
            "Token": "password",
        },
        keys={
            "Base URL": "test",
            "Token": "dummy",
        }
    )

    # Keys.objects.create(
    #     product=s,
    #     keys={
    #         "Base URL": "test",
    #         "Token": "dummy",
    #     }
    # )

    IPList.objects.create(ip="192.168.10.1", product=s)
    IPList.objects.create(ip="192.168.10.2", product=s)
    IPList.objects.create(ip="192.168.10.3", product=s)

    IPList.objects.create(ip="192.168.10.1", product=cs)
