# Generated by Django 4.2 on 2023-05-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_question_shoseki_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='shoseki',
            field=models.CharField(blank=True, choices=[('キタミ式ITイラスト塾\u3000応用情報技術者\u3000令和03年', 'キタミ式ITイラスト塾\u3000応用情報技術者\u3000令和03年'), ('令和04年【春期】\u3000応用情報技術者\u3000過去問題集', '令和04年【春期】\u3000応用情報技術者\u3000過去問題集'), ('応用情報技術者\u3000試験によくでる問題集【午後】', '応用情報技術者\u3000試験によくでる問題集【午後】'), ('応用情報技術者テキスト&問題集2020年版', '応用情報技術者テキスト&問題集2020年版'), ('LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応', 'LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応'), ('Python3エンジニア認定実践試験Web問題', 'Python3エンジニア認定実践試験Web問題'), ('Python3エンジニア認定データ分析試験Web問題', 'Python3エンジニア認定データ分析試験Web問題'), ('Python3エンジニア認定基礎試験Web問題', 'Python3エンジニア認定基礎試験Web問題'), ('Python3エンジニア認定基礎試験問題集', 'Python3エンジニア認定基礎試験問題集'), ('徹底攻略データサイエンティスト検定リテラシーレベル問題集', '徹底攻略データサイエンティスト検定リテラシーレベル問題集'), ('データベーススペシャリスト教科書令和4年度', 'データベーススペシャリスト教科書令和4年度'), ('Bronze 12c SQL 基礎問題集', 'Bronze 12c SQL 基礎問題集'), ('シェルワンライナー100本ノック', 'シェルワンライナー100本ノック'), ('Access VBA スタンダード', 'Access VBA スタンダード'), ('Access VBA ベーシック', 'Access VBA ベーシック'), ('Excel VBA スタンダード', 'Excel VBA スタンダード'), ('Excel VBA ベーシック', 'Excel VBA ベーシック'), ('統計検定2級\u3000模擬問題集1', '統計検定2級\u3000模擬問題集1'), ('統計検定2級\u3000模擬問題集2', '統計検定2級\u3000模擬問題集2'), ('統計検定2級\u3000模擬問題集3', '統計検定2級\u3000模擬問題集3'), ('基本情報技術者らくらく突破 Python', '基本情報技術者らくらく突破 Python'), ('情報セキュリティマネジメント教科書令和2年度', '情報セキュリティマネジメント教科書令和2年度'), ('LPICレベル1スピードマスター問題集', 'LPICレベル1スピードマスター問題集'), ('ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集', 'ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集'), ('徹底攻略ディープラーニングE資格エンジニア問題集', '徹底攻略ディープラーニングE資格エンジニア問題集')], max_length=200, null=True, verbose_name='書籍'),
        ),
    ]
