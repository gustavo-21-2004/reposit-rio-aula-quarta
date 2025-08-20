print("comece uma amisade lige para alguem")
while True:
    x = int(input("atendeu a telefone (1 para sim e 2 para não): "))
    if x == 1:
        break
print("otimo agora covide para refeicao")
x = int(input("se ele aceitou o convite (1 para sim)"))
if x==1:
    print("comece a amisade")
else:
    print("tente oferecer uma bebida")
    minha_lista =['café','chá','chocolate']
    x = int(input("se ele aceitou a bebida (1 para sim e 2 para não)"))
    if x==1:
        print("comece a amisade ofereça", minha_lista[0:3]) 
    else:
        y=0
        while True:
            print("gotaria de um",minha_lista[y])
            y=y+1
            x = int(input("se ele aceitou a bebida (1 para sim e 2 para não)"))
            if x == 1:
                break
        print("comece a amisade")