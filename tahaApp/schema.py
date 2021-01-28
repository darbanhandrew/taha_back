import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from tahaApp.models import Shop, Affiliate, Product, Receipt


class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        filter_fields = ['title', 'body']
        interfaces = (relay.Node,)


class AffiliateNode(DjangoObjectType):
    class Meta:
        model = Affiliate
        filter_fields = ['title', 'body']
        interfaces = (relay.Node,)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['title', 'body']
        interfaces = (relay.Node,)


class RecieptNode(DjangoObjectType):
    class Meta:
        model = Receipt
        filter_fields = ['title', 'body']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    shop = relay.Node.Field(ShopNode)
    shop_list = DjangoFilterConnectionField(ShopNode)

    affiliate = relay.Node.Field(AffiliateNode)
    affiliate_list = DjangoFilterConnectionField(AffiliateNode)

    product = relay.Node.Field(ProductNode)
    product_list = DjangoFilterConnectionField(ProductNode)

    receipt = relay.Node.Field(RecieptNode)
    receipt_list = DjangoFilterConnectionField(RecieptNode)
