



def desafio001():
  print('Olá mundo')

def desafio002():
  nome = input ('Qual é seu nome?')
  print('Olá',nome,'!','Seja bem vindo!')
  
def desafio003():
  n1 = int(input('Digite um valor:'))
  n2 = int(input('DSigite outro valor:'))
  s = n1+n2
  print('O valor é:',s)


def desafio004():
  a = input('Digite algo:')
  print('O tipo primitivo desse vlor é:')
  print('Só possui letras Maiúsculas?', a.isupper())
  print('Possui apenas números?', a.isnumeric())
  print('Possui apenas letras?', a.isalpha())
  print('É alfanumérico?', a.isalnum())
  print('É somente espaços?', a.isspace())


def desafio005():
  n = int(input('Digite um Número inteiro:'))
  n1 = n-1
  n2 = n+1
  print('O antecessor desse número é:{}'.format(n1))
  print('O sucessor desse número é:{}'.format(n2))

def desafio006():
  n = int(input('Digite um número:'))
  d = n*2
  t = n*3
  r = n**(1/2)
  print(' O dobro desse valor é:{} \n O triplo desse valor é:{} \n A raiz quadrada desse valor é:{}'.format(d, t, r))

def desafio007():
  nota1 = float(input('Digite Sua Nota:'))
  nota2 = float(input('Digite Sua Outra Nota:'))
  media = (nota1 + nota2)/2
  print('Sua média é:{}'.format(media))
  
def desafio008():
  m = float(input('Digite a de metros:'))
  c = m*100
  mi = m*1000
  print('Seu valor em centimetros é:{} \n Seu valor em milimetros é:{}'.format(c, mi))
  
