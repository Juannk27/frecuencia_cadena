#Contar palabras repetidas en un texto

def count_words(text):

    text = text.lower()

    words = text.split()

    world_count = {}

    # Recorre cada palabra en la lista de palabras.
    for word in words:
        # Si la palabra ya está en el diccionario, incrementa su valor en 1.
        if word in world_count:
            world_count[word] += 1
        else:
         # Si no está, añade la palabra al diccionario con un valor inicial de 1
         world_count[word] = 1
    
    # Devuelve el diccionario con las palabras y sus frecuencias.
    return world_count


# Entrada de ejemplo
text_input = "vamos a ir mañana vamos a ir mañana con Juan, Juan va tambien"
result = count_words(text_input)

print(result)