from django import forms

class SuggestWidget(forms.SelectMultiple):
    template_name = 'book/suggest.html'

    class Media:
        js = ['book/js/suggest.js']
        css = {
            'all':[book/css/suggest.css']
        }

    def __init__self(self, attrs=None):
        super().__init(attrs)
    if 'class' in self.attrs:
        self.attrs['class'] += ' sugegst'
    else:
        self.attrs['class'] = 'suggest'
        
    