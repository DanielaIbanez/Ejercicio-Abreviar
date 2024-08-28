numero= int (input())
letras =[]




for i in range(numero):
    letra = input()
    letras.append(letra)

for letra in letras:
    if len(letra) > 10 :
        abreviatura= letra [0]+str(len(letra)-2)+letra[-1]
        print(abreviatura)
    else:
        print(letra)
