from django.db import models
from users.models import CustomUser


# Create your models here.
class FriendList(models.Model):
    # владелец этого списка друзей
    owner = models.OneToOneField(CustomUser, related_name='friend_list', on_delete=models.CASCADE)

    def __str__(self):
        return 'FriendList {}'.format(self.id)


class Friend(models.Model):
    # Привязка к конкретному френдлисту
    f_list_id = models.ForeignKey(FriendList, related_name='friends', on_delete=models.CASCADE)
    # id друга
    friend_id = models.ForeignKey(CustomUser, related_name='friend', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('f_list_id', 'friend_id'),)

    def __str__(self):
        return '{}'.format(self.id)

    @classmethod
    def create(cls, f_list_id, friend_id):
        order_item = cls(f_list_id=f_list_id, friend_id=friend_id)
        return order_item

#
# class Status(models.Model):
#     # Статус (лучший друг, приятель, коллега)
#     friend_status = models.CharField(max_length=50, db_index=True)
#
#     class Meta:
#         ordering = ('status',)
#
#     def __str__(self):
#         return self.friend_status
#
#
# class FriendStatus(models.Model):
#     friend = models.ForeignKey(Friend, related_name='friend_status', on_delete=models.CASCADE)
#     friend_status = models.ForeignKey(Status, related_name='f_status', on_delete=models.CASCADE)
#     order_status_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         unique_together = (('friend', 'friend_status'),)
