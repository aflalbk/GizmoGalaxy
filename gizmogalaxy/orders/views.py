from django.shortcuts import render, redirect
from . models import Order, OrderedItem
from product.models import Product
from django.contrib import messages

# Create your views here.
def order(request):
    customer = request.user
    user_cart, create = Order.objects.get_or_create(owner=customer, order_status = Order.cart_stage)

    return render(request, 'order.html', {'user_cart':user_cart})

def add_to_cart(request):
    if request.POST:
        customer = request.user
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        cart_obj, created = Order.objects.get_or_create(owner=customer, order_status = Order.cart_stage)

        order_item_obj , created = OrderedItem.objects.get_or_create(
            product = Product.objects.get(pk=product_id),
            owner = cart_obj
        )
        if created:
            order_item_obj.quantity = quantity
            order_item_obj.save()
        else:
            order_item_obj.quantity = order_item_obj.quantity + int(quantity)
            order_item_obj.save()


        return redirect('order')
    return render(request, 'product_list.html')

def remove_item(request, pk):
    orderd_item = OrderedItem.objects.get(id=pk)
    orderd_item.delete()
    return redirect('order')

def proceed_to_buy(request):
    if request.POST:
        try:    
            customer = request.user
            total = float(request.POST.get('total'))
            print(total)

            cart_obj = Order.objects.get(owner=customer, order_status=Order.cart_stage)


            if cart_obj:
                cart_obj.order_status = Order.order_confirmed
                cart_obj.total_price = total
                cart_obj.save()
                status_message='Your order is processed. Your item will be delivered in 2 days.'
                messages.success(request, status_message)
            else:
                print("ABCDF")
                status_message = "Unable to process. No items in your cart."
                messages.error(request, status_message)
        except Exception as e :
            print(e)
            print("this is working")
            status_message = "Unable to process. No items in your cart."
            messages.error(request, status_message)
    return redirect('order')


