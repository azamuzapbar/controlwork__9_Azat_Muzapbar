# Generated by Django 4.2 on 2023-04-22 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_users', to='gallery.photo', verbose_name='Избранное')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_photos', to=settings.AUTH_USER_MODEL, verbose_name='Избранное')),
            ],
        ),
    ]
