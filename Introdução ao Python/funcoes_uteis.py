def soma(a, b, c):
    soma = a + b + c
    return soma

def multiplica(a, b, c):
    mult = a * b * c
    return mult

#implementamos pelo Colab...
def divisao(a, b):
  div = a / b
  return div

def ePalindromo(string):
    if(string == string[::-1]):
        return True
    return False