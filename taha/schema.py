import graphene
from tahaApp.schema import Query
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

schema = graphene.Schema(query=Query)
