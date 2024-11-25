import customtkinter as ctk
from tkinter import messagebox

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Tema de colores

# Definición de la tabla de transiciones para ADN y ARN
tabla_transiciones_adn = {
    'q0': {'A': 'q1', 'T': 'ERROR', 'C': 'ERROR', 'G': 'ERROR'},
    'q1': {'A': 'ERROR', 'T': 'q2', 'C': 'ERROR', 'G': 'ERROR'},
    'q2': {'A': 'ERROR', 'T': 'ERROR', 'C': 'ERROR', 'G': 'q3'},
    'q3': {'A': 'q4', 'T': 'q6', 'C': 'q4', 'G': 'q4'},
    'q4': {'A': 'q5', 'T': 'q5', 'C': 'q5', 'G': 'q5'},
    'q5': {'A': 'q3', 'T': 'q3', 'C': 'q3', 'G': 'q3'},
    'q6': {'A': 'q7', 'T': 'q5', 'C': 'q5', 'G': 'q8'},
    'q7': {'A': 'q9', 'T': 'q3', 'C': 'q3', 'G': 'q9'},
    'q8': {'A': 'q9', 'T': 'q3', 'C': 'q3', 'G': 'ERROR'},
    'q9': {'A': 'ERROR', 'T': 'ERROR', 'C': 'ERROR', 'G': 'ERROR'},
    'ERROR': {'A': 'ERROR', 'T': 'ERROR', 'C': 'ERROR', 'G': 'ERROR'},
}

tabla_transiciones_arn = {
    'q0': {'A': 'q1', 'U': 'ERROR', 'C': 'ERROR', 'G': 'ERROR'},
    'q1': {'A': 'ERROR', 'U': 'q2', 'C': 'ERROR', 'G': 'ERROR'},
    'q2': {'A': 'ERROR', 'U': 'ERROR', 'C': 'ERROR', 'G': 'q3'},
    'q3': {'A': 'q4', 'U': 'q6', 'C': 'q4', 'G': 'q4'},
    'q4': {'A': 'q5', 'U': 'q5', 'C': 'q5', 'G': 'q5'},
    'q5': {'A': 'q3', 'U': 'q3', 'C': 'q3', 'G': 'q3'},
    'q6': {'A': 'q7', 'U': 'q5', 'C': 'q5', 'G': 'q8'},
    'q7': {'A': 'q9', 'U': 'q3', 'C': 'q3', 'G': 'q9'},
    'q8': {'A': 'q9', 'U': 'q3', 'C': 'q3', 'G': 'ERROR'},
    'q9': {'A': 'ERROR', 'U': 'ERROR', 'C': 'ERROR', 'G': 'ERROR'},
    'ERROR': {'A': 'ERROR', 'U': 'ERROR', 'C': 'ERROR', 'G': 'ERROR'},
}

# Estados inicial y final
estado_inicial = 'q0'
estado_final = 'q9'

# Función para verificar si una cadena es válida
def es_cadena_valida(cadena):
    # Verificar si la cadena tiene una mezcla de T y U
    if 'T' in cadena and 'U' in cadena:
        messagebox.showerror("Error", "La cadena no puede contener tanto T como U.")
        return False

    # Verificar si la cadena es ARN o ADN
    if 'U' in cadena:
        tabla_transiciones = tabla_transiciones_arn
        tipo = "ARN"
        terminaciones_validas = ['UGA', 'UAA', 'UAG']
    else:
        tabla_transiciones = tabla_transiciones_adn
        tipo = "ADN"
        terminaciones_validas = ['TGA', 'TAA', 'TAG']

    # Procesar la cadena con el autómata
    estado_actual = estado_inicial
    mensajes = [f"Procesando cadena ({tipo}): {cadena}"]

    for simbolo in cadena:
        if simbolo not in tabla_transiciones[estado_actual]:
            mensajes.append(f"Símbolo no válido: {simbolo}. Rechazo inmediato.")
            messagebox.showwarning(f"Proceso Detallado ({tipo})", "\n".join(mensajes))
            return False

        estado_anterior = estado_actual
        estado_actual = tabla_transiciones[estado_actual][simbolo]
        mensajes.append(f"Estado actual: {estado_anterior}, Símbolo leído: {simbolo}, Nuevo estado: {estado_actual}")

        if estado_actual == 'ERROR':
            mensajes.append("-> Transición al estado de rechazo (cadena inválida)")
            

            # Verificar que la cadena comienza con el codón de inicio
            if not cadena.startswith("ATG") and not cadena.startswith("AUG"):
                mensajes.append("Error: La cadena debe comenzar con 'ATG' (ADN) o 'AUG' (ARN).")

            # Verificar que la longitud de la cadena sea un múltiplo de 3
            if len(cadena) % 3 != 0:
                mensajes.append("Error: La longitud de la cadena debe ser un múltiplo de 3.")

            # Verificar que la cadena termine con un codón de paro válido
            if not any(cadena.endswith(codon) for codon in terminaciones_validas):
                mensajes.append(f"Error: La cadena debe terminar con uno de los siguientes codones: {', '.join(terminaciones_validas)}.")

            if estado_anterior == 'q9':
                mensajes.append("Error: La cadena contiene un codón de terminación en una posición intermedia.")
            
            messagebox.showwarning(f"Proceso Detallado ({tipo})", "\n".join(mensajes))
            return False

    if estado_actual == estado_final:
        mensajes.append("Estado final alcanzado. Cadena válida.")
        messagebox.showinfo(f"Proceso Detallado ({tipo})", "\n".join(mensajes))
        return True
    else:
        mensajes.append("No se alcanzó el estado final. Cadena inválida.")
        # Verificar que la longitud de la cadena sea un múltiplo de 3
        if len(cadena) % 3 != 0:
            mensajes.append("Error: La longitud de la cadena debe ser un múltiplo de 3.")
        # Verificar que la cadena termine con un codón de paro válido
        if not any(cadena.endswith(codon) for codon in terminaciones_validas):
            mensajes.append(f"Error: La cadena debe terminar con uno de los siguientes codones: {', '.join(terminaciones_validas)}.")
        
        messagebox.showwarning(f"Proceso Detallado ({tipo})", "\n".join(mensajes))
        return False

