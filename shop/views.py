from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from cart.forms import AddToCartForm
from django.shortcuts import render, get_object_or_404, redirect

from user.forms import CommentForm
from user.models import Comment
from .models import Product, ProductCategory


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product, ProductCategory, ProductCharacteristics # Assuming ProductCharacteristic is your model for characteristics like color/size

def product_list(request):
    products_list = Product.objects.all()

    # По Категориям
    selected_category_slug = request.GET.get('category')
    if selected_category_slug:
        products_list = products_list.filter(category__slug=selected_category_slug)

    # ПО Цвету
    selected_color = request.GET.get('color')
    if selected_color:
        products_list = products_list.filter(product_characteristics__title='Цвет', product_characteristics__value=selected_color)

    # По Размеру
    selected_size = request.GET.get('size')
    if selected_size:
        products_list = products_list.filter(product_characteristics__title='Размер', product_characteristics__value=selected_size)

    # По Цене
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products_list = products_list.filter(price__gte=min_price)
    if max_price:
        products_list = products_list.filter(price__lte=max_price)

    # Фильтр НА ВВЕРХУ
    sort_by = request.GET.get('sort', 'default') # Default sort
    if sort_by == 'popularity':
        products_list = products_list.order_by('-created_at')
    elif sort_by == 'price-asc':
        products_list = products_list.order_by('price')
    elif sort_by == 'price-desc':
        products_list = products_list.order_by('-price')
    elif sort_by == 'newest':
        products_list = products_list.order_by('-created_at')
    else:
        products_list = products_list.order_by('-created_at')

    products = products_list
    categories = ProductCategory.objects.all()
    available_sizes = ProductCharacteristics.objects.filter(title='Размер').values_list('value', flat=True).distinct().order_by('value')


    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category_slug,
        'selected_color': selected_color,
        'selected_size': selected_size,
        'min_price': min_price,
        'max_price': max_price,
        'sort_by': sort_by,
        'available_sizes': available_sizes,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.product_images.all()
    characteristics = product.product_characteristics.all()
    category = product.category
    add_to_cart_form = AddToCartForm(initial={'product_id': product.id, 'quantity': 1})

    comments = product.comments.all()

    if request.method == 'POST':
        if 'add_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.products = product
                new_comment.author = request.user
                new_comment.save()
                return redirect('shop:product_detail', product_id=product.id)
        else:
            pass
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'images': images,
        'characteristics': characteristics,
        'category': category,
        'add_to_cart_form': add_to_cart_form,
        'reviews': comments,
        'review_form': comment_form,
    }
    return render(request, 'shop/product-detail.html', context)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author or request.user.is_superuser:
        if request.method == 'POST':
            product_id = comment.products.id
            comment.delete()
            return redirect('shop:product_detail', product_id=product_id)
        return redirect('shop:product_detail', product_id=comment.products.id)
    else:
        return HttpResponseForbidden("У вас нет прав для удаления этого комментария.")