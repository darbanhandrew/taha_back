# Generated by Django 3.1.6 on 2021-02-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tahaApp', '0009_profile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='71321', max_length=7)),
                ('valid', models.CharField(choices=[('valid', 'Valid'), ('invalid', 'Invalid')], default='valid', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='otp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tahaApp.otp'),
        ),
    ]