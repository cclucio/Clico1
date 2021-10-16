from math import sqrt

a = 1
b = 1
c = -30
X_1 = -3
x_2 = 4
x_3 = 1
x_4 = -1

def parabola(a,b,c,X_1,x_2,x_3,x_4):

    
    def corte_eje_y():
     
        corte_y = c

        return corte_y

    def corte1_eje_x():

        corte_1 = (-b + sqrt(b*b - 4*(a*c))) / (2*a)

        return corte_1

    def corte2_eje_x():

        corte_2 = (-b - sqrt(b*b - 4*(a*c))) / (2*a)

        return corte_2

    def vertice():

        vertice_x = -b / (2*a)
        vertice_y = (a*(vertice_x**2)) + (b*vertice_x) + c

        return (vertice_x, vertice_y)     

    def imagenes_del_dominio():

        dom_x1 = (a*(X_1**2)) + (b*X_1) + c
        dom_x2 = (a*(x_2**2)) + (b*x_2) + c
        dom_x3 = (a*(x_3**2)) + (b*x_3) + c
        dom_x4 = (a*(x_4**2)) + (b*x_4) + c

        return (dom_x1,dom_x2,dom_x3,dom_x4)

    return (f"los puntos de corte con el eje Y,X son respectivamente{corte_eje_y(),corte1_eje_x(),corte2_eje_x()} \nlas cordenadas del vertice son {vertice()}\nlos valores de y evaluados son:{imagenes_del_dominio()}") 
