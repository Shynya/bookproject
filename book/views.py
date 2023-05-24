from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .consts import ITEM_PER_PAGE

from .models import Book, Review, Question, Portfolio, Picturecomment, Codememo, Position

import random

from .forms import QuestionForm, FindForm, PortfolioForm, FindPortfolioForm, CodememoForm, PositionForm
#from django.views.generic import TemplateView

import os

from django_pandas.io import read_frame

#ストップウォッチ
import time

from datetime import date, timedelta, datetime

#5/3
#from django.views.generic import FormView
#from django.shortcuts import redirect


# Create your views here.

def index_view(request):
    object_list = Book.objects.order_by('-id')

    ranking_list=Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')

    paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)

    return render(
        request,
        'book/index.html',
        {'object_list': object_list, 'ranking_list': ranking_list, 'page_obj': page_obj},
    )

class ListBookView(LoginRequiredMixin, ListView):
    template_name ='book/book_list.html'
    model = Book
    paginated_by = ITEM_PER_PAGE

class DetailBookView(LoginRequiredMixin, DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(LoginRequiredMixin, CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-book')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('book:list-book')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ('title', 'text', 'category', 'thumbnail')
    template_name = 'book/book_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.id})

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        print(context)

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})



#question
"""
def index_view(request):
    object_list = Book.objects.order_by('-id')

    ranking_list=Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')

    paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)

    return render(
        request,
        'book/index.html',
        {'object_list': object_list, 'ranking_list': ranking_list, 'page_obj': page_obj},
    )
"""


#4/13 20
def questionRandom30(request):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        
        #4/13------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    #dataThumbnail = dQ.thumbnail
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Question.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer




    d4allshuf18 = Question.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Question.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Question.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Question.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer


    d4allshuf22 = Question.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Question.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Question.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Question.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Question.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Question.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer

    """
     if dQ.wronganswer4 is not None:
        data22Answer = dataWrongAnswer4
    else:
        d4allshuf22 = Question.objects.get(pk=data4allshuffle[21])
        data22Answer = d4allshuf22.answer 

    if dQ.wronganswer5 is not None:
        data23Answer = dataWrongAnswer5
    else:
        d4allshuf23 = Question.objects.get(pk=data4allshuffle[22])
        data23Answer = d4allshuf23.answer 

    if dQ.wronganswer6 is not None:
        data24Answer = dataWrongAnswer6
    else:
        d4allshuf24 = Question.objects.get(pk=data4allshuffle[23])
        data24Answer = d4allshuf24.answer 
    

    if dQ.wronganswer7 is not None:
        data25Answer = dataWrongAnswer7
    else:
        d4allshuf25 = Question.objects.get(pk=data4allshuffle[24])
        data25Answer = d4allshuf25.answer 

    if dQ.wronganswer8 is not None:
        data26Answer = dataWrongAnswer8
    else:
        d4allshuf26 = Question.objects.get(pk=data4allshuffle[25])
        data26Answer = d4allshuf26.answer 

    if dQ.wronganswer9 is not None:
        data27Answer = dataWrongAnswer9
    else:
        d4allshuf27 = Question.objects.get(pk=data4allshuffle[26])
        data27Answer = d4allshuf27.answer
    """


    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            #'dataThumbnail': dataThumbnail,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,

            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            #'data4allshuffle':data4allshuffle,
    }
    return render(request, 'book/questionRandom_list30.html', params)


#4/9 20
def questionRandom20(request):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        
        
        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3


    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    #dataThumbnail = dQ.thumbnail
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer


    d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
    if dQ.wronganswer4 is str and d4allshuf12.answer != dQ.answer:
        data12Answer = dataWrongAnswer4
    else: 
        data12Answer = d4allshuf12.answer

    d4allshuf13 = Question.objects.get(pk=data4allshuffle[12])
    if dQ.wronganswer5 is str and d4allshuf13.answer != dQ.answer:
        data13Answer = dataWrongAnswer5
    else:
        data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(pk=data4allshuffle[13])
    if dQ.wronganswer6 is str and d4allshuf14.answer != dQ.answer:
        data14Answer = dataWrongAnswer6
    else:
        data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(pk=data4allshuffle[14])
    if dQ.wronganswer7 is str and d4allshuf15.answer != dQ.answer:
        data15Answer = dataWrongAnswer7
    else:
        data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(pk=data4allshuffle[15])
    if dQ.wronganswer8 is str and d4allshuf16.answer != dQ.answer:
        data16Answer = dataWrongAnswer8
    else:
        data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(pk=data4allshuffle[16])
    if dQ.wronganswer9 is str and d4allshuf17.answer != dQ.answer:
        data17Answer = dataWrongAnswer9
    else:
        data17Answer = d4allshuf17.answer

    """
    if dQ.wronganswer4 is not None:
        data12Answer = dataWrongAnswer4
    else: 
        d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
        data12Answer = d4allshuf12.answer

    if dQ.wronganswer5 is not None:
        data13Answer = dataWrongAnswer5
    else:
        d4allshuf13 = Question.objects.get(pk=data4allshuffle[12])
        data13Answer = d4allshuf13.answer 

    if dQ.wronganswer6 is not None:
        data14Answer = dataWrongAnswer6
    else:
        d4allshuf14 = Question.objects.get(pk=data4allshuffle[13])
        data14Answer = d4allshuf14.answer 

    if dQ.wronganswer7 is not None:
        data15Answer = dataWrongAnswer7
    else:
        d4allshuf15 = Question.objects.get(pk=data4allshuffle[14])
        data15Answer = d4allshuf15.answer 

    if dQ.wronganswer8 is not None:
        data16Answer = dataWrongAnswer8
    else:
        d4allshuf16 = Question.objects.get(pk=data4allshuffle[15])
        data16Answer = d4allshuf16.answer 

    if dQ.wronganswer9 is not None:
        data17Answer = dataWrongAnswer9
    else:
        d4allshuf17 = Question.objects.get(pk=data4allshuffle[16])
        data17Answer = d4allshuf17.answer
    """

    data18Answer = dataWrongAnswer1 
    data19Answer = dataWrongAnswer2
    data20Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,20)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            #'dataThumbnail': dataThumbnail,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            #'data4allshuffle':data4allshuffle,
    }
    return render(request, 'book/questionRandom_list20.html', params)


#4/9 10
def questionRandom10(request):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        
        
        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3
    dataExplanation = dQ.explanation
    #dataThumbnail = dQ.thumbnail
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer

    data8Answer = dataWrongAnswer1 

    data9Answer = dataWrongAnswer2

    data10Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,10)


    #d7_1 = Question.objects.get(id=dataAnsList7shuffle[0])
    #d7_1_Answer = d7_1.answer
    d7_1_Answer = dataAnsList7shuffle[0]

    #d7_2 = Question.objects.get(id=dataAnsList7shuffle[1])
    #d7_2_Answer = d7_2.answer
    d7_2_Answer = dataAnsList7shuffle[1]

    #d7_3 = Question.objects.get(id=dataAnsList7shuffle[2])
    #d7_3_Answer = d7_3.answer
    d7_3_Answer = dataAnsList7shuffle[2]

    #d7_4 = Question.objects.get(id=dataAnsList7shuffle[3])
    #d7_4_Answer = d7_4.answer
    d7_4_Answer = dataAnsList7shuffle[3]

    #d7_5 = Question.objects.get(id=dataAnsList7shuffle[4])
    #d7_5_Answer = d7_5.answer
    d7_5_Answer = dataAnsList7shuffle[4]

    #d7_6 = Question.objects.get(id=dataAnsList7shuffle[5])
    #d7_6_Answer = d7_6.answer
    d7_6_Answer = dataAnsList7shuffle[5]

    #d7_7 = Question.objects.get(id=dataAnsList7shuffle[6])
    #d7_7_Answer = d7_7.answer
    d7_7_Answer = dataAnsList7shuffle[6]

    d7_8_Answer = dataAnsList7shuffle[7]

    d7_9_Answer = dataAnsList7shuffle[8]

    d7_10_Answer = dataAnsList7shuffle[9]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            #'dataThumbnail': dataThumbnail,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'data2pk3_1':data2pk3_1,
            #'data4allshuffle':data4allshuffle,
            'object_list':object_list,
    }
    return render(request, 'book/questionRandom_list10.html', params)


#def answerResult10(request):
    ##if (request.method == 'POST'):
    #context = {
    #'selectedAns':request.POST["name1"],
    #'dataAnswer' :request.POST["name0"],
    #'dataExplanation' :request.POST["nameEx"],
    #}
    #selectedAns = request.POST["name1"]
    #dataAnswer = request.POST["name0"]

    #if selectedAns == dataAnswer:

        #return render(
            #request,'book/result_success.html',context
        #)
    #else:
        #return render(
            #request,'book/result_fail.html',context
        #)


def questionRandom(request):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3
    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category

    dataHint1 = dQ.hint1
    dataHint2 = dQ.hint2

    #4/17-------------------------------------------------------------------------------
    data4RegAnswer = [dataAnswer, dataWrongAnswer1, dataWrongAnswer2, dataWrongAnswer3]
    data4RegAnswerShuffle = random.sample(data4RegAnswer, 4)
    data1Answer = data4RegAnswerShuffle[0]
    data2Answer = data4RegAnswerShuffle[1]
    data3Answer = data4RegAnswerShuffle[2]
    data4Answer = data4RegAnswerShuffle[3]
    #-------------------------------------------------------------

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'dataHint1': dataHint1,
            'dataHint2': dataHint2,
            'data1Answer':data1Answer,
            'data2Answer':data2Answer,
            'data3Answer':data3Answer,
            'data4Answer':data4Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'book/questionRandom_list.html', params)


def answerResult(request):
    #if (request.method == 'POST'):
    #else
    object_list = Question.objects.all()
    context = {
    'selectedAns':request.POST["name1"],
    'dataAnswer' :request.POST["name0"],
    'dataQuestion' :request.POST["nameQuestion"],
    'dataExplanation' :request.POST["nameEx"],
    'dataThumbnailQ1' :request.POST["nameThuQ1"],
    'dataThumbnailQ2' :request.POST["nameThuQ2"],
    'dataThumbnailQ3' :request.POST["nameThuQ3"],
    'dataThumbnailA1' :request.POST["nameThuA1"],
    'dataThumbnailA2' :request.POST["nameThuA2"],
    'dataThumbnailA3' :request.POST["nameThuA3"],
    'object_list': object_list,
    'dataNumtaku' :request.POST['nameNumtaku'],
    }
    selectedAns = request.POST["name1"]
    dataAnswer = request.POST["name0"]
    dataQuestion = request.POST["nameQuestion"]
    dataThumbnailQ1 = request.POST["nameThuQ1"]
    dataThumbnailQ2 = request.POST["nameThuQ2"]
    dataThumbnailQ3 = request.POST["nameThuQ3"]
    dataThumbnailA1 = request.POST["nameThuA1"]
    dataThumbnailA2 = request.POST["nameThuA2"]
    dataThumbnailA3 = request.POST["nameThuA3"]
    dataNumtaku = request.POST["nameNumtaku"]
    
    if selectedAns == dataAnswer:

        return render(
            request,'book/result_success.html',context
        )
    else:
        return render(
            request,'book/result_fail.html',context
        )


"""class ListQuestionView(LoginRequiredMixin, ListView):
    object_list = Question.objects.order_by('-id')
    template_name ='book/question_list.html'
    model = Question
    paginated_by = ITEM_PER_PAGE
"""

