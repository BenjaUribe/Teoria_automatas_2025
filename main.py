from collections import deque

if __name__ == "__main__":
    transiciones = [(0, 'a', 'R', 0, 'AR'), (0, 'a', 'A', 0, 'AA'), (0, 'b', 'A', 1, '-'),
                     (1, 'b', 'A', 1, '-'), (1, '-', 'R', 2, 'R')]
    estado_actual = 0
    estado_final = 2
    pila = deque(['R'])
    palabra = input("Ingrese la palabra a procesar: ")

#Problema: con este for no se alcanza a llegar a estado final
    for i in range(len(palabra)):
        simbolo_actual = palabra[i]
        print("Simbolo actual: ", simbolo_actual)
        print("Estado actual: ", estado_actual)
        print("Tope de pila: ", pila[0])
        
        #Cambio: ahora tambien busca la transición que coincida con tope de pila
        resultado = next((t for t in transiciones if (t[0] == estado_actual and t[1] == simbolo_actual) and t[2] == pila[0]), None)
        print("Transicion encontrada: ", resultado, "\n")
        if not resultado:
            print(f"Error: No hay transición definida para el estado {estado_actual} con el símbolo '{simbolo_actual}'")
            break
         
        estado_actual = resultado[3]
        if len(resultado[4]) > 1:
            for j in range(len(resultado[4])-2, -1, -1):
                pila.appendleft(resultado[4][j])
        elif resultado[4] == '-':
            pila.popleft()
        
    '''if estado_actual == estado_final:
        print("Cadena aceptada por estado final")'''
        


        
