from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)  # выбрать количество продуктов
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)  # скрытй параметр для управления обновление количества


class MessageSendForm(forms.Form):
    # mess_text = forms.Textarea()
    mess_text = forms.CharField(label='Your text', max_length=100, widget=forms.Textarea)
