frase= "la casa es la oficina"
palabra= "la"

def conteo_letras(frase: str, palabra: str) -> list:
    frase_2= [len(i) for i in frase.split(" ") if i != palabra]
    return frase_2

print(conteo_letras(frase, palabra))