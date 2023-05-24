# Generated by Django 4.1.5 on 2023-04-16 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_picturecomment_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他')], max_length=100, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='picturecomment',
            name='category',
            field=models.CharField(choices=[('laugher', '笑い'), ('impressed', '感動'), ('other', 'その他')], max_length=100, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='picturecomment',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='picturecomment',
            name='title',
            field=models.TextField(verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Excel VBA', 'Excel VBA'), ('LINE stickers', 'LINEスタンプ'), ('other', 'その他')], max_length=100, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='text',
            field=models.TextField(verbose_name='コメント'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='thumbnail1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='', verbose_name='画像1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='thumbnail2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像2'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='thumbnail3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像3'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='thumbnail4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像4'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='thumbnail5',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('JAVA', 'JAVA'), ('Linux', 'Linux'), ('LinuC1', 'LinuC1'), ('LPIC1', 'LPIC1'), ('G検定', 'G検定'), ('Python(全般)', 'Python(All)'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Python(Pandas)', 'Python(Pandas)'), ('Python3エンジニア認定基礎試験', 'Python3エンジニア認定基礎試験'), ('Python3エンジニア認定データ分析試験', 'Python3エンジニア認定データ分析試験'), ('Javascript(All)', 'Javascript(全般)'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('DATA SCIENTIST', 'データ\u3000サイエンティスト'), ('DATABASE SPECIALIST', 'データベース\u3000スペシャリスト'), ('Bronze 12c SQL基礎', 'Bronze 12c SQL基礎'), ('NETWORK SPECIALIST', 'ネットワークスペシャリスト'), ('AP', '応用情報技術者試験'), ('FE', '基本情報技術者試験'), ('情報セキュリティマネジメント', '情報セキュリティマネジメント'), ('PHP', 'PHP'), ('SEO検定', 'SEO検定'), ('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('統計検定2級', '統計検定2級'), ('statistics', '統計学'), ('簿記2級', '簿記2級'), ('trivia', '雑学'), ('other', 'その他')], max_length=100, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, null=True, verbose_name='解説'),
        ),
        migrations.AlterField(
            model_name='question',
            name='hint1',
            field=models.TextField(blank=True, null=True, verbose_name='ヒント1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='hint2',
            field=models.TextField(blank=True, null=True, verbose_name='ヒント2'),
        ),
    ]