def desafio009():
  n = int(input('Digite um número inteiro:'))
  n0 = n*0
  n1 = n*1
  n2 = n*2
  n3 = n*3
  n4 = n*4
  n5 = n*5
  n6 = n*6
  n7 = n*7
  n8 = n*8
  n9 = n*9
  n10 = n*10
  print('Atabuada desse número{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))
  
def desafio010():
  n = float(input('Quanto dinheiro você tem em reais?'))
  d = n*3.27
  print('Você pode comprar {} dólares'.format(d))
  
def desafio011():
  a = float(input('Digite a altura da parede:'))
  l = float(input('Digite a largura da parede:'))
  area = a*l
  pp = area/2
  print('A área da sua parede é de {}'.format(area))
  print('Litros de tinta necessários para pinta-la:{}'.format(pp))
  
def desafio012():
  p1 = float(input('Digite o preço do produto:'))
  desconto = p1*5/100
  pf = p1-desconto
  print('O preço com desconto é de {}'.format(pf))
  
def desafio013():
  s = float(input('Digite seu salário:'))
  s2 = s*15/100
  sf = s+s2
  print('Seu salário será de:{}'.format(sf))

def desafio014():
  tc = float(input('Digite a temperatura:'))
  tf = (tc*9/5)+32
  print('A temperatura em fahrenheit é de:{}'.format(tf))

def desafio015():
  km = float(input('Quantos km foram percorridos?'))
  dias = float(input('Por quantos dias esse carro foi alugado?'))
  ckm = km*0.15
  cd = dias*60
  ct = cd+ckm
  print('O valor total é de:{}'.format(ct))

def desafio016():
  import math


  n = float(input('Digite um número:'))
  ni = math.floor(n)
  print('A parte inteira do número é:{}'.format(ni))

def desafio017():
  import math

  co = int(input('Digite o comprimento do cateto oposto:'))
  ca = int(input('digite o comprimento do cateto adjacente:'))
  h = (co**2)+(ca**2)
  print('A hipotenusa mede:{}'.format(h))

def desafio018():
  import math

  a = float(input('Digite o ângulo desejado:'))
  seno = math.sin(math.radians(a))
  coseno = math.cos(math.radians(a))
  tangente = math.tan(math.radians(a))
  print('O seno do ângulo é:{}\n O coseno é:{}\n A tangente é:{}'.format(seno, coseno ,tangente))

def desafio019():
  import random

  a1 = input('Digite o nome de um aluno:')
  a2 = input('Digite o nome de outro aluno:')
  a3 = input('Digite o nome de outro aluno:')
  a4 = input('Digite o nome de outro aluno:')

  lista = [a1, a2, a3, a4]
  escolhido = random.choice(lista)

  print('O aluno escolhido foi:{}',format(escolhido))

def desafio020():
  import random


  n1 = input('Primeiro nome: \n')
  n2 = input('Segundo nome: \n')
  n3 = input('Terceiro nome: \n')
  n4 = input('Quarto nome: \n')
  lista = [n1, n2, n3, n4]

  random.shuffle(lista)

  print('A ordem é:')
  print(lista)
  
def desafio021():
  print('questão anulada hehe')

def desafio022():
  nome = input('Qual o seu nome? ')
  print('Tudo maiúsculo: {}'.format(nome.upper()))
  print('Tudo minúsculo: {}'.format(nome.lower()))
  lista = nome.split()
  print('O nome completo possui {} letras'.format(len(''.join(lista))))
  print('O seu primeiro nome é {} e possui {} letras'.format(lista[0], 
  len(lista[0])))

def desafio023():
  pergunta = int(input('Digite um numero: '))
  soma = 10000 + pergunta
  resultado = str(soma)
  uni = resultado[4]
  dez = resultado[3]
  cen = resultado[2]
  mil = resultado[1]
  print('Unidade: {}'.format(uni))
  print('Dezena: {}'.format(dez))
  print('Centena: {}'.format(cen))
  print('Milhar: {}'.format(mil))

def desafio024():
  c = str(input('Digite sua cidade: ')).lower().strip()
  print('santo' in c)
  
def desafio025():
  nome = str(input('Qual o seu nome? ')).strip()
  print('Seu nome possui "SILVA"? {}'.format('SILVA' in 
  nome.upper().split()))

def desafio026():
  nome = str(input('Digite seu nome:')).upper().strip()
  cont = nome.count('A')
  conta = nome.find('A')
  con = nome.rfind('A')
  print('O nome tem {} no total,\nO primeiro A aparece na {} posição, \nO ultimo A aparece na {} posição'.format(cont, conta, con))
  
def desafio027():
  nome = input('Qual o seu nome completo? ')
  m = nome.split()
  print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')

def desafio028():
  from random import choice
  print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
  lista=[0,1,2,3,4,5]
  escolha=choice(lista)
  n1=int(input('Em que número eu pensei? '))
  print('PROCESSANDO...')
  if n1 == escolha:
      print('PARABÉNS! Você conseguiu me vencer!')
  else:
      print('GANHEI! Eu pensei no número {} e não no {}'.format(escolha,n1))
  print('--FIM--')
  
def desafio029():
  print("=" * 85)
  print("Velocidade máxima da via = 80")
  print("Velocidade mínima da via = 40")
  print("=" * 85)

  C = int(input("A velocimetro está em? "))

  if(C <= 80 and C >= 40):
      print("Se beber não dirija")
  elif(C < 40):
      print("Abaixo da velocidade permitida")
  else:
      print("Acima da velocidade permitida")
      C = C - 80
      print(f"Você foi multado em R${C * 7:.2f}")

def desafio030():
  número = int(input('me diga um número qualquer: '))
  if número % 2 == 0:
      print(número,'é par.')
  else:
      print(número,'é impar.')

def desafio031():
  km = float(input('Qual a distância em (Km) você deseja percorrer? '))
  if km <= 200:
      print('Sua passagem vai custar {} reais. '.format(km * 0.5))
  else:
      print('Sua passagem vai custar {} reais. '.format(km * 0.45))

def desafio032():
  x = int(input('Digite um ano qualquer: '))
  if x%4 == 0:
      if x%100 != 0:
          print('Esse ano é bissexto.')
      else:
          if x%400 != 0:
              print('Esse ano não é bissexto.')
          else:
              print('Esse ano é bissexto.')
  else:
      print('Esse ano não é bissexto.')
  
def desafio033(): 
  n1 =int(input('digite o primeiro número:  '))
  n2 =int(input('Digite o segundo número: '))
  n3 =int(input ('Digite o terceiro número: '))

  lista =[n1,n2,n3]
  lista_ordenada = sorted(lista)

  print('O menor número é {}'.format(lista_ordenada[0]))
  print ('O maior número é {}'.format(lista_ordenada[2]))

def desafio034():
  val = float(input('Entre com o salário do funcionário: '))
  sal = val * 1.10 if val > 1250 else val * 1.15
  print('Quem ganhava R${} passa a ganhar {:.2f}'.format(val, sal))

def desafio035():
  a = float(input('Coloque o valor de um lado: '))
  b = float(input('Coloque o valor de outro lado: '))
  c = float(input('Coloque o valor de outro lado: '))

  if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
      print('Os lados {}, {} e {} podem formar triângulo.'.format(a,b,c))
  else:
      print('Os lados {}, {} e {} não podem formar triângulo.'.format(a,b,c))
  