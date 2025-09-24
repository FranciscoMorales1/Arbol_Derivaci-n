# Parser LL(1) con Árbol de Derivación

Parser LL(1) en Python que tokeniza expresiones aritméticas y muestra su árbol de derivación (texto y gráfico).

## Requisitos (librerías)

Instala Python 3 y estas librerías:

```bash
pip install networkx matplotlib pydot


## Ejecución

1. Asegúrate de que el archivo `gramatica.txt` esté en la **misma carpeta** que `Arbol_Derivación.py`.
2. Ejecuta el programa:

```bash
python Arbol_Derivación.py
```

---

## Uso

* El programa pedirá una cadena de entrada.
* **Cada carácter debe separarse por un espacio.**
  Ejemplo correcto:

```
2 + 3 * ( 4 - 1 )
```

❌ Ejemplo incorrecto (sin espacios):

```
2+3*(4-1)
```

* Cuando se abra la ventana con la imagen del árbol, **ciérrala** para poder ingresar la siguiente expresión.
* Para salir del programa escribe:

```
exit
```

