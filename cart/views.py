from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from shop.models import Product
from .models import Cart, CartItem
from .forms import CartItemForm, AddToCartForm


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, defaults={'session_key': None})
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key, defaults={'user': None})
    return cart


@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = get_cart(request)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        messages.success(request, f'"{product.name}" успешно добавлен в корзину. Количество: {cart_item.quantity}.')
        return redirect('shop:product_detail', product_id=product_id)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'Ошибка для поля "{field}": {error}')
        return redirect('shop:product_detail', product_id=product_id)


def cart_detail(request):
    cart = get_cart(request)
    cart_items_with_forms = []
    for item in cart.items.all():
        item_form = CartItemForm(initial={'quantity': item.quantity})
        cart_items_with_forms.append({
            'item': item,
            'form': item_form
        })

    context = {
        'cart_items': cart_items_with_forms,
        'cart': cart,
    }

    return render(request, 'cart/cart.html', context)


@require_POST
def update_cart_item(request, item_id):
    cart = get_cart(request)
    try:
        cart_item = CartItem.objects.get(pk=item_id, cart=cart)
    except CartItem.DoesNotExist:
        messages.error(request, 'Элемент не найден в вашей корзине.')
        return redirect('cart:cart_detail')

    form = CartItemForm(request.POST, instance=cart_item)
    if form.is_valid():
        new_quantity = form.cleaned_data['quantity']

        if new_quantity <= 0:
            cart_item.delete()
            messages.success(request, f'Товар "{cart_item.product.name}" удален из корзины.')
        else:
            if cart_item.product.stock < new_quantity:
                messages.error(request,
                               f'Недостаточно товара "{cart_item.product.name}" на складе. Доступно: {cart_item.product.stock}.')
                return redirect('cart:cart_detail')

            form.save()
            messages.success(request, f'Количество для "{cart_item.product.name}" обновлено до {cart_item.quantity}.')
        return redirect('cart:cart_detail')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'Ошибка при обновлении количества: {error}')
        return redirect('cart:cart_detail')


@require_POST
def remove_cart_item(request, item_id):
    cart = get_cart(request)
    try:
        cart_item = CartItem.objects.get(pk=item_id, cart=cart)
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f'Товар "{product_name}" удален из вашей корзины.')
    except CartItem.DoesNotExist:
        messages.error(request, 'Элемент не найден в вашей корзине.')
    return redirect('cart:cart_detail')