from django.urls import path
from catalog.views import CategoriesListView, CategoryProductsView, \
    DiscountsListView, DiscountProductsView, SellersListView, SellerProductsView, \
    BasketView, OrderView


urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),

    path('discounts/', DiscountsListView.as_view()),
    path('discounts/<int:discount_id>/', DiscountProductsView.as_view()),

    path('sellers/', SellersListView.as_view()),
    path('sellers/<int:seller_id>/', SellerProductsView.as_view()),

    path('basket/', BasketView.as_view()),

    path('order/', OrderView.as_view())
]