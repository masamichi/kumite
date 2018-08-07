from django import forms


from menu.models import Tea, TEA_KINDS

class TeaSearchForm(forms.Form):
    name = forms.CharField(label="名前", max_length=255)
    kind = forms.MultipleChoiceField(
        label="種類", choices=TEA_KINDS, required=False
    )

    def clean(self):
        if not self.is_valid():
            return self.cleaned_data

        if not self.cleaned_data["name"] and not self.cleaned_data["kind"]:
            raise forms.ValidationError('名称と種類のどちらかは入力してください')
        return self.cleaned_data