from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(label= 'Nome de login',
                               required = True,widget = forms.TextInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite seu nome de login"}
                               ),
                               max_length = 100)
    senha1 = forms.CharField(label= 'senha',
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
    senha_1 = forms.CharField(label= 'senha',
                               required= True,
                               widget = forms.PasswordInput(
                                   attrs={"class": "form-control",
                                          "placeholder": "Digite sua senha"}
                               ),
                               max_length = 100)   

    senha_2 = forms.CharField(label= 'Senha',
                               required = True,widget = forms.PasswordInput(
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
    def clean_username(self):
        name = self.cleaned_data['username']
        if name:
            name = name.strip()
        if " " in name:
            raise forms.ValidationError("O nome de usuário não pode conter espaços")
        elif " " in name:
            raise forms.ValidationError("O usuario nao pode ser vazio!") 
        elif "!" in name:
            raise forms.ValidationError("O usuario nao pode conter caracteres especiais!")
        else:
            return name 
               
    def clean_senha_2(self):
        senha_1 = self.cleaned_data['senha_1']
        senha_2 = self.cleaned_data['senha_2']
        if senha_1 != senha_2:
            raise forms.ValidationError("As senhas não conferem")
        return senha_2
        