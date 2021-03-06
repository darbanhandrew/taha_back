# Generated by Django 3.1.5 on 2021-01-28 13:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('a', 'Active'), ('d', 'Deactive')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tahaApp.basemodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('tahaApp.basemodel',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tahaApp.basemodel')),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('categories', models.ManyToManyField(to='tahaApp.Category')),
            ],
            bases=('tahaApp.basemodel',),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('related_affiliate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tahaApp.affiliate')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('types', models.CharField(choices=[('a', 'Add'), ('m', 'Minus')], max_length=2)),
                ('related_affiliate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tahaApp.affiliate')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tahaApp.basemodel')),
                ('address', models.TextField(max_length=1000)),
                ('email', models.EmailField(blank=True, max_length=48, verbose_name='E Mail')),
                ('commission', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('shop_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('tahaApp.basemodel',),
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField(blank=True, null=True)),
                ('affiliate_amount', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('related_affiliate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tahaApp.affiliate')),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tahaApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='related_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tahaApp.shop'),
        ),
    ]
