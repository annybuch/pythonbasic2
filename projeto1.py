print('Bem vindo a companhia de logística Raiany Cristina S.A')

# Inicio da função dimensoesObjeto()
def dimensoesObjeto():
  while True:
    try:
      altura = float(input('Digite a altura do objeto (em cm): '))
# float, pois, pode ter números não inteiros.
      comprimento = float(input('Digite o comprimento do objeto (em cm): '))
      largura = float(input('Digite a largura do objeto (em cm): '))
      volume = altura * comprimento * largura    # descobrir o volume do objeto em cm^3.
      print('O volume do objeto é (em cm^3): {}' .format(volume))
      if volume < 1000:   # Se volume for menor que 1000, retornar 10.
        return 10
      elif 1000 <= volume < 10000:
        return 20
      elif 10000 <= volume < 30000:
        return 30
      elif 30000 <= volume < 100000:
        return 50
      else:
        print('''
Não aceitamos objetos com valor tão grandes
Entre com as dimensões desejadas novamente
        ''')
        continue   # Continue para voltar no começo do while.
    except ValueError:    # Exeção para o ValueError para o caso de digitação errada.
      print('''
Você digitou alguma dimensão com um valor não numérico
Por favor, entre com os valores novamente 
''')
# Fim da função dimensoesObjeto()

# inico da função pesoObjeto()
def pesoObjeto():
   while True:
    try:
      peso = float(input('Digite o peso do objeto (em kg): '))  # Solicita ao usuário que insira o peso do objeto em quilogramas
      if peso <= 0.1:
        return 1
      elif 0.1 <= peso < 1:
        return 1.5
      elif 1 <= peso < 10:
        return 2
      elif 10 <= peso < 30:
        return 3
      else:
        print('''
Não aceitamos objetos tão pesados
Entre com as dimensões desejadas novamente
        ''')
        continue            # Continue para voltar no começo do while.
    except ValueError:      # Trata a exceção ValueError caso o usuário digite um valor não numérico
      print('''
Você digitou o peso do objeto com um valor não numérico
Por favor, entre com o peso desejado novamente   
      ''')
# fim da função pesoObjeto()

# inicio da função rotaObjeto()
def rotaObjeto():
     while True:
      rota = input('''
Selecione a rota:
RS - De Rio de Janeiro até São Paulo
SR - De São Paulo até Rio de Janeiro
BS - De Brasília até São Paulo
SB - De São Paulo até Brasília
BR - De Brasília até Rio de Janeiro
  ''')
      if rota == 'RS':    # Se a rota digitada for RS, retornar 1.
        return 1
      elif rota == 'SR':
        return 1
      elif rota == 'BS':
        return 1.2
      elif rota == 'SB':
        return 1.2
      elif rota == 'BR':
        return 1.5
      else:
        print('''
Você digitou uma rota que não existe,
Entre com a rota novamente
        ''')
        continue
# fim da função rotaObjeto()

# inicio main
print()
volume = dimensoesObjeto()    # Chama a função para obter o volume do objeto
peso = pesoObjeto()           # Chama a função para obter o peso do objeto
rota = rotaObjeto()           # Chama a função para obter a rota do objeto
# Total a pagar
total = volume * peso * rota  # Calcula o total a pagar multiplicando o volume, peso e rota.
print('Total a pagar: R$ {:.2f} (Dimensões: {} * Peso: {} * Rota: {})' .format(total, volume, peso, rota))