def isVogal(letra):
    if letra.lower() in "aeiouáéíóúãẽĩõũâêîôûàèìòùäëïöü":
        return True
    else:
        return False


vogais = []

with open('Exercicios\Capitulo05\\faroeste.txt', 'r') as letra:
    arquivo = letra.readlines()
    for linha in arquivo:
        for word in linha.split(' '):
            for letter in word:
                if isVogal(letter) == True:
                    vogais.append(letter)
                
print(len(vogais))
