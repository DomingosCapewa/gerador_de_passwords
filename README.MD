# Gerador de Senhas 

Um gerador de senhas seguras com interface gráfica desenvolvido em Python usando FreeSimpleGUI.

## Descrição

Este programa permite gerar senhas aleatórias e seguras com opções personalizáveis de comprimento e tipos de caracteres. Todas as senhas geradas podem ser automaticamente salvas em um arquivo local para referência futura.

## Funcionalidades

- **Geração de senhas aleatórias** com comprimento personalizável (8 a 32 caracteres)
- **Opções de personalização:**
  - Incluir/excluir letras maiúsculas
  - Incluir/excluir números
  - Incluir/excluir símbolos especiais
- **Armazenamento automático** das senhas em arquivo `passwords.txt`
- **Interface gráfica intuitiva** e fácil de usar
- **Registro de informações:** site/software e usuário associados à senha

## Requisitos

- Python 3.7 ou superior
- FreeSimpleGUI

## Instalação

1. Clone ou baixe este repositório

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
.venv\Scripts\activate

source .venv/bin/activate
```

4. Instale a dependência necessária:
```bash
pip install FreeSimpleGUI
```

## Como Usar

1. Execute o programa:
```bash
python password_gen.py
```

2. Na interface que será aberta:
   - Digite o nome do site/software (opcional)
   - Digite o email/usuário (opcional)
   - Ajuste o comprimento da senha usando o slider (8-32 caracteres)
   - Marque/desmarque as opções desejadas:
     - Incluir Letras Maiúsculas
     - Incluir Números
     - Incluir Símbolos
   - Clique em "Gerar Senha"
   - A senha gerada aparecerá no campo "Senha Gerada"

3. Se você informou o nome do site, a senha será automaticamente salva no arquivo `passwords.txt` no formato:
```
Site: exemplo.com | User: usuario@email.com | Password: Abc123!@#
```

## Estrutura do Projeto

```
password_gen/
│
├── password_gen.py    # Código principal do programa
├── README.MD          # Documentação (este arquivo)
└── passwords.txt      # Arquivo gerado automaticamente com as senhas (criado ao usar)
```

## ⚙️ Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **FreeSimpleGUI** - Biblioteca para interface gráfica (fork gratuito do PySimpleGUI)
- **random** - Módulo para geração de números aleatórios

## Segurança

**Importante:** Este programa armazena as senhas em texto simples no arquivo `passwords.txt`. Para uso em produção, considere:
- Implementar criptografia para o arquivo de senhas
- Usar um gerenciador de senhas profissional
- Não compartilhar o arquivo `passwords.txt` com terceiros

## Notas

- O arquivo `passwords.txt` é criado automaticamente na primeira vez que você gera uma senha com um nome de site informado
- As senhas são geradas de forma aleatória e não são verificadas quanto à força ou conformidade com políticas específicas
- O programa só salva as senhas quando o campo "Site/Software Name" está preenchido

##  Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é de código aberto e está disponível para uso pessoal e educacional.

## 👨‍💻 Autor

Desenvolvido como projeto de estudo em Python.

