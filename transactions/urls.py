from django.urls import path
from .views import TransactionsView, BalanceView

urlpatterns = [
    path('transactions/<str:date>/', TransactionsView.as_view()),
    path('details/<int:id>/', TransactionsView.as_view()),
    path('add/', BalanceView.as_view()),
    path('balance/<str:date>/', BalanceView.as_view()),
]
