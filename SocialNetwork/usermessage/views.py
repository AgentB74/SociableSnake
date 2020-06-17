from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Message, Dialog
# from .forms import MessageSendForm
# from goods.models import Product
# from goods.serializers import ProductSerializer
# from .models import Cart, CartItem
# from .forms import CartAddProductForm

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from .serializers import CartSerializer, CartItemSerializer, CartItemSerializer2
from collections import OrderedDict
from .forms import MessageSendForm
from users.models import CustomUser


# Create your views here.
def message_list(request, owner_id):
    try:
        owner = CustomUser.objects.get(id=owner_id)
        dialog = Dialog.objects.get(sender=owner)
        messages = Message.objects.filter(dialog_id=dialog)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        return HttpResponse(status=404)
    # for message in messages:
    #     message['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'usermessages/umessages/messageList.html',
                  {'messages': messages, 'owner': owner, 'form': MessageSendForm})


@require_POST
def send_message(request):
    # cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    # form = CartAddProductForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    # return redirect('cart:cart_detail')
    print(request.POST)
    message_form = MessageSendForm(request.POST)
    dialog = Dialog.objects.get(sender=1, recipient=1)
    if message_form.is_valid():
        cd = message_form.cleaned_data
        print(cd.get('mess_text'))
        new_message = Message.create(dialog, cd.get('mess_text'))
        new_message.save()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)


def remove_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        message.delete()
        return HttpResponse(status=204)

# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})
