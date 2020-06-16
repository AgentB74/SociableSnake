from django.db import models
from users.models import CustomUser


# Create your models here.
class Dialog(models.Model):
    # пользователь, который отправил сообщение
    sender = models.ForeignKey(CustomUser, related_name='message_sender', on_delete=models.CASCADE)
    # пользователь, который получил сообщение
    recipient = models.ForeignKey(CustomUser, related_name='message_recipient', on_delete=models.CASCADE)

    def __str__(self):
        return 'Dialog {}'.format(self.id)


class Message(models.Model):
    # Привязка к конкретному диалогу
    dialog_id = models.ForeignKey(Dialog, related_name='messages', on_delete=models.CASCADE)
    # текст сообщения
    message_text = models.TextField(blank=True)
    # дата написания сообщения
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # дата обновления сообщения (дата обновления текста сообщения)
    updated = models.DateTimeField(auto_now=True)

    # Прочтено ли сообщение
    # read = models.BooleanField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{}'.format(self.id)

    @classmethod
    def create(cls, dialog_id, message_text):
        order_item = cls(dialog_id=dialog_id, message_text=message_text)
        return order_item