# Función que se ejecuta al presionar el botón
def verificar_cadena():
    cadena = entrada_cadena.get()
    if not cadena:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una cadena para verificar.")
        return

    resultado = es_cadena_valida(cadena)

    if resultado:
        messagebox.showinfo("Resultado", f"La cadena '{cadena}' es válida.")
    else:
        messagebox.showerror("Resultado", f"La cadena '{cadena}' es inválida.")

# Creación de la ventana principal
ventana = ctk.CTk()
ventana.title("Reconocedor de Secuencias Genéticas de ADN y ARN")
ventana.geometry("650x440")

# Establecer tamaño fijo de la ventana
ventana.resizable(False, False)

# Título del programa
titulo = ctk.CTkLabel(
    ventana, 
    text="\nReconocedor de Secuencias Genéticas de ADN y ARN", 
    font=("Arial", 20, "bold"), 
    justify="center"
)
titulo.pack(pady=10)

# Descripción inicial
descripcion = (
    "Este programa verifica si una cadena de genes es válida según las siguientes reglas:\n\n"
    "1. ADN: Símbolos permitidos {A, T, C, G}.\n"
    "2. ARN: Símbolos permitidos {A, U, C, G}.\n"
    "3. La cadena debe comenzar con 'ATG' (ADN) o 'AUG' (ARN).\n"
    "4. Debe terminar con 'TGA', 'TAA', 'TAG' (ADN) o 'UGA', 'UAA', 'UAG' (ARN).\n"
    "5. No puede mezclar símbolos de ADN y ARN.\n"
    "6. Las combinaciones 'TGA', 'TAA', 'TAG' (ADN) o 'UGA', 'UAA', 'UAG' (ARN) solo pueden estar al final.\n"
    "7. La longitud de la cadena debe ser un múltiplo de 3."
)
etiqueta_descripcion = ctk.CTkLabel(
    ventana, text=descripcion, justify="left", wraplength=550, font=("Arial", 12)
)
etiqueta_descripcion.pack(pady=5)

# Ejemplos de cadenas válidas
ejemplos = (
    "Ejemplos de cadenas válidas:\n"
    "1. ADN: ATGTGA\n"
    "2. ADN: ATGCCGTAA\n"
    "3. ARN: AUGCGAUGA\n"
)
etiqueta_ejemplos = ctk.CTkLabel(
    ventana, text=ejemplos, justify="left", wraplength=550, font=("Arial", 12, "italic")
)
etiqueta_ejemplos.pack(pady=5)

# Etiqueta de instrucciones
etiqueta = ctk.CTkLabel(ventana, text="Ingrese la cadena para verificar:", font=("Arial", 14))
etiqueta.pack(pady=10)

# Entrada para la cadena
entrada_cadena = ctk.CTkEntry(ventana, width=400)
entrada_cadena.pack(pady=5)

# Botón para verificar
boton_verificar = ctk.CTkButton(ventana, text="Verificar", command=verificar_cadena)
boton_verificar.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
