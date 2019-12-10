# Generated by Django 2.2.8 on 2019-12-09 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='articleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artName', models.CharField(max_length=200)),
                ('catFK', models.IntegerField()),
                ('referenceFK', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='artComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentType', models.IntegerField()),
                ('modelReferenceFK', models.IntegerField()),
                ('articleReferenceFK', models.IntegerField()),
                ('creationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('isActive', models.BooleanField(default=True)),
                ('commentContent', models.TextField()),
                ('commentDescription', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
