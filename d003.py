# Condicionales: Estructura de codigos para que el programa sea mas
# inteligente y pueda tomar decisiones.

# > : mayor que
# < : menor que
# == : igual que
# >= : mayor o igual
# <= : menor o igual
# != : diferente que


numero = 10


# Si: se ejecuta el codigo / No: se descarta el IF y pasa al Elif.
if numero > 7:
    print("El numero es mayor que 7")
# Si: se ejecuta el codigo / No: se descarta el Elif y pasa al Else.
elif numero == 7:
    print("El numero es igual a 7")
else:  # ELSE solo se ejcuta cuando IF y ELIF son falsos.
    print("El numero es menor que 7")
