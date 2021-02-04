import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from tahaApp.models import *


class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        filter_fields = ['id', 'title', 'body']
        interfaces = (relay.Node,)

    def resolve_image(self, info):
        """Resolve product image absolute path"""
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


class AffiliateNode(DjangoObjectType):
    class Meta:
        model = Affiliate
        filter_fields = ['id', 'title', 'body']
        interfaces = (relay.Node,)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['id', 'title', 'body']
        interfaces = (relay.Node,)


class RecieptNode(DjangoObjectType):
    class Meta:
        model = Receipt
        filter_fields = ['id', 'created_at']
        interfaces = (relay.Node,)


class TransactionNode(DjangoObjectType):
    class Meta:
        model = Transaction
        filter_fields = ['id', 'created_at']
        interfaces = (relay.Node,)


class WalletNode(DjangoObjectType):
    class Meta:
        model = Wallet
        filter_fields = ['id', 'created_at']
        interfaces = (relay.Node,)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['id', 'name']
        interfaces = (relay.Node,)


class TahaQuery(graphene.ObjectType):
    shop = relay.Node.Field(ShopNode)
    shop_list = DjangoFilterConnectionField(ShopNode)

    affiliate = relay.Node.Field(AffiliateNode)
    affiliate_list = DjangoFilterConnectionField(AffiliateNode)

    product = relay.Node.Field(ProductNode)
    product_list = DjangoFilterConnectionField(ProductNode)

    receipt = relay.Node.Field(RecieptNode)
    receipt_list = DjangoFilterConnectionField(RecieptNode)

    transaction = relay.Node.Field(TransactionNode)
    transaction_list = DjangoFilterConnectionField(TransactionNode)

    wallet = relay.Node.Field(WalletNode)
    wallet_list = DjangoFilterConnectionField(WalletNode)

    category = relay.Node.Field(CategoryNode)
    category_list = DjangoFilterConnectionField(CategoryNode)
