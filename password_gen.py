import random
import FreeSimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        print("Iniciando aplicação...")
        try:
            sg.theme('DarkAmber')
        except Exception as e:
            print(f"Erro ao definir tema: {e}")
            sg.theme('Default')
        layout = [
            [sg.Text('Site/Software Name', size=(10, 1)), sg.InputText(key='site_name', size=(20, 1))],
            [sg.Text('Email/Username', size=(10, 1)), sg.InputText(key='username', size=(20, 1))],
            [sg.Text('Password Length', size=(15, 1)), sg.Slider(range=(8, 32), orientation='h', size=(15, 15), default_value=12, key='length')],
            [sg.Checkbox('Incluir Letras Maiúsculas', default=True, key='uppercase')],
            [sg.Checkbox('Incluir Números', default=True, key='numbers')],
            [sg.Checkbox('Incluir Símbolos', default=True, key='symbols')],
            [sg.Button('Gerar Senha'), sg.Button('Sair')],
            [sg.Text('Senha Gerada:', size=(15, 1)), sg.InputText(key='generated_password', size=(30, 1))],

        ]

        self.janela = sg.Window('Gerador de Senhas', layout)
        print("Janela criada com sucesso")

    def Iniciar(self):
        print("Iniciando loop de eventos...")
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Sair':
                break
            if evento == 'Gerar Senha':
                site_name = valores['site_name']
                username = valores['username']
                length = int(valores['length'])
                
                characters = 'abcdefghijklmnopqrstuvwxyz'
                if valores['uppercase']:
                    characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                if valores['numbers']:
                    characters += '0123456789'
                if valores['symbols']:
                    characters += '!@#$%^&*()_+-=[]{}|;:,.<>?'
                
                password = ''.join(random.choice(characters) for _ in range(length))
                
                self.janela['generated_password'].update(password)
                
                if site_name:
                    with open('passwords.txt', 'a', encoding='utf-8') as f:
                        f.write(f'Site: {site_name} | User: {username} | Password: {password}\n')
        
        self.janela.close()

try:
    print("Criando gerador de senhas...")
    gen = PassGen()
    gen.Iniciar()
except Exception as e:
    print(f"Erro ao executar programa: {e}")
    import traceback
    traceback.print_exc()
    input("Pressione Enter para sair...")