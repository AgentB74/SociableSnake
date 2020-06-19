from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Message, Dialog, MessageText
from collections import OrderedDict
from .forms import MessageSendForm
from users.models import CustomUser


# Create your views here.
def message_list(request, part1, part2):
    try:
        owner1 = CustomUser.objects.get(id=part1)
        owner2 = CustomUser.objects.get(id=part2)
        dialog = Dialog.objects.get(
            Q(participant1=owner1, participant2=owner2) | Q(participant1=owner2, participant2=owner1))
        messages = Message.objects.filter(dialog_id=dialog)
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        print()
        new_dialog = Dialog.create(owner1, owner2)
        new_dialog.save()
        messages = Message.objects.filter(dialog_id=new_dialog)
        return render(request, 'usermessages/umessages/messageList.html',
                      {'messages': messages, 'dialog': new_dialog, 'form': MessageSendForm})
    # for message in messages:
    #     message['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'usermessages/umessages/messageList.html',
                  {'messages': messages, 'dialog': dialog, 'form': MessageSendForm})


def dialog_list(request, owner_id):
    try:
        owner = CustomUser.objects.get(id=owner_id)
        dialog = Dialog.objects.filter(Q(participant1=owner) | Q(participant2=owner))
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'usermessages/umessages/dialogList.html',
                  {'dialogs': dialog})


@require_POST
def send_message(request, sen_id, rec_id):
    print(request.POST)
    message_form = MessageSendForm(request.POST)
    owner1 = CustomUser.objects.get(id=sen_id)
    owner2 = CustomUser.objects.get(id=rec_id)
    dialog = Dialog.objects.get(
        Q(participant1=owner1, participant2=owner2) | Q(participant1=owner2, participant2=owner1))
    print(dialog.id)
    if message_form.is_valid():
        cd = message_form.cleaned_data
        print(cd.get('mess_text'))
        new_text = MessageText.create(cd.get('mess_text'))
        new_text.save()
        print(new_text)
        new_message = Message.create(dialog, owner1, owner2, new_text)
        new_message.save()
        messages = Message.objects.filter(dialog_id=dialog)
        return redirect('message:message_list', part1=sen_id, part2=rec_id)
        # return render(request, 'usermessages/umessages/messageList.html',
        #               {'messages': messages, 'dialog': dialog, 'form': MessageSendForm})
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


def remove_dialog(request, sen_id, rec_id):
    try:
        owner1 = CustomUser.objects.get(id=sen_id)
        owner2 = CustomUser.objects.get(id=rec_id)
        dialog = Dialog.objects.get(
            Q(participant1=owner1, participant2=owner2) | Q(participant1=owner2, participant2=owner1))
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    except Dialog.DoesNotExist:
        return HttpResponse(status=404)
    print("sas")
    dialog.delete()
    # return HttpResponseRedirect(redirect('message:dialogs', owner_id=owner1.id))
        # print("sas")
    return redirect('message:dialogs', owner_id=sen_id)

# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})
