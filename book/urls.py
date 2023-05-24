from django.urls import path

from . import views



urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/', views.ListBookView.as_view(), name='list-book'),
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name='detail-book'),
    path('book/create/', views.CreateBookView.as_view(), name='create-book'),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name='delete-book'), 
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-book'),
    path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),

    path('question/random/', views.questionRandom, name='questionRandom'),
    path('question/random10/', views.questionRandom10, name='questionRandom10'),
    path('question/random20/', views.questionRandom20, name='questionRandom20'),
    path('question/random30/', views.questionRandom30, name='questionRandom30'),
    #path('question/random50/', views.questionRandom50, name='questionRandom50'),
    path('question/random/result/', views.answerResult, name='answer-result'),

    path('question/<int:pk>/each/', views.EachQuestionView, name='each-question'),
    path('question/<int:pk>/each10/', views.EachQuestionView10, name='each-question10'),
    path('question/<int:pk>/each20/', views.EachQuestionView20, name='each-question20'),
    path('question/<int:pk>/each30/', views.EachQuestionView30, name='each-question30'),
    path('question/', views.ListQuestionView, name='list-question'),
    path('question/test/', views.testQuestionView, name='test-question'),
    path('question/test/50/', views.testQuestionView50, name='test-question50'),
    path('question/test/10/', views.testQuestionView10, name='test-question10'),
    path('question/test/4_10/', views.testQuestionView4taku_10, name='test-question4-10'),
    
    #path('question/find/',views.ListQuestionFindAfterView,name='find'),
    path('question/<int:pk>/detail/', views.DetailQuestionView.as_view(), name='detail-question'),
    path('question/create/', views.CreateQuestionView.as_view(), name='create-question'),
    path('question/<int:pk>/delete/', views.DeleteQuestionView.as_view(), name='delete-question'), 
    path('question/<int:pk>/update/', views.UpdateQuestionView.as_view(), name='update-question'),

    path('portfolio/', views.ListPortfolioView, name='list-portfolio'),
    path('portfolio/<int:pk>/detail/', views.DetailPortfolioView.as_view(), name='detail-portfolio'),
    path('portfolio/create/', views.CreatePortfolioView.as_view(), name='create-portfolio'),
    path('portfolio/<int:pk>/delete/', views.DeletePortfolioView.as_view(), name='delete-portfolio'), 
    path('portfolio/<int:pk>/update/', views.UpdatePortfolioView.as_view(), name='update-portfolio'),
    
    path('picturecomment/', views.ListPicturecommentView.as_view(), name='list-picturecomment'),
    path('picturecomment/<int:pk>/detail/', views.DetailPicturecommentView.as_view(), name='detail-picturecomment'),
    path('picturecomment/create/', views.CreatePicturecommentView.as_view(), name='create-picturecomment'),
    path('picturecomment/<int:pk>/delete/', views.DeletePicturecommentView.as_view(), name='delete-picturecomment'), 
    path('picturecomment/<int:pk>/update/', views.UpdatePicturecommentView.as_view(), name='update-picturecomment'),

    path('codememo/', views.ListCodememoView.as_view(), name='list-codememo'),
    path('codememo/<int:pk>/detail/', views.DetailCodememoView.as_view(), name='detail-codememo'),
    path('codememo/create/', views.CreateCodememoView.as_view(), name='create-codememo'),
    path('codememo/<int:pk>/delete/', views.DeleteCodememoView.as_view(), name='delete-codememo'), 
    path('codememo/<int:pk>/update/', views.UpdateCodememoView.as_view(), name='update-codememo'),

    path('position/', views.ListPositionView.as_view(), name='list-position'),
    path('position/<int:pk>/detail/', views.DetailPositionView.as_view(), name='detail-position'),
    path('position/create/', views.CreatePositionView.as_view(), name='create-position'),
    path('position/<int:pk>/delete/', views.DeletePositionView.as_view(), name='delete-position'), 
    path('position/<int:pk>/update/', views.UpdatePositionView.as_view(), name='update-position'),
]