def ListQuestionView(request):

    data = Question.objects.all().order_by('pk').reverse()
    dataFirst = Question.objects.all().order_by('pk').reverse().first()
    selectColor = ""
    dataFirst1 = ""
    dataFirst2 = ""
    dataFirst3 = ""
    dataFirst1_page = ""
    dataFirst2_page = ""
    dataFirst3_page = ""
    dataFirst1_shoseki = ""
    dataFirst2_shoseki = ""
    dataFirst3_shoseki = ""


    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find1 = request.POST.get('find1')
        find2 = request.POST.get('find2')
        answers = request.POST.get('answers')
        
        
        #data = Question.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,category__contains=answers)
        
        if request.POST.get('nameG'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameG')
        elif request.POST.get('nameLinux'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LPICレベル1スピードマスター問題集"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LPICレベル1スピードマスター問題集").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""      
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameLinux')
        elif request.POST.get('nameSQL'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Bronze 12c SQL 基礎問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Bronze 12c SQL 基礎問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki           
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            #selectColor = request.POST.get('nameSQL')
            selectColor = "sqlBronze"
        
        elif request.POST.get('namePython3D'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定データ分析試験Web問題"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定データ分析試験Web問題").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('namePython3D')
        elif request.POST.get('nameAccessVBA'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Access VBA"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Access VBA").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki

            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameAccessVBA')
        elif request.POST.get('nameToukei'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集1"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集1").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集2"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集2").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級公式問題集CBT対応板"):
                dataFirst3 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級公式問題集CBT対応板").first()
                dataFirst3_page = dataFirst3.shoseki_page
                dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = request.POST.get('nameToukei')
        elif request.POST.get('namePython3'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験Web問題"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験Web問題").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験問題集"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験問題集").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('namePython3')
        elif request.POST.get('nameDBS'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="データベーススペシャリスト教科書令和4年度"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="データベーススペシャリスト教科書令和4年度").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameDBS')
        elif request.POST.get('nameOuyou'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　応用情報技術者　令和03年"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　応用情報技術者　令和03年").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="令和04年【春期】　応用情報技術者　過去問題集"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="令和04年【春期】　応用情報技術者　過去問題集").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="応用情報技術者　試験によくでる問題集【午後】"):
                dataFirst3 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="応用情報技術者　試験によくでる問題集【午後】").first()
                dataFirst3_page = dataFirst3.shoseki_page
                dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = request.POST.get('nameOuyou')
        
        #5/6
        elif request.POST.get('nameKihon'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　基本情報技術者　令和02年"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　基本情報技術者　令和02年").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameKihon')
        
        elif request.POST.get('namePython3Jissen'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定実践試験Web問題"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定実践試験Web問題").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('namePython3Jissen')
        elif request.POST.get('nameDataScientist'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略データサイエンティスト検定リテラシーレベル問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略データサイエンティスト検定リテラシーレベル問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameDataScientist')
        elif request.POST.get('nameEshikaku'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略ディープラーニングE資格エンジニア問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略ディープラーニングE資格エンジニア問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameEshikaku')

        elif request.POST.get('nameBoki2'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                

            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            #selectColor = request.POST.get('nameBoki2')
            selectColor = "javaBronze"
            
        elif request.POST.get('nameJava'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="- [ ] 徹底攻略 Java SE Bronze 問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="- [ ] 徹底攻略 Java SE Bronze 問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki

            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.POST.get('nameJava')
            
        elif request.POST.get('nameFind'):
            data = Question.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,category__contains=answers)
            dataFirst1 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = dataFirst1.shoseki_page
            dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = dataFirst2.shoseki_page
            dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = dataFirst3.shoseki_page
            dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = ""
        else:
            dataFirst1 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = ""
            dataFirst1_shoseki = ""
            dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = ""

        #today = date.today()
        #today = date.today().strftime('%Y/%m/%d')
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        #dateFormat = Question.created_at.strftime('%Y/%m/%d')
    else:
        #msg = 'search words...'
        form = FindForm()
        data = Question.objects.all().order_by('pk').reverse()
        #dataKoujun = Question.objects.order_by('pk').reverse()
        #dataKoujun = Question.objects.all().order_by('id').reverse()
        dataFirst1 = ""
        dataFirst2 = ""
        dataFirst3 = ""
        dataFirst1_page = ""
        dataFirst2_page = ""
        dataFirst3_page = ""
        
        #today = datetime.now()
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        #today = datetime.now().replace(hour=00, minute=0)

        #today = today - today.time()

        #strToday = str(datetime.now())
        #strTodayNoTime = str(today)

        #today = date.today().strftime('%Y/%m/%d')
        #dataKoujun = data
        #dateFormat = created_at.strftime('%Y/%m/%d')

    databaseSpecialistCount = Question.objects.filter(shoseki__icontains="データベーススペシャリスト教科書令和4年度", created_at__range=[today, datetime.now()]).count()
    accessVBACount = Question.objects.filter(shoseki__icontains="Access VBA スタンダード", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>", created_at__range=[today, datetime.now()]).count()
    ouyoujouhouCount = Question.objects.filter(shoseki__icontains="令和04年【春期】　応用情報技術者　過去問題集", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="応用情報技術者テキスト&問題集2020年版", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="キタミ式ITイラスト塾　応用情報技術者　令和03年", created_at__range=[today, datetime.now()]).count()
    kihonjouhouCount = Question.objects.filter(shoseki__icontains="キタミ式ITイラスト塾　基本情報技術者　令和02年", created_at__range=[today, datetime.now()]).count()
    toukeikenteiCount = Question.objects.filter(shoseki__icontains="統計検定2級　模擬問題集1", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="統計検定2級公式問題集CBT対応板", created_at__range=[today, datetime.now()]).count()

    python3Count = Question.objects.filter(shoseki__icontains="Python3エンジニア認定基礎試験問題集", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="Python3エンジニア認定基礎試験Web問題", created_at__range=[today, datetime.now()]).count()
    
    sqlCount = Question.objects.filter(shoseki__icontains="Bronze 12c SQL 基礎問題集", created_at__range=[today, datetime.now()]).count()
    python3JissenCount = Question.objects.filter(shoseki__icontains="Python3エンジニア認定実践試験Web問題", created_at__range=[today, datetime.now()]).count()
    python3dataBunsekiCount = Question.objects.filter(shoseki__icontains="Python3エンジニア認定データ分析試験Web問題", created_at__range=[today, datetime.now()]).count()
    gkenteiCount = Question.objects.filter(shoseki__icontains="ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集", created_at__range=[today, datetime.now()]).count()
    linuxCount = Question.objects.filter(shoseki__icontains="LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="LPICレベル1スピードマスター問題集", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="シェルワンライナー100本ノック", created_at__range=[today, datetime.now()]).count()
    
    
    dataScientistCount = Question.objects.filter(shoseki__icontains="徹底攻略データサイエンティスト検定リテラシーレベル問題集", created_at__range=[today, datetime.now()]).count()
    eShikakuCount = Question.objects.filter(shoseki__icontains="徹底攻略ディープラーニングE資格エンジニア問題集", created_at__range=[today, datetime.now()]).count()
    boki2Count  = Question.objects.filter(shoseki__icontains="パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集", created_at__range=[today, datetime.now()]).count()
    javaCount  = Question.objects.filter(shoseki__icontains="徹底攻略 Java SE Bronze 問題集", created_at__range=[today, datetime.now()]).count()

    params = {
            'title': '',
            #'message': msg,
            'form': form,
            'data': data,
            'dataFirst': dataFirst,
            'dataFirst1': dataFirst1,
            'dataFirst2': dataFirst2,
            'dataFirst3': dataFirst3,
            'dataFirst1_page': dataFirst1_page,
            'dataFirst2_page': dataFirst2_page,
            'dataFirst3_page': dataFirst3_page,
            'dataFirst1_shoseki': dataFirst1_shoseki,
            'dataFirst2_shoseki': dataFirst2_shoseki,
            'dataFirst3_shoseki': dataFirst3_shoseki,
            'today': today,
            #'dateFormat': dateFormat,
            'databaseSpecialistCount': databaseSpecialistCount,
            'accessVBACount': accessVBACount,
            'ouyoujouhouCount': ouyoujouhouCount,
            'kihonjouhouCount': kihonjouhouCount,
            'toukeikenteiCount': toukeikenteiCount,
            'python3Count': python3Count,
            'sqlCount': sqlCount,
            'python3JissenCount':python3JissenCount,
            'python3dataBunsekiCount': python3dataBunsekiCount,
            'gkenteiCount': gkenteiCount,
            'linuxCount': linuxCount,
            'dataScientistCount': dataScientistCount,
            'selectColor': selectColor,
            'eShikakuCount': eShikakuCount,
            'boki2Count': boki2Count,
            'javaCount': javaCount

    }
    return render(request, 'book/question_list.html', params)

"""
class ListQuestionView(LoginRequiredMixin, ListView):
    #form_class = FindForm
    template_name ='book/question_list.html'
    model = Question
    #paginated_by = ITEM_PER_PAGE
"""

#class EachQuestionView(LoginRequiredMixin, DetailView):
def EachQuestionView30(request, pk):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        #data = random.sample(pks_list,1)
        #data = list(pk)
        data = [pk]

        #pks_list = list('pk')
        

        #4/9------------------
        #pks_list.remove(data[0])
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        #data = random.sample(pks_list,1)
        #data = list(pk)
        data = [pk]

        #pks_list = list('pk')

        
        #4/13------------------
        #pks_list.remove(data[0])
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    dQ = Question.objects.get(pk=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9


    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category

    
    d4allshuf1 = Question.objects.get(pk=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(pk=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(pk=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(pk=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(pk=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(pk=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(pk=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(pk=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(pk=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(pk=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(pk=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Question.objects.get(pk=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Question.objects.get(pk=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(pk=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(pk=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(pk=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(pk=data4allshuffle[16])
    data17Answer = d4allshuf17.answer


    d4allshuf18 = Question.objects.get(pk=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Question.objects.get(pk=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Question.objects.get(pk=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    
    d4allshuf21 = Question.objects.get(pk=data4allshuffle[20])
    data21Answer = d4allshuf21.answer


    d4allshuf22 = Question.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Question.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Question.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Question.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Question.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Question.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer


    """
    if dQ.wronganswer4 is not None:
        data22Answer = dataWrongAnswer4
    else:
        d4allshuf22 = Question.objects.get(pk=data4allshuffle[21])
        data22Answer = d4allshuf22.answer 

    if dQ.wronganswer5 is not None:
        data23Answer = dataWrongAnswer5
    else:
        d4allshuf23 = Question.objects.get(pk=data4allshuffle[22])
        data23Answer = d4allshuf23.answer 

    if dQ.wronganswer6 is not None:
        data24Answer = dataWrongAnswer6
    else:
        d4allshuf24 = Question.objects.get(pk=data4allshuffle[23])
        data24Answer = d4allshuf24.answer 

    if dQ.wronganswer7 is not None:
        data25Answer = dataWrongAnswer7
    else:
        d4allshuf25 = Question.objects.get(pk=data4allshuffle[24])
        data25Answer = d4allshuf25.answer 

    if dQ.wronganswer8 is not None:
        data26Answer = dataWrongAnswer8
    else:
        d4allshuf26 = Question.objects.get(pk=data4allshuffle[25])
        data26Answer = d4allshuf26.answer 

    if dQ.wronganswer9 is not None:
        data27Answer = dataWrongAnswer9
    else:
        d4allshuf27 = Question.objects.get(pk=data4allshuffle[26])
        data27Answer = d4allshuf27.answer
    """

    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            #'dataThumbnail': dataThumbnail,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,

            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            #'data4allshuffle':data4allshuffle,
    }
    return render(request, 'book/questionEach_list30.html', params)

def EachQuestionView20(request, pk):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        
        
        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3


    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 


    d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
    if dQ.wronganswer4 is str and d4allshuf12.answer != dQ.answer:
        data12Answer = dataWrongAnswer4
    else: 
        data12Answer = d4allshuf12.answer

    d4allshuf13 = Question.objects.get(pk=data4allshuffle[12])
    if dQ.wronganswer5 is str and d4allshuf13.answer != dQ.answer:
        data13Answer = dataWrongAnswer5
    else:
        data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(pk=data4allshuffle[13])
    if dQ.wronganswer6 is str and d4allshuf14.answer != dQ.answer:
        data14Answer = dataWrongAnswer6
    else:
        data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(pk=data4allshuffle[14])
    if dQ.wronganswer7 is str and d4allshuf15.answer != dQ.answer:
        data15Answer = dataWrongAnswer7
    else:
        data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(pk=data4allshuffle[15])
    if dQ.wronganswer8 is str and d4allshuf16.answer != dQ.answer:
        data16Answer = dataWrongAnswer8
    else:
        data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(pk=data4allshuffle[16])
    if dQ.wronganswer9 is str and d4allshuf17.answer != dQ.answer:
        data17Answer = dataWrongAnswer9
    else:
        data17Answer = d4allshuf17.answer

    data18Answer = dataWrongAnswer1 
    data19Answer = dataWrongAnswer2
    data20Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,20)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            #'data4allshuffle':data4allshuffle,
    }
    return render(request, 'book/questionEach_list20.html', params)

def EachQuestionView10(request, pk):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3
    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer

    data8Answer = dataWrongAnswer1 

    data9Answer = dataWrongAnswer2

    data10Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,10)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'book/questionEach_list10.html', params)

def EachQuestionView(request, pk):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]
        dataafter = Question.objects.filter(pk__in=data)

        data2 = Question.objects.order_by('?')[:3]
        data2after = Question.objects.filter(pk__in=data2)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)
        #---------------------

        data3 = dataafter | data2after
        data3_list = list(data3)
        if len(data3_list) == 4:
            data3_listtemp = random.sample(data3_list,4)
        else:

            dataadd = Question.objects.order_by('?')[:1]
            dataaddafter =  Question.objects.filter(pk__in=dataadd)
            data3 = data3 | dataaddafter
            data3_list = list(data3)

            if len(data3_list) == 4:
                data3_listtemp = random.sample(data3_list,4)
            else:
                dataadd = Question.objects.order_by('?')[:1]
                dataaddafter =  Question.objects.filter(pk__in=dataadd)
                data3 = data3 | dataaddafter
                data3_list = list(data3)

                if len(data3_list) == 4:
                    data3_listtemp = random.sample(data3_list,4)
                else:
                    dataadd = Question.objects.order_by('?')[:1]
                    dataaddafter =  Question.objects.filter(pk__in=dataadd)
                    data3 = data3 | dataaddafter
                    data3_list = list(data3)

                    if len(data3_list) == 3:
                        data3_listtemp = random.sample(data3_list,3)
                    else:
                        data3_listtemp = random.sample(data3_list,4)

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]
        dataafter = Question.objects.filter(pk__in=data)

        data2 = Question.objects.order_by('?')[:3]
        data2after = Question.objects.filter(pk__in=data2)

        #4/9------------------
        pks_list.remove(data[0])
        
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)
        #---------------------

        data3 = dataafter | data2after
        data3_list = list(data3)
        if len(data3_list) == 4:
            data3_listtemp = random.sample(data3_list,4)
        else:

            dataadd = Question.objects.order_by('?')[:1]
            dataaddafter =  Question.objects.filter(pk__in=dataadd)
            data3 = data3 | dataaddafter
            data3_list = list(data3)

            if len(data3_list) == 4:
                data3_listtemp = random.sample(data3_list,4)
            else:
                dataadd = Question.objects.order_by('?')[:1]
                dataaddafter =  Question.objects.filter(pk__in=dataadd)
                data3 = data3 | dataaddafter
                data3_list = list(data3)

                if len(data3_list) == 4:
                    data3_listtemp = random.sample(data3_list,4)
                else:
                    dataadd = Question.objects.order_by('?')[:1]
                    dataaddafter =  Question.objects.filter(pk__in=dataadd)
                    data3 = data3 | dataaddafter
                    data3_list = list(data3)

                    if len(data3_list) == 3:
                        data3_listtemp = random.sample(data3_list,3)
                    else:
                        data3_listtemp = random.sample(data3_list,4)

        data4 = Question.objects.filter(answer__in=data3_listtemp)

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category

    dataHint1 = dQ.hint1
    dataHint2 = dQ.hint2

    """4/17
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer
    """

    #4/17-------------------------------------------------------------------------------
    data4RegAnswer = [dataAnswer, dataWrongAnswer1, dataWrongAnswer2, dataWrongAnswer3]   
    data4RegAnswerShuffle = random.sample(data4RegAnswer, 4)
    data1Answer = data4RegAnswerShuffle[0]
    data2Answer = data4RegAnswerShuffle[1]
    data3Answer = data4RegAnswerShuffle[2]
    data4Answer = data4RegAnswerShuffle[3]
    #-------------------------------------------------------------

    params = {
            'data': data,
            'data2': data2,
            'dataafter': dataafter,
            'data4': data4,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'dataHint1': dataHint1,
            'dataHint2': dataHint2,
            'data1Answer':data1Answer,
            'data2Answer':data2Answer,
            'data3Answer':data3Answer,
            'data4Answer':data4Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'book/questionEach_list.html', params)

def testQuestionView(request):

    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find1 = request.POST.get('find1')
        find2 = request.POST.get('find2')
        answers = request.POST.get('answers')
        data = Question.objects.filter(question__contains=find1,answer__contains=find2,category__contains=answers)
        #msg = 'Result: ' + str(data.count())
    else:
        #msg = 'search words...'
        form = FindForm()
        data = Question.objects.all().order_by('pk').reverse()
    params = {
            'title': '',
            #'message': msg,
            'form': form,
            'data': data,
    }
    return render(request, 'book/question_test.html', params)


#4/18
def questionRandom50(request):
    object_list = Question.objects.all()
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        
        #4/13------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation

    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Question.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer


    d4allshuf18 = Question.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Question.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Question.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Question.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer



    d4allshuf22 = Question.objects.get(id=data4allshuffle[21])
    data22Answer = d4allshuf22.answer

    d4allshuf23 = Question.objects.get(id=data4allshuffle[22])
    data23Answer = d4allshuf23.answer

    d4allshuf24 = Question.objects.get(id=data4allshuffle[23])
    data24Answer = d4allshuf24.answer

    d4allshuf25 = Question.objects.get(id=data4allshuffle[24])
    data25Answer = d4allshuf25.answer

    d4allshuf26 = Question.objects.get(id=data4allshuffle[25])
    data26Answer = d4allshuf26.answer

    d4allshuf27 = Question.objects.get(id=data4allshuffle[26])
    data27Answer = d4allshuf27.answer

    d4allshuf28 = Question.objects.get(id=data4allshuffle[27])
    data28Answer = d4allshuf28.answer

    d4allshuf29 = Question.objects.get(id=data4allshuffle[28])
    data29Answer = d4allshuf29.answer

    d4allshuf30 = Question.objects.get(id=data4allshuffle[29])
    data30Answer = d4allshuf30.answer

    d4allshuf31 = Question.objects.get(id=data4allshuffle[30])
    data31Answer = d4allshuf31.answer

    d4allshuf32 = Question.objects.get(id=data4allshuffle[31])
    data32Answer = d4allshuf32.answer

    d4allshuf33 = Question.objects.get(id=data4allshuffle[32])
    data33Answer = d4allshuf33.answer

    d4allshuf34 = Question.objects.get(id=data4allshuffle[33])
    data34Answer = d4allshuf34.answer

    d4allshuf35 = Question.objects.get(id=data4allshuffle[34])
    data35Answer = d4allshuf35.answer

    d4allshuf36 = Question.objects.get(id=data4allshuffle[35])
    data36Answer = d4allshuf36.answer

    d4allshuf37 = Question.objects.get(id=data4allshuffle[36])
    data37Answer = d4allshuf37.answer

    d4allshuf38 = Question.objects.get(id=data4allshuffle[37])
    data38Answer = d4allshuf38.answer

    d4allshuf39 = Question.objects.get(id=data4allshuffle[38])
    data39Answer = d4allshuf39.answer

    d4allshuf40 = Question.objects.get(id=data4allshuffle[39])
    data40Answer = d4allshuf40.answer

    d4allshuf41 = Question.objects.get(id=data4allshuffle[40])
    data41Answer = d4allshuf41.answer



    d4allshuf42 = Question.objects.get(pk=data4allshuffle[41])
    if dQ.wronganswer4 is str and d4allshuf42.answer != dQ.answer:
        data42Answer = dataWrongAnswer4
    else:   
        data42Answer = d4allshuf42.answer

    d4allshuf43 = Question.objects.get(pk=data4allshuffle[42])
    if dQ.wronganswer5 is str and d4allshuf43.answer != dQ.answer:
        data43Answer = dataWrongAnswer5
    else:
        data43Answer = d4allshuf43.answer 

    d4allshuf44 = Question.objects.get(pk=data4allshuffle[43])
    if dQ.wronganswer6 is str and d4allshuf44.answer != dQ.answer:
        data44Answer = dataWrongAnswer6
    else:
        data44Answer = d4allshuf44.answer 

    d4allshuf45 = Question.objects.get(pk=data4allshuffle[44])
    if dQ.wronganswer7 is str and d4allshuf45.answer != dQ.answer:
        data45Answer = dataWrongAnswer7
    else:
        data45Answer = d4allshuf45.answer 

    d4allshuf46 = Question.objects.get(pk=data4allshuffle[45])
    if dQ.wronganswer8 is str and d4allshuf46.answer != dQ.answer:
        data46Answer = dataWrongAnswer8
    else:
        data46Answer = d4allshuf46.answer 

    d4allshuf47 = Question.objects.get(pk=data4allshuffle[46])
    if dQ.wronganswer9 is str and d4allshuf47.answer != dQ.answer:
        data47Answer = dataWrongAnswer9
    else:     
        data47Answer = d4allshuf47.answer

    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            #'dataThumbnail': dataThumbnail,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,

            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            #'data4allshuffle':data4allshuffle,
    }
    return render(request, 'book/questionRandom_list50.html', params)

def testQuestionView50(request):
    object_list = Question.objects.all()
    
    test50count = request.POST["test50count"]
    test50seikai = request.POST["test50seikai"]
    testShokai = request.POST["testShokai"]

    if testShokai != 'testShokai':
        context = {
            'test50count' :request.POST["test50count"],
            'test50seikai' :request.POST["test50seikai"],
            'testShokai' :request.POST["testShokai"],
            'selectedAns' :request.POST["name1"],
            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            'dataThumbnailQ1' :request.POST["nameThuQ1"],
            'dataThumbnailQ2' :request.POST["nameThuQ2"],
            'dataThumbnailQ3' :request.POST["nameThuQ3"],
            'dataThumbnailA1' :request.POST["nameThuA1"],
            'dataThumbnailA2' :request.POST["nameThuA2"],
            'dataThumbnailA3' :request.POST["nameThuA3"],
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],
            'testId11':request.POST['testId11'],
            'testId12':request.POST['testId12'],
            'testId13':request.POST['testId13'],
            'testId14':request.POST['testId14'],
            'testId15':request.POST['testId15'],
            'testId16':request.POST['testId16'],
            'testId17':request.POST['testId17'],
            'testId18':request.POST['testId18'],
            'testId19':request.POST['testId19'],
            'testId20':request.POST['testId20'],
            'testId21':request.POST['testId21'],
            'testId22':request.POST['testId22'],
            'testId23':request.POST['testId23'],
            'testId24':request.POST['testId24'],
            'testId25':request.POST['testId25'],
            'testId26':request.POST['testId26'],
            'testId27':request.POST['testId27'],
            'testId28':request.POST['testId28'],
            'testId29':request.POST['testId29'],
            'testId30':request.POST['testId30'],
            'testId31':request.POST['testId31'],
            'testId32':request.POST['testId32'],
            'testId33':request.POST['testId33'],
            'testId34':request.POST['testId34'],
            'testId35':request.POST['testId35'],
            'testId36':request.POST['testId36'],
            'testId37':request.POST['testId37'],
            'testId38':request.POST['testId38'],
            'testId39':request.POST['testId39'],
            'testId40':request.POST['testId40'],
            'testId41':request.POST['testId41'],
            'testId42':request.POST['testId42'],
            'testId43':request.POST['testId43'],
            'testId44':request.POST['testId44'],
            'testId45':request.POST['testId45'],
            'testId46':request.POST['testId46'],
            'testId47':request.POST['testId47'],
            'testId48':request.POST['testId48'],
            'testId49':request.POST['testId49'],
            'testId50':request.POST['testId50'],
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test50count = request.POST['test50count']
        test50seikai = request.POST['test50seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']
        testId11 = request.POST['testId11']
        testId12 = request.POST['testId12']
        testId13 = request.POST['testId13']
        testId14 = request.POST['testId14']
        testId15 = request.POST['testId15']
        testId16 = request.POST['testId16']
        testId17 = request.POST['testId17']
        testId18 = request.POST['testId18']
        testId19 = request.POST['testId19']
        testId20 = request.POST['testId20']
        testId21 = request.POST['testId21']
        testId22 = request.POST['testId22']
        testId23 = request.POST['testId23']
        testId24 = request.POST['testId24']
        testId25 = request.POST['testId25']
        testId26 = request.POST['testId26']
        testId27 = request.POST['testId27']
        testId28 = request.POST['testId28']
        testId29 = request.POST['testId29']
        testId30 = request.POST['testId30']
        testId31 = request.POST['testId31']
        testId32 = request.POST['testId32']
        testId33 = request.POST['testId33']
        testId34 = request.POST['testId34']
        testId35 = request.POST['testId35']
        testId36 = request.POST['testId36']
        testId37 = request.POST['testId37']
        testId38 = request.POST['testId38']
        testId39 = request.POST['testId39']
        testId40 = request.POST['testId40']
        testId41 = request.POST['testId41']
        testId42 = request.POST['testId42']
        testId43 = request.POST['testId43']
        testId44 = request.POST['testId44']
        testId45 = request.POST['testId45']
        testId46 = request.POST['testId46']
        testId47 = request.POST['testId47']
        testId48 = request.POST['testId48']
        testId49 = request.POST['testId49']
        testId50 = request.POST['testId50']
    else:
        context = {
            'test50count':request.POST["test50count"],
            'test50seikai':request.POST["test50seikai"],
        }
        selectedAns = "shokaihanai"

    test50count = int(test50count)
    test50count += 1

    test50seikai = int(test50seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test50seikai += 1
    
    
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)
   
        #4/13------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3
    dataCategory = dQ.category
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Question.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer

    d4allshuf18 = Question.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Question.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Question.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Question.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer

    d4allshuf22 = Question.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Question.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Question.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Question.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Question.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Question.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer


    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]
    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    test50mondaisuu = 3
        
    seikairitsuFloat = (float(test50seikai) / float(test50mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    #4/19 django-pandas----------------------------------
    df = read_frame(object_list, fieldnames=['answer'])
    #----------------------------------------------------

    dQID = data[0]
    if test50count == 0:
        testId1 = 777
    if test50count <= 1:
        testId2 = 777
    if test50count <= 2:
        testId3 = 777
    if test50count <= 3:
        testId4 = 7777
    if test50count <= 4:
        testId5 = 7777
    if test50count <= 5:
        testId6 = 7777
    if test50count <= 6:
        testId7 = 7777
    if test50count <= 7:
        testId8 = 7777
    if test50count <= 8:
        testId9 = 7777
    if test50count <= 9:
        testId10 = 7777
    if test50count <= 10:
        testId11 = 7777
    if test50count <= 11:
        testId12 = 7777
    if test50count <= 12:
        testId13 = 7777
    if test50count <= 13:
        testId14 = 7777
    if test50count <= 14:
        testId15 = 7777
    if test50count <= 15:
        testId16 = 7777
    if test50count <= 16:
        testId17 = 7777
    if test50count <= 17:
        testId18 = 7777
    if test50count <= 18:
        testId19 = 7777
    if test50count <= 19:
        testId20 = 7777 
    if test50count <= 20:
        testId21 = 7777
    if test50count <= 21:
        testId22 = 7777
    if test50count <= 22:
        testId23 = 7777
    if test50count <= 23:
        testId24 = 7777
    if test50count <= 24:
        testId25 = 7777
    if test50count <= 25:
        testId26 = 7777
    if test50count <= 26:
        testId27 = 7777
    if test50count <= 27:
        testId28 = 7777
    if test50count <= 28:
        testId29 = 7777
    if test50count <= 29:
        testId30 = 7777
    if test50count <= 30:
        testId31 = 7777
    if test50count <= 31:
        testId32 = 7777
    if test50count <= 32:
        testId33 = 7777
    if test50count <= 33:
        testId34 = 7777
    if test50count <= 34:
        testId35 = 7777
    if test50count <= 35:
        testId36 = 7777
    if test50count <= 36:
        testId37 = 7777
    if test50count <= 37:
        testId38 = 7777
    if test50count <= 38:
        testId39 = 7777
    if test50count <= 39:
        testId40 = 7777 
    if test50count <= 40:
        testId41 = 7777
    if test50count <= 41:
        testId42 = 7777
    if test50count <= 42:
        testId43 = 7777
    if test50count <= 43:
        testId44 = 7777
    if test50count <= 44:
        testId45 = 7777
    if test50count <= 45:
        testId46 = 7777
    if test50count <= 46:
        testId47 = 7777
    if test50count <= 47:
        testId48 = 7777
    if test50count <= 48:
        testId49 = 7777
    if test50count <= 49:
        testId50 = 7777 
    if test50count <= 50:
        testId50 = 7777 
    if test50count == 1:
        testId1 = dQID
    if test50count == 2:
        testId2 = dQID
    if test50count == 3:
        testId3 = dQID
    if test50count == 4:
        testId4 = dQID
    if test50count == 5:
        testId5 = dQID
    if test50count == 6:
        testId6 = dQID
    if test50count == 7:
        testId7 = dQID
    if test50count == 8:
        testId8 = dQID
    if test50count == 9:
        testId9 = dQID
    if test50count == 10:
        testId10 = dQID
    if test50count == 11:
        testId11 = dQID
    if test50count == 12:
        testId12 = dQID
    if test50count == 13:
        testId13 = dQID
    if test50count == 14:
        testId14 = dQID
    if test50count == 15:
        testId15 = dQID
    if test50count == 16:
        testId16 = dQID
    if test50count == 17:
        testId17 = dQID
    if test50count == 18:
        testId18 = dQID
    if test50count == 19:
        testId19 = dQID
    if test50count == 20:
        testId20 = dQID
    if test50count == 21:
        testId21 = dQID
    if test50count == 22:
        testId22 = dQID
    if test50count == 23:
        testId23 = dQID
    if test50count == 24:
        testId24 = dQID
    if test50count == 25:
        testId25 = dQID
    if test50count == 26:
        testId26 = dQID
    if test50count == 27:
        testId27 = dQID
    if test50count == 28:
        testId28 = dQID
    if test50count == 29:
        testId29 = dQID
    if test50count == 30:
        testId30 = dQID 
    if test50count == 31:
        testId31 = dQID
    if test50count >= 32:
        testId32 = dQID
    if test50count == 33:
        testId33 = dQID
    if test50count == 34:
        testId34 = dQID
    if test50count == 35:
        testId35 = dQID
    if test50count == 36:
        testId36 = dQID
    if test50count == 37:
        testId37 = dQID
    if test50count == 38:
        testId38 = dQID
    if test50count == 39:
        testId39 = dQID
    if test50count == 40:
        testId40 = dQID
    if test50count == 41:
        testId41 = dQID
    if test50count == 42:
        testId42 = dQID
    if test50count == 43:
        testId43 = dQID
    if test50count == 44:
        testId44 = dQID
    if test50count == 45:
        testId45 = dQID
    if test50count == 46:
        testId46 = dQID
    if test50count == 47:
        testId47 = dQID
    if test50count == 48:
        testId48 = dQID
    if test50count == 49:
        testId49 = dQID
    if test50count == 50:
        testId50 = dQID   

    testId = dQID
    
    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            'test50count':test50count,
            'test50seikai':test50seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test50mondaisuu':test50mondaisuu,
            'selectedAns':selectedAns,
            'df':df,
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId11':testId11,
            'testId12':testId12,
            'testId13':testId13,
            'testId14':testId14,
            'testId15':testId15,
            'testId16':testId16,
            'testId17':testId17,
            'testId18':testId18,
            'testId19':testId19,
            'testId20':testId20,
            'testId21':testId21,
            'testId22':testId22,
            'testId23':testId23,
            'testId24':testId24,
            'testId25':testId25,
            'testId26':testId26,
            'testId27':testId27,
            'testId28':testId28,
            'testId29':testId29,
            'testId30':testId30,
            'testId31':testId31,
            'testId32':testId32,
            'testId33':testId33,
            'testId34':testId34,
            'testId35':testId35,
            'testId36':testId36,
            'testId37':testId37,
            'testId38':testId38,
            'testId39':testId39,
            'testId40':testId40,
            'testId41':testId41,
            'testId42':testId42,
            'testId43':testId43,
            'testId44':testId44,
            'testId45':testId45,
            'testId46':testId46,
            'testId47':testId47,
            'testId48':testId48,
            'testId49':testId49,
            'testId50':testId50,
            'testId':testId,
    }

    if test50count == test50mondaisuu + 1 :
        return render(request, 'book/question_test_result50.html', params)
    else:
        return render(request, 'book/question_test50.html', params)

#4/20
def testQuestionView10(request):

    object_list = Question.objects.all()
    
    test10count = request.POST["test10count"]
    test10seikai = request.POST["test10seikai"]
    testShokai = request.POST["testShokai"]

    if testShokai != 'testShokai':
        context = {
            'test10count' :request.POST["test10count"],
            'test10seikai' :request.POST["test10seikai"],
            'testShokai' :request.POST["testShokai"],
            'selectedAns' :request.POST["name1"],
            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            'dataThumbnailQ1' :request.POST["nameThuQ1"],
            'dataThumbnailQ2' :request.POST["nameThuQ2"],
            'dataThumbnailQ3' :request.POST["nameThuQ3"],
            'dataThumbnailA1' :request.POST["nameThuA1"],
            'dataThumbnailA2' :request.POST["nameThuA2"],
            'dataThumbnailA3' :request.POST["nameThuA3"],
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],

            'testQuestion1' :request.POST['testQuestion1'],
            'testQuestion2' :request.POST['testQuestion2'],
            'testQuestion3' :request.POST['testQuestion3'],
            'testQuestion4':request.POST['testQuestion4'],
            'testQuestion5':request.POST['testQuestion5'],
            'testQuestion6':request.POST['testQuestion6'],
            'testQuestion7':request.POST['testQuestion7'],
            'testQuestion8':request.POST['testQuestion8'],
            'testQuestion9':request.POST['testQuestion9'],
            'testQuestion10':request.POST['testQuestion10'],

            'testAnswer1' :request.POST['testAnswer1'],
            'testAnswer2' :request.POST['testAnswer2'],
            'testAnswer3' :request.POST['testAnswer3'],
            'testAnswer4':request.POST['testAnswer4'],
            'testAnswer5':request.POST['testAnswer5'],
            'testAnswer6':request.POST['testAnswer6'],
            'testAnswer7':request.POST['testAnswer7'],
            'testAnswer8':request.POST['testAnswer8'],
            'testAnswer9':request.POST['testAnswer9'],
            'testAnswer10':request.POST['testAnswer10'],

            'testSelectAns1' :request.POST['testSelectAns1'],
            'testSelectAns2' :request.POST['testSelectAns2'],
            'testSelectAns3' :request.POST['testSelectAns3'],
            'testSelectAns4':request.POST['testSelectAns4'],
            'testSelectAns5':request.POST['testSelectAns5'],
            'testSelectAns6':request.POST['testSelectAns6'],
            'testSelectAns7':request.POST['testSelectAns7'],
            'testSelectAns8':request.POST['testSelectAns8'],
            'testSelectAns9':request.POST['testSelectAns9'],
            'testSelectAns10':request.POST['testSelectAns10'],
            
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test10count = request.POST['test10count']
        test10seikai = request.POST['test10seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']

        testQuestion1 = request.POST['testQuestion1']
        testQuestion2 = request.POST['testQuestion2']
        testQuestion3 = request.POST['testQuestion3']
        testQuestion4 = request.POST['testQuestion4']
        testQuestion5 = request.POST['testQuestion5']
        testQuestion6 = request.POST['testQuestion6']
        testQuestion7 = request.POST['testQuestion7']
        testQuestion8 = request.POST['testQuestion8']
        testQuestion9 = request.POST['testQuestion9']
        testQuestion10 = request.POST['testQuestion10']

        testAnswer1 = request.POST['testAnswer1']
        testAnswer2 = request.POST['testAnswer2']
        testAnswer3 = request.POST['testAnswer3']
        testAnswer4 = request.POST['testAnswer4']
        testAnswer5 = request.POST['testAnswer5']
        testAnswer6 = request.POST['testAnswer6']
        testAnswer7 = request.POST['testAnswer7']
        testAnswer8 = request.POST['testAnswer8']
        testAnswer9 = request.POST['testAnswer9']
        testAnswer10 = request.POST['testAnswer10']

        testSelectAns1 = request.POST['testSelectAns1']
        testSelectAns2 = request.POST['testSelectAns2']
        testSelectAns3 = request.POST['testSelectAns3']
        testSelectAns4 = request.POST['testSelectAns4']
        testSelectAns5 = request.POST['testSelectAns5']
        testSelectAns6 = request.POST['testSelectAns6']
        testSelectAns7 = request.POST['testSelectAns7']
        testSelectAns8 = request.POST['testSelectAns8']
        testSelectAns9 = request.POST['testSelectAns9']
        testSelectAns10 = request.POST['testSelectAns10']
    else:
        context = {
            'test10count':request.POST["test10count"],
            'test10seikai':request.POST["test10seikai"],
            
        }
        selectedAns = "shokaihanai"
        testId = 7777777
        testId1 = 7777777
        testId2 = 7777777
        testId3 = 7777777
        testId4 = 7777777
        testId5 = 7777777
        testId6 = 7777777
        testId7 = 7777777
        testId8 = 7777777
        testId9 = 7777777
        testId10 = 7777777

    test10count = int(test10count)
    test10count += 1

    test10seikai = int(test10seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test10seikai += 1
    
    
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        #data = random.sample(pks_list,1)

        #4/20
        #if testId1 = data[0]:
            #data = random.sample(pks_list,1)
                #if testId = data[0]:
                    #data = random.sample(pks_list,1)
                    #if testId = data[0]:
                        #data = random.sample(pks_list,1)

        #try:
            #pks_list.remove(testId1)
        #except:
            #pass

        testId = int(testId)
        testId1 = int(testId1)
        testId2 = int(testId2)
        testId3 = int(testId3)
        testId4 = int(testId4)
        testId5 = int(testId5)
        testId6 = int(testId6)
        testId7 = int(testId7)
        testId8 = int(testId8)
        testId9 = int(testId9)
        testId10 = int(testId10)

        if testShokai != 'testShokai':
            pks_list.remove(testId1)
        
        try:
            pks_list.remove(testId2)
        except:
            pass

        try:
            pks_list.remove(testId3)
        except:
            pass

        try:
            pks_list.remove(testId4)
        except:
            pass

        try:
            pks_list.remove(testId5)
        except:
            pass

        try:
            pks_list.remove(testId6)
        except:
            pass

        try:
            pks_list.remove(testId7)
        except:
            pass

        try:
            pks_list.remove(testId8)
        except:
            pass

        try:
            pks_list.remove(testId9)
        except:
            pass

        try:
            pks_list.remove(testId10)
        except:
            pass
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)
   
        #4/13------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3
    dataCategory = dQ.category
    
    d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer
    #data1Answer = dQ.answer

    d4allshuf2 = Question.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Question.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Question.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Question.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Question.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Question.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Question.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Question.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Question.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Question.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Question.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Question.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Question.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Question.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Question.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Question.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer

    d4allshuf18 = Question.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Question.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Question.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Question.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer

    d4allshuf22 = Question.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Question.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Question.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Question.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Question.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Question.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer


    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]
    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    test10mondaisuu = 10
        
    seikairitsuFloat = (float(test10seikai) / float(test10mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    #4/19 django-pandas----------------------------------
    #df = read_frame(object_list, fieldnames=['answer'])
    df = read_frame(object_list)
    df1 = df.head()
    #----------------------------------------------------

    #4/23 django-pandas----------------------------------
    #df2 = pd.DataFrame(product.objects.all().values())
    #----------------------------------------------------

    dQID = data[0]
    dQQuestion = dQ.question
    dQAnswer = dQ.answer
    dQSelectAns = selectedAns


    if test10count == 0:
        testId1 = 777
        testQuestion1 = 7777
        testAnswer1 = 7777
        testSelectAns1 = 7777
    if test10count <= 1:
        testId2 = 777
        testQuestion2 = 7777
        testAnswer2 = 7777
        testSelectAns2 = 7777
    if test10count <= 2:
        testId3 = 777
        testQuestion3 = 7777
        testAnswer3 = 7777
        testSelectAns3 = 7777
    if test10count <= 3:
        testId4 = 7777
        testQuestion4 = 7777
        testAnswer4 = 7777
        testSelectAns4 = 7777
    if test10count <= 4:
        testId5 = 7777
        testQuestion5 = 7777
        testAnswer5 = 7777
        testSelectAns5 = 7777
    if test10count <= 5:
        testId6 = 7777
        testQuestion6 = 7777
        testAnswer6 = 7777
        testSelectAns6 = 7777
    if test10count <= 6:
        testId7 = 7777
        testQuestion7 = 7777
        testAnswer7 = 7777
        testSelectAns7 = 7777
    if test10count <= 7:
        testId8 = 7777
        testQuestion8 = 7777
        testAnswer8 = 7777
        testSelectAns8 = 7777
    if test10count <= 8:
        testId9 = 7777
        testQuestion9 = 7777
        testAnswer9 = 7777
        testSelectAns9 = 7777
    if test10count <= 9:
        testId10 = 7777
        testQuestion10 = 7777
        testAnswer10 = 7777
        testSelectAns10 = 7777
    if test10count == 1:
        testId1 = dQID
        testQuestion1 = dQQuestion
        testAnswer1 = dQAnswer
        testSelectAns1 = dQSelectAns
    if test10count == 2:
        testId2 = dQID
        testQuestion2 = dQQuestion
        testAnswer2 = dQAnswer
        testSelectAns2 = dQSelectAns
    if test10count == 3:
        testId3 = dQID
        testQuestion3 = dQQuestion
        testAnswer3 = dQAnswer
        testSelectAns3 = dQSelectAns
    if test10count == 4:
        testId4 = dQID
        testQuestion4 = dQQuestion
        testAnswer4 = dQAnswer
        testSelectAns4 = dQSelectAns
    if test10count == 5:
        testId5 = dQID
        testQuestion5 = dQQuestion
        testAnswer5 = dQAnswer
        testSelectAns5 = dQSelectAns
    if test10count == 6:
        testId6 = dQID
        testQuestion6 = dQQuestion
        testAnswer6 = dQAnswer
        testSelectAns6 = dQSelectAns
    if test10count == 7:
        testId7 = dQID
        testQuestion7 = dQQuestion
        testAnswer7 = dQAnswer
        testSelectAns7 = dQSelectAns
    if test10count == 8:
        testId8 = dQID
        testQuestion8 = dQQuestion
        testAnswer8 = dQAnswer
        testSelectAns8 = dQSelectAns
    if test10count == 9:
        testId9 = dQID
        testQuestion9 = dQQuestion
        testAnswer9 = dQAnswer
        testSelectAns9 = dQSelectAns
    if test10count == 10:
        testId10 = dQID
        testQuestion10 = dQQuestion
        testAnswer10 = dQAnswer
        testSelectAns10 = dQSelectAns
    #if test10count == 11:
        #testSelectAns11 = dQSelectAns

    testId = dQID

    #dataKoujun = Question.objects.order_by('pk').reverse()
    #dataKoujun = Question.objects.all().order_by('id').reverse()
    #dataKoujun = data

    
    params = {
            'data': data,
            #'dataKoujun': dataKoujun,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            'test10count':test10count,
            'test10seikai':test10seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test10mondaisuu':test10mondaisuu,
            'selectedAns':selectedAns,
            'df':df1,
            'dfHtml': df1.to_html(),
            #'df2':df2,
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId':testId,

            'testQuestion1':testQuestion1,
            'testQuestion2':testQuestion2,
            'testQuestion3':testQuestion3,
            'testQuestion4':testQuestion4,
            'testQuestion5':testQuestion5,
            'testQuestion6':testQuestion6,
            'testQuestion7':testQuestion7,
            'testQuestion8':testQuestion8,
            'testQuestion9':testQuestion9,
            'testQuestion10':testQuestion10,

            'testAnswer1':testAnswer1,
            'testAnswer2':testAnswer2,
            'testAnswer3':testAnswer3,
            'testAnswer4':testAnswer4,
            'testAnswer5':testAnswer5,
            'testAnswer6':testAnswer6,
            'testAnswer7':testAnswer7,
            'testAnswer8':testAnswer8,
            'testAnswer9':testAnswer9,
            'testAnswer10':testAnswer10,

            'testSelectAns1':testSelectAns1,
            'testSelectAns2':testSelectAns2,
            'testSelectAns3':testSelectAns3,
            'testSelectAns4':testSelectAns4,
            'testSelectAns5':testSelectAns5,
            'testSelectAns6':testSelectAns6,
            'testSelectAns7':testSelectAns7,
            'testSelectAns8':testSelectAns8,
            'testSelectAns9':testSelectAns9,
            'testSelectAns10':testSelectAns10,
            #'testSelectAns11':testSelectAns11,
    }

    if test10count == test10mondaisuu + 1 :
        return render(request, 'book/question_test_result10.html', params)
    else:
        return render(request, 'book/question_test10.html', params)

#5/4
def testQuestionView4taku_10(request):

    object_list = Question.objects.all()
    
    test10count = request.POST["test10count"]
    test10seikai = request.POST["test10seikai"]
    testShokai = request.POST["testShokai"]

    if testShokai != 'testShokai':
        context = {
            'test10count' :request.POST["test10count"],
            'test10seikai' :request.POST["test10seikai"],
            'testShokai' :request.POST["testShokai"],
            'selectedAns' :request.POST["name1"],
            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            'dataThumbnailQ1' :request.POST["nameThuQ1"],
            'dataThumbnailQ2' :request.POST["nameThuQ2"],
            'dataThumbnailQ3' :request.POST["nameThuQ3"],
            'dataThumbnailA1' :request.POST["nameThuA1"],
            'dataThumbnailA2' :request.POST["nameThuA2"],
            'dataThumbnailA3' :request.POST["nameThuA3"],
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],

            'testQuestion1' :request.POST['testQuestion1'],
            'testQuestion2' :request.POST['testQuestion2'],
            'testQuestion3' :request.POST['testQuestion3'],
            'testQuestion4':request.POST['testQuestion4'],
            'testQuestion5':request.POST['testQuestion5'],
            'testQuestion6':request.POST['testQuestion6'],
            'testQuestion7':request.POST['testQuestion7'],
            'testQuestion8':request.POST['testQuestion8'],
            'testQuestion9':request.POST['testQuestion9'],
            'testQuestion10':request.POST['testQuestion10'],

            'testAnswer1' :request.POST['testAnswer1'],
            'testAnswer2' :request.POST['testAnswer2'],
            'testAnswer3' :request.POST['testAnswer3'],
            'testAnswer4':request.POST['testAnswer4'],
            'testAnswer5':request.POST['testAnswer5'],
            'testAnswer6':request.POST['testAnswer6'],
            'testAnswer7':request.POST['testAnswer7'],
            'testAnswer8':request.POST['testAnswer8'],
            'testAnswer9':request.POST['testAnswer9'],
            'testAnswer10':request.POST['testAnswer10'],

            'testSelectAns1' :request.POST['testSelectAns1'],
            'testSelectAns2' :request.POST['testSelectAns2'],
            'testSelectAns3' :request.POST['testSelectAns3'],
            'testSelectAns4':request.POST['testSelectAns4'],
            'testSelectAns5':request.POST['testSelectAns5'],
            'testSelectAns6':request.POST['testSelectAns6'],
            'testSelectAns7':request.POST['testSelectAns7'],
            'testSelectAns8':request.POST['testSelectAns8'],
            'testSelectAns9':request.POST['testSelectAns9'],
            'testSelectAns10':request.POST['testSelectAns10'],
            
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test10count = request.POST['test10count']
        test10seikai = request.POST['test10seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']

        testQuestion1 = request.POST['testQuestion1']
        testQuestion2 = request.POST['testQuestion2']
        testQuestion3 = request.POST['testQuestion3']
        testQuestion4 = request.POST['testQuestion4']
        testQuestion5 = request.POST['testQuestion5']
        testQuestion6 = request.POST['testQuestion6']
        testQuestion7 = request.POST['testQuestion7']
        testQuestion8 = request.POST['testQuestion8']
        testQuestion9 = request.POST['testQuestion9']
        testQuestion10 = request.POST['testQuestion10']

        testAnswer1 = request.POST['testAnswer1']
        testAnswer2 = request.POST['testAnswer2']
        testAnswer3 = request.POST['testAnswer3']
        testAnswer4 = request.POST['testAnswer4']
        testAnswer5 = request.POST['testAnswer5']
        testAnswer6 = request.POST['testAnswer6']
        testAnswer7 = request.POST['testAnswer7']
        testAnswer8 = request.POST['testAnswer8']
        testAnswer9 = request.POST['testAnswer9']
        testAnswer10 = request.POST['testAnswer10']

        testSelectAns1 = request.POST['testSelectAns1']
        testSelectAns2 = request.POST['testSelectAns2']
        testSelectAns3 = request.POST['testSelectAns3']
        testSelectAns4 = request.POST['testSelectAns4']
        testSelectAns5 = request.POST['testSelectAns5']
        testSelectAns6 = request.POST['testSelectAns6']
        testSelectAns7 = request.POST['testSelectAns7']
        testSelectAns8 = request.POST['testSelectAns8']
        testSelectAns9 = request.POST['testSelectAns9']
        testSelectAns10 = request.POST['testSelectAns10']
    else:
        context = {
            'test10count':request.POST["test10count"],
            'test10seikai':request.POST["test10seikai"],
            
        }
        selectedAns = "shokaihanai"
        testId = 7777777
        testId1 = 7777777
        testId2 = 7777777
        testId3 = 7777777
        testId4 = 7777777
        testId5 = 7777777
        testId6 = 7777777
        testId7 = 7777777
        testId8 = 7777777
        testId9 = 7777777
        testId10 = 7777777

    test10count = int(test10count)
    test10count += 1

    test10seikai = int(test10seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test10seikai += 1
    
    
    if (request.method == 'POST'):
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        

        testId = int(testId)
        testId1 = int(testId1)
        testId2 = int(testId2)
        testId3 = int(testId3)
        testId4 = int(testId4)
        testId5 = int(testId5)
        testId6 = int(testId6)
        testId7 = int(testId7)
        testId8 = int(testId8)
        testId9 = int(testId9)
        testId10 = int(testId10)

        if testShokai != 'testShokai':
            pks_list.remove(testId1)
        
        try:
            pks_list.remove(testId2)
        except:
            pass

        try:
            pks_list.remove(testId3)
        except:
            pass

        try:
            pks_list.remove(testId4)
        except:
            pass

        try:
            pks_list.remove(testId5)
        except:
            pass

        try:
            pks_list.remove(testId6)
        except:
            pass

        try:
            pks_list.remove(testId7)
        except:
            pass

        try:
            pks_list.remove(testId8)
        except:
            pass

        try:
            pks_list.remove(testId9)
        except:
            pass

        try:
            pks_list.remove(testId10)
        except:
            pass
        data = random.sample(pks_list,1)

        #4/9------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    else:
        pks = Question.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)
   
        #4/13------------------
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)
        #---------------------

    dQ = Question.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3
    dataCategory = dQ.category
    
    #d4allshuf1 = Question.objects.get(id=data4allshuffle[0])
    #data1Answer = d4allshuf1.answer
    data1Answer = dQ.answer

    data2Answer = dataWrongAnswer1 
    data3Answer = dataWrongAnswer2
    data4Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,4)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    
    test10mondaisuu = 10
        
    seikairitsuFloat = (float(test10seikai) / float(test10mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    dQID = data[0]
    dQQuestion = dQ.question
    dQAnswer = dQ.answer
    dQSelectAns = selectedAns


    if test10count == 0:
        testId1 = 777
        testQuestion1 = 7777
        testAnswer1 = 7777
        testSelectAns1 = 7777
    if test10count <= 1:
        testId2 = 777
        testQuestion2 = 7777
        testAnswer2 = 7777
        testSelectAns2 = 7777
    if test10count <= 2:
        testId3 = 777
        testQuestion3 = 7777
        testAnswer3 = 7777
        testSelectAns3 = 7777
    if test10count <= 3:
        testId4 = 7777
        testQuestion4 = 7777
        testAnswer4 = 7777
        testSelectAns4 = 7777
    if test10count <= 4:
        testId5 = 7777
        testQuestion5 = 7777
        testAnswer5 = 7777
        testSelectAns5 = 7777
    if test10count <= 5:
        testId6 = 7777
        testQuestion6 = 7777
        testAnswer6 = 7777
        testSelectAns6 = 7777
    if test10count <= 6:
        testId7 = 7777
        testQuestion7 = 7777
        testAnswer7 = 7777
        testSelectAns7 = 7777
    if test10count <= 7:
        testId8 = 7777
        testQuestion8 = 7777
        testAnswer8 = 7777
        testSelectAns8 = 7777
    if test10count <= 8:
        testId9 = 7777
        testQuestion9 = 7777
        testAnswer9 = 7777
        testSelectAns9 = 7777
    if test10count <= 9:
        testId10 = 7777
        testQuestion10 = 7777
        testAnswer10 = 7777
        testSelectAns10 = 7777
    if test10count == 1:
        testId1 = dQID
        testQuestion1 = dQQuestion
        testAnswer1 = dQAnswer
        testSelectAns1 = dQSelectAns
    if test10count == 2:
        testId2 = dQID
        testQuestion2 = dQQuestion
        testAnswer2 = dQAnswer
        testSelectAns2 = dQSelectAns
    if test10count == 3:
        testId3 = dQID
        testQuestion3 = dQQuestion
        testAnswer3 = dQAnswer
        testSelectAns3 = dQSelectAns
    if test10count == 4:
        testId4 = dQID
        testQuestion4 = dQQuestion
        testAnswer4 = dQAnswer
        testSelectAns4 = dQSelectAns
    if test10count == 5:
        testId5 = dQID
        testQuestion5 = dQQuestion
        testAnswer5 = dQAnswer
        testSelectAns5 = dQSelectAns
    if test10count == 6:
        testId6 = dQID
        testQuestion6 = dQQuestion
        testAnswer6 = dQAnswer
        testSelectAns6 = dQSelectAns
    if test10count == 7:
        testId7 = dQID
        testQuestion7 = dQQuestion
        testAnswer7 = dQAnswer
        testSelectAns7 = dQSelectAns
    if test10count == 8:
        testId8 = dQID
        testQuestion8 = dQQuestion
        testAnswer8 = dQAnswer
        testSelectAns8 = dQSelectAns
    if test10count == 9:
        testId9 = dQID
        testQuestion9 = dQQuestion
        testAnswer9 = dQAnswer
        testSelectAns9 = dQSelectAns
    if test10count == 10:
        testId10 = dQID
        testQuestion10 = dQQuestion
        testAnswer10 = dQAnswer
        testSelectAns10 = dQSelectAns

    testId = dQID
    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            'test10count':test10count,
            'test10seikai':test10seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test10mondaisuu':test10mondaisuu,
            'selectedAns':selectedAns,
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId':testId,

            'testQuestion1':testQuestion1,
            'testQuestion2':testQuestion2,
            'testQuestion3':testQuestion3,
            'testQuestion4':testQuestion4,
            'testQuestion5':testQuestion5,
            'testQuestion6':testQuestion6,
            'testQuestion7':testQuestion7,
            'testQuestion8':testQuestion8,
            'testQuestion9':testQuestion9,
            'testQuestion10':testQuestion10,

            'testAnswer1':testAnswer1,
            'testAnswer2':testAnswer2,
            'testAnswer3':testAnswer3,
            'testAnswer4':testAnswer4,
            'testAnswer5':testAnswer5,
            'testAnswer6':testAnswer6,
            'testAnswer7':testAnswer7,
            'testAnswer8':testAnswer8,
            'testAnswer9':testAnswer9,
            'testAnswer10':testAnswer10,

            'testSelectAns1':testSelectAns1,
            'testSelectAns2':testSelectAns2,
            'testSelectAns3':testSelectAns3,
            'testSelectAns4':testSelectAns4,
            'testSelectAns5':testSelectAns5,
            'testSelectAns6':testSelectAns6,
            'testSelectAns7':testSelectAns7,
            'testSelectAns8':testSelectAns8,
            'testSelectAns9':testSelectAns9,
            'testSelectAns10':testSelectAns10,
            
    }

    if test10count == test10mondaisuu + 1 :
        return render(request, 'book/question_test4taku_result10.html', params)
    else:
        return render(request, 'book/question_test4taku_10.html', params)



class DetailQuestionView(LoginRequiredMixin, DetailView):
    object_list = Question.objects.all()
    template_name = 'book/question_detail.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Question.objects.all()
        return context

class CreateQuestionView(LoginRequiredMixin, CreateView):
    object_list = Question.objects.all()
    template_name = 'book/question_create.html'
    form_class = QuestionForm
    #def __init__(self):
        #self.params = {"情報を入力してください。","form":forms.QuestionForm(),}

    model = Question
    #fields = ('question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','hint1','hint2','explanation', 'category', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3')
    

    #success_url = reverse_lazy('list-question')
    success_url = reverse_lazy('create-question')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Question.objects.all()

        context['fromList'] = ""

        #4/18-------------
        shoseki_list = Question.objects.values_list('shoseki', flat=True)
        context['shoseki'] = shoseki_list
        print()
        #------------------
        
        touroku1tsumae = Question.objects.all().last()
        touroku1tsumaeShoseki = touroku1tsumae.shoseki
        touroku1tsumaeCategory = touroku1tsumae.category
        touroku1tsumaeQuestion = touroku1tsumae.question
        touroku1tsumaeAnswer = touroku1tsumae.answer
        touroku1tsumaePage = touroku1tsumae.shoseki_page
        touroku1tsumaeId = touroku1tsumae.id
        context['touroku1tsumaeShoseki'] = touroku1tsumaeShoseki
        context['touroku1tsumaeCategory'] = touroku1tsumaeCategory 
        context['touroku1tsumaeQuestion'] = touroku1tsumaeQuestion
        context['touroku1tsumaeAnswer'] = touroku1tsumaeAnswer
        context['touroku1tsumaePage'] = touroku1tsumaePage
        context['touroku1tsumaeId'] = touroku1tsumaeId 
        
        context['tourokugoNew'] = ""
        #0427-------------
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        databaseSpecialistCount = Question.objects.filter(shoseki__icontains="データベーススペシャリスト教科書令和4年度", created_at__range=[today, datetime.now()]).count()
        accessVBACount = Question.objects.filter(shoseki__icontains="Access VBA スタンダード", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>", created_at__range=[today, datetime.now()]).count()
        ouyoujouhouCount = Question.objects.filter(shoseki__icontains="令和04年【春期】　応用情報技術者　過去問題集", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="応用情報技術者テキスト&問題集2020年版", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="キタミ式ITイラスト塾　応用情報技術者　令和03年", created_at__range=[today, datetime.now()]).count()
        kihonjouhouCount = Question.objects.filter(shoseki__icontains="キタミ式ITイラスト塾　基本情報技術者　令和02年", created_at__range=[today, datetime.now()]).count()
        toukeikenteiCount = Question.objects.filter(shoseki__icontains="統計検定2級　模擬問題集1", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="統計検定2級公式問題集CBT対応板", created_at__range=[today, datetime.now()]).count()
        
        python3Count = Question.objects.filter(shoseki__icontains="Python3エンジニア認定基礎試験問題集", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="Python3エンジニア認定基礎試験Web問題", created_at__range=[today, datetime.now()]).count()
        sqlCount = Question.objects.filter(shoseki__icontains="Bronze 12c SQL 基礎問題集", created_at__range=[today, datetime.now()]).count()
        python3JissenCount = Question.objects.filter(shoseki__icontains="Python3エンジニア認定実践試験Web問題", created_at__range=[today, datetime.now()]).count()
        python3dataBunsekiCount = Question.objects.filter(shoseki__icontains="Python3エンジニア認定データ分析試験Web問題", created_at__range=[today, datetime.now()]).count()
        gkenteiCount = Question.objects.filter(shoseki__icontains="ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集", created_at__range=[today, datetime.now()]).count()
        linuxCount = Question.objects.filter(shoseki__icontains="LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="LPICレベル1スピードマスター問題集", created_at__range=[today, datetime.now()]).count() + Question.objects.filter(shoseki__icontains="シェルワンライナー100本ノック", created_at__range=[today, datetime.now()]).count()
        dataScientistCount = Question.objects.filter(shoseki__icontains="徹底攻略データサイエンティスト検定リテラシーレベル問題集", created_at__range=[today, datetime.now()]).count()
        eShikakuCount  = Question.objects.filter(shoseki__icontains="徹底攻略ディープラーニングE資格エンジニア問題集", created_at__range=[today, datetime.now()]).count()
        boki2Count  = Question.objects.filter(shoseki__icontains="パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集", created_at__range=[today, datetime.now()]).count()
        javaCount  = Question.objects.filter(shoseki__icontains="徹底攻略 Java SE Bronze 問題集", created_at__range=[today, datetime.now()]).count()

        context['databaseSpecialistCount'] = databaseSpecialistCount
        context['accessVBACount'] = accessVBACount
        context['ouyoujouhouCount'] = ouyoujouhouCount
        context['kihonjouhouCount'] = kihonjouhouCount
        context['toukeikenteiCount'] = toukeikenteiCount
        context['python3Count'] = python3Count
        context['sqlCount'] = sqlCount
        context['python3JissenCount'] = python3JissenCount
        context['python3dataBunsekiCount'] = python3dataBunsekiCount
        context['gkenteiCount'] = gkenteiCount
        context['linuxCount'] = linuxCount
        context['dataScientistCount'] = dataScientistCount
        #context['selectColor'] = selectColor,
        context['eShikakuCount'] = eShikakuCount
        context['boki2Count'] = boki2Count
        context['javaCount'] = javaCount
        
        return context
    
    
    
    def get(self, request, *args, **kwargs):
        self.object = Question(question=self.request.user)

        context = self.get_context_data(**kwargs)

        
        dataFirst1 = ""
        dataFirst1_page = ""
        dataFirst1_shoseki = ""

        dataFirst2 = ""
        dataFirst2_page = ""
        dataFirst2_shoseki = ""   

        dataFirst3 = ""
        dataFirst3_page = ""
        dataFirst3_shoseki = ""
        context['kategory'] = ""

        nextReg = ""
        nextShoseki = ""
        nextQuestion = ""
        nextCategory = ""
        nextSho_page = ""

        """
        context['shosekiSakuseigo'] = ""
        context['kateSakuseigo'] = ""
        """
        
        if request.GET.get("nameTouroku") == "sono1":

            first1 = request.GET.get("nameFirst1")
            context['first1'] = first1
            context['idid'] = first1

            first1Shoseki = request.GET.get("nameFirst1Shoseki")
            context['first1Shoseki'] = first1Shoseki
            context['sho'] = first1Shoseki
    
            first1Shoseki_page = request.GET.get("nameFirst1Shoseki_page")
            context['first1Shoseki_page'] = first1Shoseki_page
            context['sho_page'] = first1Shoseki_page

            first1Category = request.GET.get("nameFirst1Category")
            context['first1Category'] = first1Category
            context['cate'] = first1Category

            first1Question = request.GET.get("nameFirst1Question")
            context['first1Question'] = first1Question
            context['que'] = first1Question
            

            dataWatashi = "watashi1"
            context['dataWatashi'] = dataWatashi

            context['fromList'] = "ari"


        elif request.GET.get("nameTouroku") == "sono2":

            first2 = request.GET.get("nameFirst2")
            context['first2'] = first2
            context['idid'] = first2

            first2Shoseki = request.GET.get("nameFirst2Shoseki")
            context['first2Shoseki'] = first2Shoseki
            context['sho'] = first2Shoseki
        
            first2Shoseki_page = request.GET.get("nameFirst2Shoseki_page")
            context['first2Shoseki_page'] = first2Shoseki_page
            context['sho_page'] = first2Shoseki_page

            first2Category = request.GET.get("nameFirst2Category")
            context['first2Category'] = first2Category
            context['cate'] = first2Category

            first2Question = request.GET.get("nameFirst2Question")
            context['first2Question'] = first2Question
            context['que'] = first2Question
        
            dataWatashi = "watashi2"
            context['dataWatashi'] = dataWatashi

            context['fromList'] = "ari"

        elif request.GET.get("nameTouroku") == "sono3":

            first3 = request.GET.get("nameFirst3")
            context['first3'] = first3
            context['idid'] = first3

            first3Shoseki = request.GET.get("nameFirst3Shoseki")
            context['first3Shoseki'] = first3Shoseki
            context['sho'] = first3Shoseki
        
            first3Shoseki_page = request.GET.get("nameFirst3Shoseki_page")
            context['first3Shoseki_page'] = first3Shoseki_page
            context['sho_page'] = first3Shoseki_page

            first3Category = request.GET.get("nameFirst3Category")
            context['first3Category'] = first3Category
            context['cate'] = first3Category

            first3Question = request.GET.get("nameFirst3Question")
            context['first3Question'] = first3Question
            context['que'] = first3Question

            dataWatashi = "watashi3"
            context['dataWatashi'] = dataWatashi

            context['fromList'] = "ari"
            

        #else:
        #5/5
        elif request.GET.get('nameG') == "G検定":
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = gkenteiNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameG')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "gkentei"

            context['kuuhaku'] = "kuuhaku"
            

        elif request.GET.get('nameLinux'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = linuxNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LPICレベル1スピードマスター問題集"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="LPICレベル1スピードマスター問題集").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
                """
                nextReg = linuxNext2
                nextShoseki = dataFirst2.shoseki
                nextQuestion = dataFirst2.question
                nextCategory = dataFirst2.category
                nextSho_page = dataFirst2.shoseki_page
                """
            
            dataFirst3 = ""      
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameLinux')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "linux"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameSQL'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Bronze 12c SQL 基礎問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Bronze 12c SQL 基礎問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = sqlNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameSQL')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "sql"
            
            context['kuuhaku'] = "kuuhaku"
        
        elif request.GET.get('namePython3D'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定データ分析試験Web問題"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定データ分析試験Web問題").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = python3DNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
           
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('namePython3D')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "python3d"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameAccessVBA'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Access VBA"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Access VBA").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = accessVBANext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameAccessVBA')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "accessvba"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameToukei'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集1"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集1").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = toukeiNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集2"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級　模擬問題集2").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
                """
                nextReg = toukeiNext2
                nextShoseki = dataFirst2.shoseki
                nextQuestion = dataFirst2.question
                nextCategory = dataFirst2.category
                nextSho_page = dataFirst2.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級公式問題集CBT対応板"):
                dataFirst3 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="統計検定2級公式問題集CBT対応板").first()
                dataFirst3_page = dataFirst3.shoseki_page
                dataFirst3_shoseki = dataFirst3.shoseki
                """
                nextReg = toukeiNext3
                nextShoseki = dataFirst3.shoseki
                nextQuestion = dataFirst3.question
                nextCategory = dataFirst3.category
                nextSho_page = dataFirst3.shoseki_page
                """
            selectColor = request.GET.get('nameToukei')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "toukei"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('namePython3'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験Web問題"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験Web問題").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = python3Next1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験問題集"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定基礎試験問題集").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
                """
                nextReg = python3Next2
                nextShoseki = dataFirst2.shoseki
                nextQuestion = dataFirst2.question
                nextCategory = dataFirst2.category
                nextSho_page = dataFirst2.shoseki_page
                """
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('namePython3')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "python3"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameDBS'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="データベーススペシャリスト教科書令和4年度"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="データベーススペシャリスト教科書令和4年度").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = dbsNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            #dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            #dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameDBS')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "dbs"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameOuyou'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　応用情報技術者　令和03年"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　応用情報技術者　令和03年").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = ouyouNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="令和04年【春期】　応用情報技術者　過去問題集"):
                dataFirst2 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="令和04年【春期】　応用情報技術者　過去問題集").first()
                dataFirst2_page = dataFirst2.shoseki_page
                dataFirst2_shoseki = dataFirst2.shoseki
                """
                nextReg = ouyouNext2
                nextShoseki = dataFirst2.shoseki
                nextQuestion = dataFirst2.question
                nextCategory = dataFirst2.category
                nextSho_page = dataFirst2.shoseki_page
                """
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="応用情報技術者　試験によくでる問題集【午後】"):
                dataFirst3 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="応用情報技術者　試験によくでる問題集【午後】").first()
                dataFirst3_page = dataFirst3.shoseki_page
                dataFirst3_shoseki = dataFirst3.shoseki
                """
                nextReg = ouyouNext3
                nextShoseki = dataFirst3.shoseki
                nextQuestion = dataFirst3.question
                nextCategory = dataFirst3.category
                nextSho_page = dataFirst3.shoseki_page
                """
            selectColor = request.GET.get('nameOuyou')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "ouyou"

            context['kuuhaku'] = "kuuhaku"

        #5/6
        elif request.GET.get('nameKihon'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　基本情報技術者　令和02年"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="キタミ式ITイラスト塾　基本情報技術者　令和02年").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = kihonNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""

            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameKihon')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "kihon"   

            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('namePython3Jissen'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定実践試験Web問題"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="Python3エンジニア認定実践試験Web問題").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = python3JissenNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """
            
            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""

            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('namePython3Jissen')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "python3jissen"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameDataScientist'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略データサイエンティスト検定リテラシーレベル問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略データサイエンティスト検定リテラシーレベル問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = dataScientistNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """

            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameDataScientist')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "datascientist"
            
            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameEshikaku'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略ディープラーニングE資格エンジニア問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="徹底攻略ディープラーニングE資格エンジニア問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                """
                nextReg = EshikakuNext1
                nextShoseki = dataFirst1.shoseki
                nextQuestion = dataFirst1.question
                nextCategory = dataFirst1.category
                nextSho_page = dataFirst1.shoseki_page
                """

            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameEshikaku')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "eshikaku"

            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameBoki2'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki
                

            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameBoki2')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "boki2"

            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameJava'):
            if Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="- [ ] 徹底攻略 Java SE Bronze 問題集"):
                dataFirst1 = Question.objects.all().order_by('pk').reverse().filter(shoseki__contains="- [ ] 徹底攻略 Java SE Bronze 問題集").first()
                dataFirst1_page = dataFirst1.shoseki_page
                dataFirst1_shoseki = dataFirst1.shoseki

            dataFirst2 = ""
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = ""
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = request.GET.get('nameJava')

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
            context['kategory'] = "java"

            context['kuuhaku'] = "kuuhaku"

        elif request.GET.get('nameFind'):
            data = Question.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,category__contains=answers)
            dataFirst1 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = dataFirst1.shoseki_page
            dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = dataFirst2.shoseki_page
            dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = dataFirst3.shoseki_page
            dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = ""

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki
        
            
        else:
            dataFirst1 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = ""
            dataFirst1_shoseki = ""
            dataFirst2 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = Question.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            selectColor = ""

        """
        context['nextReg'] = nextReg
        context['nextShoseki'] = nextShoseki
        context['nextQuestion'] = nextQuestion
        context['nextCategory'] = nextCategory
        context['nextSho_page'] = nextSho_page
        """

        #today = datetime.today().replace(hour=0, #minute=0, second=0, microsecond=0).astimezone()
        """
        else:
        
        form = FindForm()
        data = Question.objects.all().order_by('pk').reverse()
        
        dataFirst1 = ""
        dataFirst2 = ""
        dataFirst3 = ""
        dataFirst1_page = ""
        dataFirst2_page = ""
        dataFirst3_page = ""
        """

        #0522-----------------------------------
        #context = self.get_context_data(**kwargs)
        context['shosekiSakuseigo'] = ""
        context['kateSakuseigo'] = ""

        
        context['tourokugoNew'] = "tourokumae"
        
        
        return self.render_to_response(context)
        


      #5/14
    """
    def post(self, request, *args, **kwargs):
        self.object = Question(question=self.request.user)

        context = self.get_context_data(**kwargs)

        dataFirst1 = ""
        dataFirst1_page = ""
        dataFirst1_shoseki = ""

        dataFirst2 = ""
        dataFirst2_page = ""
        dataFirst2_shoseki = ""   

        dataFirst3 = ""
        dataFirst3_page = ""
        dataFirst3_shoseki = ""
        context['kategory'] = ""

        
        nextReg = ""
        nextShoseki = ""
        nextQuestion = ""
        nextCategory = ""
        nextSho_page = ""
        """
    """
    def post(self, request, *args, **kwargs):
        self.object = Question(question=self.request.user)

        context = self.get_context_data(**kwargs)

        if request.method == 'POST':
            context['shosekiSakuseigo'] = request.POST.get("shoseki")
            context['kateSakuseigo'] = request.POST.get("category")
        
            context['tes'] = "tes"
        
        
        return self.render_to_response(context)
        """
        


    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        ##form = QuestionForm(request.POST)
        #data = form.cleaned_data
        #obj = Question(**data)
        #obj.save()

        #self.object = form.save(self.request.user)
        #return HttpResponseRedirect(self.get_success_url())

        """
        context['nextReg'] = nextReg
        context['nextShoseki'] = nextShoseki
        context['nextQuestion'] = nextQuestion
        context['nextCategory'] = nextCategory
        context['nextSho_page'] = nextSho_page
        """

        """
        #0521
        context = self.get_context_data(**kwargs)
        context['shosekiSakuseigo'] = ""
        context['kateSakuseigo'] = ""

        if self.request.method == 'POST':
            context['shosekiSakuseigo'] = self.request.POST.get("nameShosekiSakuseigo")
            context['kateSakuseigo'] = self.request.POST.get("nameKateSakuseigo")
        """
        #self.newDef(self, *args, **kwargs)
        
        
        #return self.render_to_response(context)
        

        return super().form_valid(form) 
        #return self.render_to_response(context)

        #return render(self.request, self.template_name, context)
        

    """
    def form_invalid(self, form):
        print(form.errors)
        form.instance.user = self.request.user
        return super().form_invalid(form)
        """
            
      
class DeleteQuestionView(LoginRequiredMixin, DeleteView):
    object_list = Question.objects.all()
    template_name = 'book/question_confirm_delete.html'
    model = Question
    success_url = reverse_lazy('list-question')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Question.objects.all()
        return context
        """

class UpdateQuestionView(LoginRequiredMixin, UpdateView):
    model = Question
    #fields = ('question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','hint1','hint2','explanation', 'category', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3')
    template_name = 'book/question_update.html'
    form_class = QuestionForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-question', kwargs={'pk': self.object.id})

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Question.objects.all()
        return context
        """
"""
class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        print(context)

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})
"""


# Portfolio
def ListPortfolioView(request):

    if (request.method == 'POST'):
        form = FindPortfolioForm(request.POST)
        find1 = request.POST.get('find1')
        find2 = request.POST.get('find2')
        answers = request.POST.get('answers')
        data = Portfolio.objects.filter(title__contains=find1,text__contains=find2,category__contains=answers)
        #msg = 'Result: ' + str(data.count())
    else:
        #msg = 'search words...'
        form = FindPortfolioForm()
        data = Portfolio.objects.all()
    params = {
            'title': '',
            #'message': msg,
            'form': form,
            'data': data,
    }
    return render(request, 'book/portfolio_list.html', params)


class DetailPortfolioView(LoginRequiredMixin, DetailView):
    object_list = Portfolio.objects.all()
    template_name = 'book/portfolio_detail.html'
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Portfolio.objects.all()
        return context

class CreatePortfolioView(LoginRequiredMixin, CreateView):
    object_list = Portfolio.objects.all()
    template_name = 'book/portfolio_create.html'
    form_class = PortfolioForm
    #def __init__(self):
        #self.params = {"情報を入力してください。","form":forms.QuestionForm(),}

    model = Portfolio
    #fields = ('question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','hint1','hint2','explanation', 'category', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3')
    success_url = reverse_lazy('list-portfolio')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Portfolio.objects.all()
        return context
        

class DeletePortfolioView(LoginRequiredMixin, DeleteView):
    object_list = Portfolio.objects.all()
    template_name = 'book/portfolio_confirm_delete.html'
    model = Portfolio
    success_url = reverse_lazy('book:list-portfolio')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Portfolio.objects.all()
        return context


class UpdatePortfolioView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    #fields = ('question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','hint1','hint2','explanation', 'category', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3')
    template_name = 'book/portfolio_update.html'
    form_class = PortfolioForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-portfolio', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Portfolio.objects.all()
        return context


# Picturecomment
class ListPicturecommentView(LoginRequiredMixin, ListView):
    template_name ='book/picturecomment_list.html'
    model = Picturecomment
    paginated_by = ITEM_PER_PAGE

class DetailPicturecommentView(LoginRequiredMixin, DetailView):
    template_name = 'book/picturecomment_detail.html'
    model = Picturecomment

class CreatePicturecommentView(LoginRequiredMixin, CreateView):
    template_name = 'book/picturecomment_create.html'
    model = Picturecomment
    fields = ('title','category', 'thumbnail')
    success_url = reverse_lazy('list-picturecomment')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeletePicturecommentView(LoginRequiredMixin, DeleteView):
    template_name = 'book/picturecomment_confirm_delete.html'
    model = Picturecomment
    success_url = reverse_lazy('book:list-picturecomment')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdatePicturecommentView(LoginRequiredMixin, UpdateView):
    model = Picturecomment
    fields = ('title','category', 'thumbnail')
    template_name = 'book/picturecomment_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-picturecomment', kwargs={'pk': self.object.id})


class ListCodememoView(LoginRequiredMixin, ListView):
    template_name ='book/codememo_list.html'
    model = Codememo
    paginated_by = ITEM_PER_PAGE

class DetailCodememoView(LoginRequiredMixin, DetailView):
    template_name = 'book/codememo_detail.html'
    model = Codememo

class CreateCodememoView(LoginRequiredMixin, CreateView):
    template_name = 'book/codememo_create.html'
    model = Codememo
    #fields = ('title', 'text', 'category')
    form_class = CodememoForm
    success_url = reverse_lazy('list-codememo')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteCodememoView(LoginRequiredMixin, DeleteView):
    template_name = 'book/codememo_confirm_delete.html'
    model = Codememo
    success_url = reverse_lazy('book:list-codememo')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdateCodememoView(LoginRequiredMixin, UpdateView):
    model = Codememo
    fields = ('title', 'text', 'category')
    template_name = 'book/codememo_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-codememo', kwargs={'pk': self.object.id})

#0422
class ListPositionView(LoginRequiredMixin, ListView):
    template_name ='book/position_list.html'
    model = Position
    paginated_by = ITEM_PER_PAGE

class DetailPositionView(LoginRequiredMixin, DetailView):
    template_name = 'book/position_detail.html'
    model = Position

class CreatePositionView(LoginRequiredMixin, CreateView):
    template_name = 'book/position_create.html'
    model = Position
    #fields = ('title', 'text', 'category')
    form_class = PositionForm
    success_url = reverse_lazy('list-position')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class DeletePositionView(LoginRequiredMixin, DeleteView):
    template_name = 'book/position_confirm_delete.html'
    model = Position
    success_url = reverse_lazy('book:list-position')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

class UpdatePositionView(LoginRequiredMixin, UpdateView):
    model = Position
    fields = ('title', 'text', 'category')
    template_name = 'book/position_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-position', kwargs={'pk': self.object.id})