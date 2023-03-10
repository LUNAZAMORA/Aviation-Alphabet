
alphabet ={ "alpha" : 'a',
            "bravo" : 'b',
            "charlie" : 'c',

        }
for key, value in alphabet.items():
    print("Key: %s, value: %s" % (key, value))
print("hola mundo")

# imprimir menu
    # leer entrada
    # checar si entrada es valida
    # si es valida, procesarla
# si la entrada es 3, salir
# si no es valida, volver a imprimir el menu

def print_menu():
    print("Tienes las siguientes opciones: ")
    print("\t1-. Codificar mensaje.")
    print("\t2-. Decodificar mensaje.")
    print("\t3-. MiniJuego.")
    print("\t4-. Salir.")
def process_option(option):
    if opt != '1' or opt != '2' or opt != '3' or opt != '4': 
        print("Invalid Option!")
        return 

print_menu()
opt = 0
while(opt != 3):
    opt = input()
    if opt != '1' or opt != '2' or opt != '3' or opt != '4': 
        print("Invalid Option!")
    opt = int(opt)
    print_menu()
    if opt == 1:
        print("Dame el mensaje a codificar: ")
        msg = input().strip().split()
