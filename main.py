from collections import deque

#arreglar el problema de la pila con las transiciones duplicadas
if __name__ == "__main__":
    transiciones = [(0, 'a', 'R', 0, 'AR'), (0, 'a', 'A', 0, 'AA'), (0, 'b', 'A', 1, '-'),
                     (1, 'b', 'A', 1, '-'), (1, '-', 'R', 2, 'R')]
    estado_actual = 0
    estado_final = 2
    pila = deque(['R'])
    palabra = input("Ingrese la palabra a procesar: ")

    

    for i in range(len(palabra)):
        simbolo_actual = palabra[i]
        resultado = next((t for t in transiciones if t[0] == estado_actual and t[1] == simbolo_actual), None)
        if not resultado:
            print(f"Error: No hay transición definida para el estado {estado_actual} con el símbolo '{simbolo_actual}'")
            break
        if not resultado[2] == pila[0]:
            print(f"Error: No se puede hacer la transición desde el estado {estado_actual} con el símbolo '{simbolo_actual}'")
            break
         
        estado_actual = resultado[3]
        if len(resultado[4]) > 1:
            for j in range(len(resultado[4])-2, 0, -1):
                pila.appendleft(resultado[4][j])
        elif resultado[4] == '-':
            pila.popleft()
        
    if estado_actual == estado_final:
        print("Cadena aceptada por estado final")
        


        
