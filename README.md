

````markdown
# Parser LL(1) con Árbol de Derivación

Parser LL(1) en Python que tokeniza expresiones aritméticas y muestra su árbol de derivación tanto en texto como en gráfico.

---

## Requisitos

Instala Python 3 y las siguientes librerías:

```bash
pip install networkx matplotlib pydot
````

También debes tener instalado **Graphviz** en tu sistema para visualizar los árboles.

---

## Ejecución

1. Asegúrate de que el archivo `gramatica.txt` esté en la **misma carpeta** que `Arbol_Derivación.py`.
2. Ejecuta el programa desde la terminal:

```bash
python Arbol_Derivación.py
```

---

## Uso

* El programa pedirá una cadena de entrada.
* **Cada carácter debe escribirse separado por un espacio.**

 Ejemplo correcto:

```
2 + 3 * ( 4 - 1 )
```

 Ejemplo incorrecto:

```
2+3*(4-1)
```

* Cuando se abra la ventana con la imagen del árbol, **debes cerrarla** para poder ingresar la siguiente expresión.
* Para salir del programa escribe:

```
exit
```

```

