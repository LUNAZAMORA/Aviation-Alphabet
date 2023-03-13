
alphabet ={ "alpha" : 'a',
            "bravo" : 'b',
            "charlie" : 'c',
            "delta" : 'd',
            "echo" : 'e',
            "foxtrot" : 'f',
            "golf" : 'g',
            "hotel" : 'h',
            "india" : 'i',
            "juliet" : 'j',
            "kilo" : 'k',
            "lima" : 'l',
            "mike" : 'm',
            "november" : 'n',
            "o" : 'g',
            "p" : 'h',
            "quebec" : 'q',
            "romeo" : 'r',
            "kilo" : 'k',
            "lima" : 'l',
            "mike" : 'm',

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
while(opt != 4):
    opt = input()
    if opt != '1' and opt != '2' and opt != '3' and opt != '4': 
        print("Invalid Option!")
        print_menu()
        continue
    opt = int(opt)
    if opt == 1:
        print("Dame el mensaje a codificar: ")
        msg = input().strip().split()
        #print(msg)
    print_menu()
