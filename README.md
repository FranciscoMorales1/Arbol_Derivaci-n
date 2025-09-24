Tienes un bloque de código mal cerrado: por eso `## Ejecución` quedó dentro del bloque y se ve pequeño. Copia y pega **esto tal cual** como tu `README.md` (ya está limpio y con los backticks correctos):

````markdown
# Parser LL(1) con Árbol de Derivación

Parser LL(1) en Python que tokeniza expresiones aritméticas y muestra su árbol de derivación (texto y gráfico).

## Requisitos (librerías)

Instala Python 3 y estas librerías:

```bash
pip install networkx matplotlib pydot
````

## Ejecución

1. Asegúrate de que `gramatica.txt` esté en la **misma carpeta** que `Arbol_Derivación.py`.
2. Ejecuta:

```bash
python Arbol_Derivación.py
```

## Uso rápido / evitar errores

* **Espacios**: escribe cada carácter separado por un espacio.
  Ejemplo correcto: `2 + 3 * ( 4 - 1 )`
  Incorrecto: `2+3*(4-1)`
* **Ventana del gráfico**: **cierra** la ventana del árbol para poder ingresar la siguiente expresión.
* Si ves un error tipo `GraphViz's executables not found`, instala **Graphviz** en tu sistema y (en Windows) agrega su carpeta `bin` al `PATH`.
* Para salir, escribe: `exit`

```

Con esto, los títulos se verán grandes y el bloque de instalación no “tragará” el resto del README.
```

