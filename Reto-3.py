#Reto 3: Números amistosos

# Un par de números m y n son llamados amistosos (o se conocen como un par amigable), si la suma de todos los divisores de m (excluyendo a m) es igual al número n, y la suma de todos los divisores del número n (excluyendo a n) es igual a m (con m ≠ n).
# Por ejemplo, los números 220 y 284 son un par amigable porque los únicos números que dividen de forma exacta 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, y 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
# Por lo tanto, 220 es un número amistoso. Los únicos números que dividen exactamente 284 son 1, 2, 4, 71 y 142 y 1 + 2 + 4 + 71 + 142 = 220
# Por lo tanto, 284 es un número amistoso.
# Muchos pares de números amigables son conocidos; sin embargo, sólo uno de los pares (220, 284) tiene valores menores que 1000. El siguiente par está en el rango [1000, 1500].
# Desarrolle un programa que permita encontrar dicho par.

def suma_divisores(num):
    suma = 0
    for i in range(1, num):
        if (num % i) == 0:
            suma += i
    return suma

def encontrar_par_amistoso(min, max):
    for m in range(min, max):
        for n in range(m+1, max):
            if suma_divisores(m) == n and suma_divisores(n) == m:
                return m, n
    return None
par_amistoso = encontrar_par_amistoso(1000, 1500)
print("El par amigable encontrado en el rango [1000, 1500] es: ",par_amistoso)