from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(label= 'Nome de login',
                               required = True,widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite seu nome de login"}
                               ),
                               max_length = 100)
    Senha1 = forms.CharField(label= 'senha',
                               required= True,
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha"}
                               ),
                               max_length = 100)   



class CadastroForms(forms.Form):
    username = forms.CharField(label= 'Nome de login',
                               required = True,widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite seu nome de login"}
                               ),
                               max_length = 100)
    Senha1 = forms.CharField(label= 'senha',
                               required= True,
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha"}
                               ),
                               max_length = 100)   

    Senha2 = forms.CharField(label= 'Senha',
                               required = True,widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "confirme senha"}
                               ),
                               max_length = 100)    

    email = forms.EmailField(label='E-mail',
                             required=True, widget=forms.EmailInput(
                                 attrs={"class": "form-control",
                                        "placeholder": "Digite seu e-mail"}
                             ),
                             max_length=100)
     
    