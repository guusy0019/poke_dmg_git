from django.db import models

# Create your models here.
#実用性を兼ねて全国図鑑のnumberを採用する
CHOICE_poke_type =(
    ('なし', 'なし'), 
    ('ノーマル', 'ノーマル'), 
    ('ほのお', 'ほのお'),
    ('みず', 'みず'), 
    ('でんき','でんき'),
    ('くさ', 'くさ'),
    ('こおり', 'こおり'),
    ('かくとう','かくとう'),
    ('どく','どく'),
    ('じめん', 'じめん'),
    ('ひこう', 'ひこう'),
    ('エスパー','エスパー'),
    ('むし', 'むし'),
    ('いわ', 'いわ'),
    ('ゴースト','ゴースト'),
    ('ドラゴン', 'ドラゴン'),
    ('あく', 'あく'),
    ('はがね','はがね'),
    ('フェアリー', 'フェアリー'),
)

CHOICE_poke_type2 =(
    ('なし', 'なし'), 
    ('ノーマル', 'ノーマル'), 
    ('ほのお', 'ほのお'),
    ('みず', 'みず'), 
    ('でんき','でんき'),
    ('くさ', 'くさ'),
    ('こおり', 'こおり'),
    ('かくとう','かくとう'),
    ('どく','どく'),
    ('じめん', 'じめん'),
    ('ひこう', 'ひこう'),
    ('エスパー','エスパー'),
    ('むし', 'むし'),
    ('いわ', 'いわ'),
    ('ゴースト','ゴースト'),
    ('ドラゴン', 'ドラゴン'),
    ('あく', 'あく'),
    ('はがね','はがね'),
    ('フェアリー', 'フェアリー'),
)
class PokeModel(models.Model):
    poke_name = models.CharField(max_length=50, null=True, blank=True)
    poke_image = models.ImageField(upload_to='')
    poke_number = models.IntegerField(null=True, blank=True)
    poke_type = models.CharField(
        max_length=30, 
        null=True, 
        blank=True,
        choices=CHOICE_poke_type,
        default='なし',
        )
    poke_type2 = models.CharField(
        max_length=30, 
        null=True, 
        blank=True,
        choices=CHOICE_poke_type2,
        default='なし',
        )
    poke_ability = models.CharField(max_length=50, null=True, blank=True)
    poke_ability2 = models.CharField(max_length=50, null=True, blank=True)
    poke_abi_hidden = models.CharField(max_length=50, null=True, blank=True)
    poke_hp = models.IntegerField(null=True, blank=True)
    poke_attack = models.IntegerField(null=True, blank=True)
    poke_defense = models.IntegerField(null=True, blank=True)
    poke_sp_atk = models.IntegerField(null=True, blank=True)
    poke_sp_def = models.IntegerField(null=True, blank=True)
    poke_speed = models.IntegerField(null=True, blank=True)
    poke_base_stats = models.IntegerField(null=True, blank=True)
    before_evolution = models.BooleanField(default=True, help_text='進化前ならTrue')

    def __str__(self):
        return self.poke_name
    
CHOICE_move_type =(
    ('なし', 'なし'), 
    ('ノーマル', 'ノーマル'), 
    ('ほのお', 'ほのお'),
    ('みず', 'みず'), 
    ('でんき','でんき'),
    ('くさ', 'くさ'),
    ('こおり', 'こおり'),
    ('かくとう','かくとう'),
    ('どく','どく'),
    ('じめん', 'じめん'),
    ('ひこう', 'ひこう'),
    ('エスパー','エスパー'),
    ('むし', 'むし'),
    ('いわ', 'いわ'),
    ('ゴースト','ゴースト'),
    ('ドラゴン', 'ドラゴン'),
    ('あく', 'あく'),
    ('はがね','はがね'),
    ('フェアリー', 'フェアリー'),
)
    
CHOICE_move_class = (('physical', '物理技'), ('special', '特殊技'),('status', '変化技'))

class PokeMove(models.Model):
    move_name = models.CharField(max_length=20, null=True, blank=True)
    move_type = models.CharField(
        max_length=10, 
        null=True, 
        blank=True,
        choices=CHOICE_move_type,
        default='なし',
        )
    
    move_class = models.CharField(
        help_text='技の分類',
        max_length=30, 
        choices=CHOICE_move_class,
        null=True,
        blank=True,
        default='physical',
        )
    move_power = models.IntegerField(help_text='技の威力', null=True, blank=True)
    move_accuracy = models.IntegerField(help_text='命中率', null=True, blank=True)
    move_PP = models.IntegerField(help_text='技の使用可能回数', null=True, blank=True)
    move_direct = models.BooleanField(help_text='直接ならcheck', default=True, null=True, blank=True)
    move_defend = models.BooleanField(help_text='守れるならcheck', default=True, null=True, blank=True)
    move_effect = models.TextField(help_text='技の説明', null=True, blank=True)

    def __str__(self):
        return self.move_name
