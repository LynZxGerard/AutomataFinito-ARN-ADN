# Validación de Secuencias Genéticas de ADN y ARN con Autómatas Finitos

Este proyecto consiste en el desarrollo de una herramienta interactiva para validar secuencias genéticas de ADN y ARN utilizando autómatas finitos, implementados mediante Python y una interfaz gráfica desarrollada con CustomTkinter.

## Reglas de Validación

El objetivo es verificar si una cadena genética cumple con las siguientes reglas específicas según su tipo:

### ADN:

-   **Inicio:** La cadena debe iniciar con el codón `ATG`.
-   **Término:** Debe finalizar con uno de los codones de parada: `TGA`, `TAA` o `TAG`.
-   **Alfabeto:** Solo pueden usarse los caracteres `{A, T, C, G}`.
-   **Longitud:** Debe ser múltiplo de 3.

### ARN:

-   **Inicio:** La cadena debe iniciar con el codón `AUG`.
-   **Término:** Debe finalizar con uno de los codones de parada: `UGA`, `UAA` o `UAG`.
-   **Alfabeto:** Solo pueden usarse los caracteres `{A, U, C, G}`.
-   **Longitud:** Debe ser múltiplo de 3.

Además, el programa identifica automáticamente si la cadena corresponde a ADN o ARN, basándose en el alfabeto utilizado.

## Implementación del Autómata

### Diseño

-   **Estados:** Incluyen un estado inicial (`q0`), estados intermedios para validar inicio, codones y longitud, un estado de aceptación (`q9`), y un estado de error para manejar irregularidades.
-   **Transiciones:** Definidas para procesar un símbolo a la vez, siguiendo las reglas estructurales específicas.
-   **Alfabetos:** `{A, T, C, G}` para ADN y `{A, U, C, G}` para ARN.

### Solución al No-Determinismo

Inicialmente, el autómata fue diseñado como **no determinista**, lo que complicaba su implementación y generaba errores, como la aceptación de codones de terminación en posiciones intermedias. Para resolver esto:

1.  **Conversión a determinista:** Se eliminaron transiciones redundantes y se corrigió el flujo lógico para que el autómata determinista aceptara únicamente cadenas válidas.
2.  **Reestructuración de transiciones:** Se eliminaron transiciones desde el estado de aceptación (`q9`), asegurando que, una vez alcanzado, el proceso no retrocediera.

### Interfaz Gráfica

La interfaz permite a los usuarios:

-   Ingresar cadenas genéticas para validación.
-   Recibir retroalimentación sobre la validez de la cadena o los motivos de rechazo.
-   Visualizar instrucciones claras de uso.

## Metodología

-   **Definición del autómata:** Se crearon diagramas y tablas de transición para estructurar las validaciones.
-   **Pruebas exhaustivas:** Cada tipo de cadena (válida e inválida) se probó para garantizar que las reglas fueran correctamente aplicadas.
-   **Documentación:** Se explican detalladamente las reglas de validación, las decisiones de diseño y los problemas resueltos.

## Dependencias

Asegúrese de instalar la biblioteca **CustomTkinter** antes de ejecutar el programa:

`pip install customtkinter` 

Este proyecto busca optimizar la validación de cadenas genéticas, simplificando procesos complejos y reduciendo errores, con un enfoque educativo y práctico en la aplicación de los autómatas finitos.
