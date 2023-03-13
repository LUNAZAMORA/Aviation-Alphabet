import random

alphabet_words={ "alpha" : 'a',
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
            "oscar" : 'o',
            "papa" : 'p',
            "quebec" : 'q',
            "romeo" : 'r',
            "sierra" : 's',
            "tango" : 't',
            "uniform" : 'u',
            "victor" : 'v',
            "whiskey" : 'w',
            "xray" : 'x',
            "yankee" : 'y',
            "zulu" : 'z',

        }
alphabet_letters ={ 'a': "alpha" ,
            'b': "bravo" ,
            'c': "charlie" ,
            'd': "delta" ,
            'e': "echo" ,
            'f': "foxtrot" ,
            'g': "golf" ,
            'h': "hotel" ,
            'i': "india" ,
            'j': "juliet" ,
            'k': "kilo" ,
            'l': "lima" ,
            'm': "mike" ,
            'n': "november" ,
            'o': "oscar" ,
            'p': "papa" ,
            'q': "quebec" ,
            'r': "romeo" ,
            's': "sierra" ,
            't': "tango" ,
            'u': "uniform" ,
            'v': "victor" ,
            'w': "whiskey" ,
            'x': "xray" ,
            'y': "yankee" ,
            'z': "zulu" ,

        }
'''
for key, value in alphabet.items():
    print("Key: %s, value: %s" % (key, value))
print("hola mundo")
'''

# imprimir menu
    # leer entrada
    # checar si entrada es valida
    # si es valida, procesarla
# si la entrada es 3, salir
# si no es valida, volver a imprimir el menu

def print_menu():
    print("Tienes las siguientes opciones: ")
    print("\t1-. Recuerdame el alfabeto.")
    print("\t2-. Codificar mensaje.")
    print("\t3-. Decodificar mensaje.")
    print("\t4-. MiniJuego.")
    print("\t5-. Salir.")
def process_option(option):
    if opt != '1' or opt != '2' or opt != '3' or opt != '4': 
        print("Invalid Option!")
        return 

print_menu()
opt = 0
while(opt != 5):
    opt = input()
    if opt != '1' and opt != '2' and opt != '3' and opt != '4' and opt != '5':
        print("Invalid Option!")
        print_menu()
        continue
    opt = int(opt)
    if opt == 1:
        print()
        print("El alfabeto de aviacion es:")
        print()
        for key, value in alphabet_letters.items():
            print("\t", key, ": ", value)
        print()
    elif opt == 2:
        print("Dame el mensaje a codificar: ")
        msg = list(map(str.lower, input().strip().split()))
        sentence = []
        for word in msg:
            res = ' '.join(list(map(lambda x: alphabet_letters[x], word)))
            sentence.append(res)
        final = ' '.join(sentence)
        print(final)
    elif opt == 3:
        print("Dame el mensaje a decodificar: ")
        msg = list(map(str.lower, input().strip().split()))
        #print(msg)
        res = ''.join(list(map(lambda x: alphabet_words[x], msg)))
        print(res)
    elif opt == 4:
        print("Si quieres salir, escribe: 'exit'.")
        #for i in range(random.randint(1, 11)):
        good = 0
        while(True):
            print()
            print("Cual es el valor para la siguiente letra en el alfabeto de aviacion: ", end ='')
            print(choice:= random.choice(list(alphabet_letters.keys())))
            res = input().strip().lower()
            if res == "exit":
                print("Obtuviste %s respuestas correctas." % good)
                print("Hasta Luego!")
                print()
                break
            elif res == alphabet_letters[choice]:
                print("Correcto!")
                good += 1
            else:
                print("Eso es incorrecto!")
                print("La respuesta correcta es: %s" % alphabet_letters[choice])
                print("Obtuviste %s respuestas correctas." % good)
                print()
                break
        #continue
    elif opt == 5:
        print("Nos vemos!")
        break
    print_menu()
