# Generated by Django 4.1.5 on 2023-04-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_question_created_at_alter_question_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('JAVA', 'JAVA'), ('Linux', 'Linux'), ('LinuC1', 'LinuC1'), ('LPIC1', 'LPIC1'), ('ディープラーニングE資格', 'ディープラーニングE資格'), ('G検定', 'G検定'), ('Python(全般)', 'Python(All)'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Python(Pandas)', 'Python(Pandas)'), ('Python3エンジニア認定基礎試験', 'Python3エンジニア認定基礎試験'), ('Python3エンジニア認定データ分析試験', 'Python3エンジニア認定データ分析試験'), ('Python3エンジニア認定実践試験', 'Python3エンジニア認定実践試験'), ('Javascript(All)', 'Javascript(全般)'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('DATA SCIENTIST', 'データ\u3000サイエンティスト'), ('DATABASE SPECIALIST', 'データベース\u3000スペシャリスト'), ('Bronze 12c SQL基礎', 'Bronze 12c SQL基礎'), ('NETWORK SPECIALIST', 'ネットワークスペシャリスト'), ('AP', '応用情報技術者試験'), ('FE', '基本情報技術者試験'), ('情報セキュリティマネジメント', '情報セキュリティマネジメント'), ('PHP', 'PHP'), ('SEO検定', 'SEO検定'), ('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('統計検定2級', '統計検定2級'), ('統計検定3級', '統計検定3級'), ('statistics', '統計学'), ('簿記2級', '簿記2級'), ('trivia', '雑学'), ('other', 'その他')], max_length=100, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='shoseki',
            field=models.CharField(blank=True, choices=[('キタミ式ITイラスト塾\u3000応用情報技術者\u3000令和03年', 'キタミ式ITイラスト塾\u3000応用情報技術者\u3000令和03年'), ('令和04年【春期】\u3000応用情報技術者\u3000過去問題集', '令和04年【春期】\u3000応用情報技術者\u3000過去問題集'), ('応用情報技術者\u3000試験によくでる問題集【午後】', '応用情報技術者\u3000試験によくでる問題集【午後】'), ('応用情報技術者テキスト&問題集2020年版', '応用情報技術者テキスト&問題集2020年版'), ('LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応', 'LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応'), ('Python3エンジニア認定実践試験Web問題', 'Python3エンジニア認定実践試験Web問題'), ('Python3エンジニア認定データ分析試験Web問題', 'Python3エンジニア認定データ分析試験Web問題'), ('Python3エンジニア認定基礎試験Web問題', 'Python3エンジニア認定基礎試験Web問題'), ('Python3エンジニア認定基礎試験問題集', 'Python3エンジニア認定基礎試験問題集'), ('徹底攻略データサイエンティスト検定リテラシーレベル問題集', '徹底攻略データサイエンティスト検定リテラシーレベル問題集'), ('データベーススペシャリスト教科書令和4年度', 'データベーススペシャリスト教科書令和4年度'), ('Bronze 12c SQL 基礎問題集', 'Bronze 12c SQL 基礎問題集'), ('シェルワンライナー100本ノック', 'シェルワンライナー100本ノック'), ('Access VBA スタンダード', 'Access VBA スタンダード'), ('Access VBA ベーシック', 'Access VBA ベーシック'), ('Excel VBA スタンダード', 'Excel VBA スタンダード'), ('Excel VBA ベーシック', 'Excel VBA ベーシック'), ('統計検定2級\u3000模擬問題集1', '統計検定2級\u3000模擬問題集1'), ('統計検定2級\u3000模擬問題集2', '統計検定2級\u3000模擬問題集2'), ('統計検定2級\u3000模擬問題集3', '統計検定2級\u3000模擬問題集3'), ('基本情報技術者らくらく突破 Python', '基本情報技術者らくらく突破 Python'), ('情報セキュリティマネジメント教科書令和2年度', '情報セキュリティマネジメント教科書令和2年度'), ('LPICレベル1スピードマスター問題集', 'LPICレベル1スピードマスター問題集'), ('ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集', 'ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集'), ('徹底攻略ディープラーニングE資格エンジニア問題集', '徹底攻略ディープラーニングE資格エンジニア問題集')], max_length=100, null=True, verbose_name='書籍'),
        ),
    ]
