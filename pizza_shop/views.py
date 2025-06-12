from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart, CartItem, Order
from .forms import OrderForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f'Đã thêm {product.name} vào giỏ hàng!')
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.get_total_price() for item in items)
    return render(request, 'cart.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def checkout_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()
        total = sum(item.get_total_price() for item in items)
    except Cart.DoesNotExist:
        messages.error(request, "Giỏ hàng của bạn đang trống.")
        return redirect('home')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.cart = cart
            order.save()
            messages.success(request, "Đặt hàng thành công!")
            return redirect('home')
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form, 'cart': cart, 'total': total})
@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart_view')

@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart_view')
