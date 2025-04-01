import random
import string
def rm():
    return random.randint(0,9)

print("MENU\n 1.creador de contraseñas\n 2.identificador de cuadrantes\n 3.salir")
while True:
    r=input("ingrese el numero de la accion a realizar\n")
    r=int(r)
    if r== 1:
        print("selecciono el creador de contraseñas\n para la creacion de una contraseña de 8 caracteres se le pedira que ingrese de 3 palabras\n")
        p1=input("introduce la primer palabra\n")
        p2=input("introduce la segunda palabra\n")
        p3=input("itroduce la tercer palabra\n")
        if len(p1)< 2:
            p1=p1+str(rm())
        if len(p2)< 2:
            p2=p2+str(rm())
        if len(p3)< 2:
            p3=p3+str(rm())
        p=p1+p2+p3
        lc=8
        c=''.join(random.choice(p) for _ in range(lc))
        print("la contraseña generada es:\n" +c)
        print("favor de ingresar la contraseña generada para su confirmacion\n")
        cu=input()
        if len(cu)<len(c):
            print("faltan ",len(c)-len(cu)," caracteres")
        elif len(cu)>len(c):
            print("sobran ",len(cu)-len(c)," caracteres")
        elif len(cu)==len(c):
            print("la contraseña a sido confirmada")
        else:
            print("la contraseña es incorrecta")
    elif r==2:
        print("selecciono identificador de cuadrantes\n favor de ingresar las coordenadas\n")
        while True:
            while True:
                x=input("ingrese coordenada X")
                x=int(x)
                if x==0:
                    print("ingrese un numero deferente a 0")
                else:
                 break
            while True:
                y=input("ingrese coordenada Y")
                y=int(y)
                if y==0:
                    print("ingrese un numero deferente a 0")
                else:
                  break
            if x<0 and y<0:
                print("la coordenada ingresada se encuentra en el cuadrante 3")
            elif x>0 and y>0:
                print("la coordenada ingresada se encuentra en el cuadrante 1")
            elif x<0 and y>0:
                print("la coordenada ingresada se encuentra en el cuadrante 2")
            elif x>0 and y<0:
                print("la coordenada ingresada se encuentra en el cuadrante 4")
            rep=input("desea ingresar otra coordenada?\n 1.si\n 2.no\n")
            rep=int(rep)
            if rep==2:
                break
            else:
                print("favor de ingresar las coordenadas\n")
    elif r==3:
        print("hasta luego")
        break
    else:
        print("funcion no reconocida intente de nuevo")