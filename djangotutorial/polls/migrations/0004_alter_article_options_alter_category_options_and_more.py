# Generated by Django 4.2 on 2024-12-25 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import polls.custom_field


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_feed_alter_article_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='feed',
            options={'verbose_name_plural': 'Feed'},
        ),
        migrations.AlterField(
            model_name='article',
            name='special',
            field=polls.custom_field.CustomBooleanField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_homepage',
            field=polls.custom_field.CustomBooleanField(),
        ),
        migrations.CreateModel(
            name='ArticleViewHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-viewed_at'],
            },
        ),
    ]