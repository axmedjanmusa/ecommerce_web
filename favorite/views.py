from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from favorite.models import FavoriteProduct
from shop.models import Product


@login_required
def favorite_list(request):
    favorites = FavoriteProduct.objects.filter(user=request.user)
    return render(request, 'favorite/favorite.html', {'favorites': favorites})


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not FavoriteProduct.objects.filter(user=request.user, product=product).exists():
        FavoriteProduct.objects.create(user=request.user, product=product)
        messages.success(request, 'Товар добавлен в избранное')
    else:
        messages.info(request, 'Товар уже в избранном')

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite = FavoriteProduct.objects.filter(user=request.user, product=product).first()
    if favorite:
        favorite.delete()
        messages.success(request, 'Товар удален из избранного')

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    favorite = FavoriteProduct.objects.filter(user=request.user, product=product).first()

    if favorite:
        favorite.delete()
        is_favorite = False
        message = 'Удалено из избранного'
    else:
        FavoriteProduct.objects.create(user=request.user, product=product)
        is_favorite = True
        message = 'Добавлено в избранное'

    return JsonResponse({
        'is_favorite': is_favorite,
        'message': message
    })