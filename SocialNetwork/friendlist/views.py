from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import FriendList, Friend
from users.models import CustomUser
# from .forms import MessageSendForm
# from goods.models import Product
# from goods.serializers import ProductSerializer
# from .models import Cart, CartItem
# from .forms import CartAddProductForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from .serializers import CartSerializer, CartItemSerializer, CartItemSerializer2
from collections import OrderedDict
# from .forms import MessageSendForm


# Create your views here.
def friend_list(request, user_id):
    try:
        owner = CustomUser.objects.get(id=user_id)
        friends_list = FriendList.objects.get(owner=owner)
        friends = Friend.objects.filter(f_list_id=friends_list)
    except FriendList.DoesNotExist:
        return HttpResponse(status=404)
    except Friend.DoesNotExist:
        return HttpResponse(status=404)
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'friendlist/friends/list.html', {'friends': friends})


# @require_POST
# def send_message(request):
#     # cart = Cart(request)
#     # product = get_object_or_404(Product, id=product_id)
#     # form = CartAddProductForm(request.POST)
#     # if form.is_valid():
#     #     cd = form.cleaned_data
#     #     cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#     # return redirect('cart:cart_detail')
#     print(request.POST)
#     message_form = MessageSendForm(request.POST)
#     dialog = Dialog.objects.get(sender=1, recipient=1)
#     if message_form.is_valid():
#         cd = message_form.cleaned_data
#         print(cd.get('mess_text'))
#         new_message = Message.create(dialog, cd.get('mess_text'))
#         new_message.save()
#         return HttpResponse(status=204)
#     else:
#         return HttpResponse(status=404)
#
#
# def remove_message(request, message_id):
#     try:
#         message = Message.objects.get(id=message_id)
#     except Message.DoesNotExist:
#         # return Response(status=status.HTTP_404_NOT_FOUND)
#         return HttpResponse(status=404)
#     if request.method == 'DELETE':
#         # cart = Cart(request)
#         message.delete()
#         print("NESOSI")
#         return HttpResponse(status=204)
#         # return Response(status=status.HTTP_204_NO_CONTENT)
#         # cart.remove(product)
#         # return redirect('cart:cart_detail')
#     else:
#         print("SOSIIII")
