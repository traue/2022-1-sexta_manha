def soma(a, b, c):
    soma = a + b + c
    return soma

def multiplica(a, b, c):
    mult = a * b * c
    return mult

def ePalindromo(string):
    if(string == string[::-1]):
        return True
    return False