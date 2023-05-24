from django import forms
from django.forms import ModelForm
from .models import Question, Portfolio, Picturecomment, Codememo, Position


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','wronganswer4','wronganswer5','wronganswer6','wronganswer7','wronganswer8','wronganswer9','hint1','hint2','explanation', 'category', 'shoseki', 'shoseki_page', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3']
        ### 追加 ###
        widgets = {
            'question': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'answer': forms.Textarea(attrs={'rows':1, 'cols':45}),

            #'thumbnailQ1': forms.Textarea(attrs={'rows':1, 'cols':15}),
            #'thumbnailQ2': forms.Textarea(attrs={'rows':1, 'cols':15}),
            #'thumbnailQ3': forms.Textarea(attrs={'rows':1, 'cols':15}),

            'wronganswer1': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer2': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer3': forms.Textarea(attrs={'rows':1, 'cols':43}),

            'wronganswer4': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer5': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer6': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer7': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer8': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'wronganswer9': forms.Textarea(attrs={'rows':1, 'cols':43}),

            'explanation': forms.Textarea(attrs={'rows':1, 'cols':45}),
            'hint1': forms.Textarea(attrs={'rows':1, 'cols':43}),
            'hint2': forms.Textarea(attrs={'rows':1, 'cols':43}),
            #'category': forms.CharField(attrs={'rows':1, 'cols':43}),
            #'shoseki': forms.CharField(attrs={'rows':1, 'cols':45}),
        }

class FindForm(forms.Form):
        find1 = forms.CharField(label='問題', widget=forms.TextInput(attrs={'class':'form-control1'}),max_length=15, required=False)
        find2 = forms.CharField(label='答え', widget=forms.TextInput(attrs={'class':'form-control2'}),max_length=15,required=False)
        answers = forms.fields.ChoiceField(
            choices = (
              ('','全ての項目'), ('JAVA', 'JAVA'), ('Linux', 'Linux'), ('LinuC1', 'LinuC1'),('LPIC1', 'LPIC1'),('ディープラーニングE資格', 'ディープラーニングE資格'),('G検定', 'G検定'),('Python(全般)', 'Python(All)'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Python(Pandas)', 'Python(Pandas)'),('Python3エンジニア認定基礎試験', 'Python3エンジニア認定基礎試験'),('Python3エンジニア認定データ分析試験', 'Python3エンジニア認定データ分析試験'),('Python3エンジニア認定実践試験','Python3エンジニア認定実践試験'),('Javascript(All)', 'Javascript(全般)'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('DATA SCIENTIST', 'データ　サイエンティスト'),('DATABASE SPECIALIST', 'データベース　スペシャリスト'),('Bronze 12c SQL基礎', 'Bronze 12c SQL基礎'),('NETWORK SPECIALIST', 'ネットワークスペシャリスト'),('AP', '応用情報技術者試験'),('FE', '基本情報技術者試験'),('情報セキュリティマネジメント', '情報セキュリティマネジメント'),('PHP', 'PHP'), ('SEO検定', 'SEO検定'),('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('統計検定2級', '統計検定2級'), ('統計検定3級', '統計検定3級'),('statistics', '統計学'), ('簿記2級', '簿記2級'),('trivia','雑学'),('other','その他'),('other','その他')
            ),
            initial='',
            label='カテゴリ',
            required=False,
            widget=forms.widgets.Select()
        )

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'text', 'thumbnail1', 'thumbnail2', 'thumbnail3', 'thumbnail4', 'thumbnail5','category']
        ### 追加 ###
        widgets = {
            #'title': forms.CharField(attrs={'rows':1, 'cols':35}),
            'text': forms.Textarea(attrs={'rows':1, 'cols':35}),
            
        }
        """
        wronganswer4 = forms.CharField(
            widget=forms.TextInput(
            attrs={
                #'placeholder': 'Username',
                'class': 'class_wronganswer4',
            }
        ))
        wronganswer5 = forms.CharField(
           widget=forms.TextInput(
            attrs={
                #'placeholder': 'Username',
                'class': 'class_wronganswer5',
            }
        ))
        wronganswer6 = forms.CharField(
           widget=forms.TextInput(
            attrs={
                #'placeholder': 'Username',
                'class': 'class_wronganswer6',
            }
        ))
        wronganswer7 = forms.CharField(
            widget=forms.TextInput(
            attrs={
                #'placeholder': 'Username',
                'class': 'class_wronganswer7',
            }
        ))
        wronganswer8 = forms.CharField(
            widget=forms.TextInput(
            attrs={
                #'placeholder': 'Username',
                'class': 'class_wronganswer8',
            }
        ))
        wronganswer9 = forms.CharField(
            widget=forms.TextInput(
            attrs={
                #'placeholder': 'Username',
                'class': 'class_wronganswer9',
            }
        ))
        """

class FindPortfolioForm(forms.Form):
        find1 = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'class':'form-control1'}),max_length=15, required=False)
        find2 = forms.CharField(label='内容', widget=forms.TextInput(attrs={'class':'form-control2'}),max_length=15,required=False)
        answers = forms.fields.ChoiceField(
            choices = (
              ('','全ての項目'), ('Excel VBA','Excel VBA'), ('LINE stickers','LINEスタンプ'),('other', 'その他')
            ),
            initial='',
            label='カテゴリ',
            required=False,
            widget=forms.widgets.Select()
        )

class PicturecommentForm(ModelForm):
    class Meta:
        model = Picturecomment
        fields = ['title', 'thumbnail', 'category']
        ### 追加 ###
        widgets = {
            #'title': forms.CharField(attrs={'rows':1, 'cols':35}),
            'text': forms.Textarea(attrs={'rows':1, 'cols':35}),
            
        }

class FindPicturecommentForm(forms.Form):
        find1 = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'class':'form-control1'}),max_length=15, required=False)
        find2 = forms.CharField(label='内容', widget=forms.TextInput(attrs={'class':'form-control2'}),max_length=15,required=False)
        answers = forms.fields.ChoiceField(
            choices = (
              ('','全ての項目'), ('laugher','笑い'),('impressed','感動'),('other','その他')
            ),
            initial='',
            label='カテゴリ',
            required=False,
            widget=forms.widgets.Select()
        )

class CodememoForm(ModelForm):
    class Meta:
        model = Codememo
        fields = ['title', 'text','category']
        ### 追加 ###
        widgets = {
            #'title': forms.CharField(attrs={'rows':1, 'cols':35}),
            'text': forms.Textarea(attrs={'rows':1, 'cols':60}),
            #'category': forms.Textarea(attrs={'rows':1, 'cols':35}),
            
        }

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['title', 'text','category']
        ### 追加 ###
        widgets = {
            #'title': forms.CharField(attrs={'rows':1, 'cols':35}),
            'text': forms.Textarea(attrs={'rows':1, 'cols':60}),
            #'category': forms.Textarea(attrs={'rows':1, 'cols':35}),
            
        }