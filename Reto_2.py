def sonido_grillo(temp: float, hembra:bool):

    cantidad_crics= 4*(temp - 4.5)

    if temp <= 4.70:
        return {'crics': 'grillo muere', 'hembra': 'grillo hembra muere'}

    elif hembra == True:
        return {'crics': {cantidad_crics*2}, 'hembra': 'hembra presente'}

    return {'crics': {cantidad_crics}, 'hembra': 'hembra ausente'}

 



print(sonido_grillo(4.80, False))