from django import forms
from member.models import Member


class MemberLoginForm(forms.Form):
    member_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MemberSignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['member_id', 'password1', 'password2', 'name']

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError("비밀번호가 다릅니다.")

        return password1
