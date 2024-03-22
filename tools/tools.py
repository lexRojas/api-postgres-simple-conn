
def list_to_str(l):
    # Convertir cada elemento en la lista en una cadena y unirlos con comas
    cadena = ', '.join(str(x) for x in l)

    # Añadir paréntesis al inicio y al final de la cadena
    cadena_final = f'({cadena})'

    return cadena_final