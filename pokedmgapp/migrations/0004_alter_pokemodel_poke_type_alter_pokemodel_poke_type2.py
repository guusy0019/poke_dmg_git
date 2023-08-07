# Generated by Django 4.2.2 on 2023-07-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokedmgapp", "0003_pokemove_move_pp_pokemove_move_accuracy_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemodel",
            name="poke_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "なし"),
                    ("normal", "ノーマル"),
                    ("fire", "ほのお"),
                    ("water", "みず"),
                    ("electric", "でんき"),
                    ("grass", "くさ"),
                    ("ice", "こおり"),
                    ("fighting", "かくとう"),
                    ("poison", "どく"),
                    ("ground", "じめん"),
                    ("flying", "ひこう"),
                    ("psychic", "エスパー"),
                    ("bug", "むし"),
                    ("rock", "いわ"),
                    ("ghost", "ゴースト"),
                    ("dragon", "ドラゴン"),
                    ("dark", "あく"),
                    ("steel", "はがね"),
                    ("fairy", "フェアリー"),
                ],
                default="none",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="pokemodel",
            name="poke_type2",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "なし"),
                    ("normal", "ノーマル"),
                    ("fire", "ほのお"),
                    ("water", "みず"),
                    ("electric", "でんき"),
                    ("grass", "くさ"),
                    ("ice", "こおり"),
                    ("fighting", "かくとう"),
                    ("poison", "どく"),
                    ("ground", "じめん"),
                    ("flying", "ひこう"),
                    ("psychic", "エスパー"),
                    ("bug", "むし"),
                    ("rock", "いわ"),
                    ("ghost", "ゴースト"),
                    ("dragon", "ドラゴン"),
                    ("dark", "あく"),
                    ("steel", "はがね"),
                    ("fairy", "フェアリー"),
                ],
                default="none",
                max_length=30,
                null=True,
            ),
        ),
    ]