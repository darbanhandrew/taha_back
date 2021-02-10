from django.contrib import admin
from django.apps import apps
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, MyAdmin)
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
