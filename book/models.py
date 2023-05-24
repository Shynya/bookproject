from django.db import models

from .consts import MAX_RATE

from django.conf import settings

from django_pandas.io import read_frame

from datetime import datetime
from datetime import date, timedelta

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


CATEGORY = (('business', 'ビジネス'), ('life','生活'),('other','その他'))
CATEGORY2 = (('JAVA', 'JAVA'), ('Linux', 'Linux'), ('LinuC1', 'LinuC1'),('LPIC1', 'LPIC1'),('ディープラーニングE資格', 'ディープラーニングE資格'),('G検定', 'G検定'),('Python(全般)', 'Python(All)'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Python(Pandas)', 'Python(Pandas)'),('Python3エンジニア認定基礎試験', 'Python3エンジニア認定基礎試験'),('Python3エンジニア認定データ分析試験', 'Python3エンジニア認定データ分析試験'),('Python3エンジニア認定実践試験','Python3エンジニア認定実践試験'),('Javascript(All)', 'Javascript(全般)'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('DATA SCIENTIST', 'データ　サイエンティスト'),('DATABASE SPECIALIST', 'データベース　スペシャリスト'),('Bronze 12c SQL基礎', 'Bronze 12c SQL基礎'),('NETWORK SPECIALIST', 'ネットワークスペシャリスト'),('AP', '応用情報技術者試験'),('FE', '基本情報技術者試験'),('情報セキュリティマネジメント', '情報セキュリティマネジメント'),('PHP', 'PHP'), ('SEO検定', 'SEO検定'),('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('統計検定2級', '統計検定2級'), ('統計検定3級', '統計検定3級'),('statistics', '統計学'), ('簿記2級', '簿記2級'),('trivia','雑学'),('other','その他'))
CATEGORY3 = (('Excel VBA','Excel VBA'), ('LINE stickers','LINEスタンプ'),('other', 'その他'))
CATEGORY4 = ( ('laugher','笑い'),('impressed','感動'),('other','その他'))
SHOSEKILIST = (('徹底攻略 Java SE Bronze 問題集','徹底攻略 Java SE Bronze 問題集'),('キタミ式ITイラスト塾　応用情報技術者　令和03年','キタミ式ITイラスト塾　応用情報技術者　令和03年'),('令和04年【春期】　応用情報技術者　過去問題集','令和04年【春期】　応用情報技術者　過去問題集'),('応用情報技術者　試験によくでる問題集【午後】','応用情報技術者　試験によくでる問題集【午後】'),('応用情報技術者テキスト&問題集2020年版','応用情報技術者テキスト&問題集2020年版'),('LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応','LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応'),('Python3エンジニア認定実践試験Web問題','Python3エンジニア認定実践試験Web問題'),('Python3エンジニア認定データ分析試験Web問題','Python3エンジニア認定データ分析試験Web問題'),('Python3エンジニア認定基礎試験Web問題','Python3エンジニア認定基礎試験Web問題'),('Python3エンジニア認定基礎試験問題集','Python3エンジニア認定基礎試験問題集'),('徹底攻略データサイエンティスト検定リテラシーレベル問題集','徹底攻略データサイエンティスト検定リテラシーレベル問題集'),('データベーススペシャリスト教科書令和4年度','データベーススペシャリスト教科書令和4年度'),('Bronze 12c SQL 基礎問題集','Bronze 12c SQL 基礎問題集'),('シェルワンライナー100本ノック','シェルワンライナー100本ノック'),('【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>','【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>'),('Access VBA スタンダード','Access VBA スタンダード'),('Access VBA ベーシック','Access VBA ベーシック'),('Excel VBA スタンダード','Excel VBA スタンダード'),('Excel VBA ベーシック','Excel VBA ベーシック'), ('統計検定2級公式問題集CBT対応板','統計検定2級公式問題集CBT対応板'), ('統計検定2級　模擬問題集1', '統計検定2級　模擬問題集1'), ('統計検定2級　模擬問題集2', '統計検定2級　模擬問題集2'), ('統計検定2級　模擬問題集3', '統計検定2級　模擬問題集3'),('基本情報技術者らくらく突破 Python','基本情報技術者らくらく突破 Python'),('キタミ式ITイラスト塾　基本情報技術者　令和02年','キタミ式ITイラスト塾　基本情報技術者　令和02年'),('情報セキュリティマネジメント教科書令和2年度','情報セキュリティマネジメント教科書令和2年度'),('LPICレベル1スピードマスター問題集','LPICレベル1スピードマスター問題集'),('ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集','ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集'),('徹底攻略ディープラーニングE資格エンジニア問題集', '徹底攻略ディープラーニングE資格エンジニア問題集'),('Linuxコマンド200本ノック','Linuxコマンド200本ノック'),('パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集','パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集'))
CATEGORYCODEMEMO = (('JAVA','JAVA'), ('Python','Python'), ('Jsvascript','Javascript'),('PHP','PHP'), ('HTML,CSS','HTML,CSS'),('SQL','SQL'),('Excel VBA','Excel VBA'), ('Access VBA','Access VBA'),('other', 'その他'))
CATEGORYPOSITION = (('business', 'ビジネス'), ('life','生活'),('other','その他'))

class Book(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=100)
    text = models.TextField(verbose_name="内容")
    thumbnail = models.ImageField(verbose_name="画像", null=True, blank= True)
    category= models.CharField(
        verbose_name="カテゴリ", 
        max_length=100,
        choices = CATEGORY
        )
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.TextField(verbose_name="問題")
    thumbnailQ1 = models.ImageField(verbose_name="画像1 (問題)", null=True, blank= True)
    thumbnailQ2 = models.ImageField(verbose_name="画像2 (問題)", null=True, blank= True)
    thumbnailQ3 = models.ImageField(verbose_name="画像3 (問題)", null=True, blank= True)
    answer = models.TextField(verbose_name="正解")
    wronganswer1 = models.TextField(verbose_name="誤回答1")
    wronganswer2 = models.TextField(verbose_name="誤回答2")
    wronganswer3 = models.TextField(verbose_name="誤回答3")

    #4/17---------------------------------------------------
    wronganswer4 = models.TextField(verbose_name="誤回答4", null=True, blank= True)
    wronganswer5 = models.TextField(verbose_name="誤回答5", null=True, blank= True)
    wronganswer6 = models.TextField(verbose_name="誤回答6", null=True, blank= True)
    wronganswer7 = models.TextField(verbose_name="誤回答7", null=True, blank= True)
    wronganswer8 = models.TextField(verbose_name="誤回答8", null=True, blank= True)
    wronganswer9 = models.TextField(verbose_name="誤回答9", null=True, blank= True)
    #4/17---------------------------------------------------

    explanation = models.TextField(verbose_name="解説", null=True,  blank=True,)
    #thumbnail = models.ImageField(verbose_name="画像", null=True, blank= True)
    thumbnailA1 = models.ImageField(verbose_name="画像1 (正解)", null=True, blank= True)
    thumbnailA2 = models.ImageField(verbose_name="画像2 (正解)", null=True, blank= True)
    thumbnailA3 = models.ImageField(verbose_name="画像3 (正解)", null=True, blank= True)
    hint1 = models.TextField(verbose_name="ヒント1", null=True,  blank=True,)
    hint2 = models.TextField(verbose_name="ヒント2", null=True,  blank=True,)
    category= models.CharField(
        verbose_name="カテゴリ", 
        max_length=100,
        choices = CATEGORY2
        )
    #create_time = models.DateTimeField(default=datetime.now()) 
    #create_day = models.DateTimeField(blank=True, null=True)
    #create_day = models.DateTimeField(auto_now_add=True)
    #create_day = datetime.date.today() 間違い
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    #object_list = Question.objects.all()
    
    #df = read_frame(object_list, fieldnames=['shoseki'])
    #SHOSEKILIST = df

    shoseki= models.CharField(
        verbose_name="書籍",
        max_length=200,
        null=True,  blank=True,
        choices = SHOSEKILIST
    )
    shoseki_page = models.CharField(verbose_name="書籍ページ", max_length=10, null=True,  blank=True,)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Portfolio(models.Model):
    title = models.CharField(verbose_name="タイトル" ,max_length=100)
    text = models.TextField(verbose_name="コメント")
    thumbnail1 = models.ImageField(verbose_name="画像1")
    thumbnail2 = models.ImageField(verbose_name="画像2", null=True, blank= True)
    thumbnail3 = models.ImageField(verbose_name="画像3", null=True, blank= True)
    thumbnail4 = models.ImageField(verbose_name="画像4", null=True, blank= True)
    thumbnail5 = models.ImageField(verbose_name="画像5", null=True, blank= True)
    category= models.CharField(
        verbose_name="カテゴリ", 
        max_length=100,
        choices = CATEGORY3
        )
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Picturecomment(models.Model):
    title = models.TextField(verbose_name="タイトル")
    thumbnail = models.ImageField(verbose_name="画像", null=True, blank= True)
    category= models.CharField(
        verbose_name="カテゴリ", 
        max_length=100,
        choices = CATEGORY4
        )
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Codememo(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=100)
    text = models.TextField(verbose_name="内容")
    category= models.CharField(
        verbose_name="カテゴリ", 
        max_length=100,
        choices = CATEGORYCODEMEMO
        )
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Position(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=100)
    text = models.TextField(verbose_name="内容")
    category= models.CharField(
        verbose_name="カテゴリ", 
        max_length=100,
        choices = CATEGORYPOSITION
        )
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title