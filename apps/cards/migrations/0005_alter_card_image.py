# Generated by Django 4.1.2 on 2022-11-04 13:49

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0004_tag_card_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=["middle", "center"],
                force_format=None,
                keep_meta=True,
                null=True,
                quality=-1,
                scale=None,
                size=[200, 200],
                upload_to="images",
            ),
        ),
    ]