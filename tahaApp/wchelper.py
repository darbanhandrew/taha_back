from woocommerce import API

from tahaApp.models import Product, Shop

wcapi = API(
    url="https://gaat.fashion",
    consumer_key="ck_3736481ccc3e247185d42558c7d0eb94fab67a2b",
    consumer_secret="cs_73a28ae70a6d6296dc45f835425e44e535349df0",
    version="wc/v3"
)


def get_products():
    r = wcapi.get("products", params={"fields": "id,name,images", "per_page": "1"})
    products = r.json()
    for product in products:
        p = Product()
        shop = Shop.objects.first()
        p.related_shop = shop
        p.name = product['name']
        p.save()
        return p.id
    return r.json()
