


````markdown
# Parser LL(1) con Árbol de Derivación

Parser LL(1) en Python que tokeniza expresiones aritméticas y muestra su árbol de derivación tanto en texto como en gráfico.

---

## Requisitos

1. Instalar **Python 3**.  
2. Instalar las siguientes librerías:

```bash
pip install networkx matplotlib pydot
````

3. Instalar **Graphviz** en tu sistema para visualizar los árboles.

   * Linux (Debian/Ubuntu): `sudo apt-get install graphviz`
   * macOS (Homebrew): `brew install graphviz`
   * Windows: descarga el instalador desde [graphviz.org](https://graphviz.org/download/) y agrega la carpeta `bin/` al **PATH**.

---

## Ejecución

1. Asegúrate de que el archivo `gramatica.txt` esté en la **misma carpeta** que `Arbol_Derivación.py`.
2. Ejecuta el programa desde la terminal:

```bash
python Arbol_Derivación.py
```

---

## Uso

1. El programa pedirá una cadena de entrada.
2. **Cada carácter debe escribirse separado por un espacio.**

✅ Ejemplo correcto:

```
2 + 3 * ( 4 - 1 )
```

❌ Ejemplo incorrecto:

```
2+3*(4-1)
```

3. Cuando se abra la ventana con la imagen del árbol, **debes cerrarla** para poder ingresar la siguiente expresión.
4. Para salir del programa escribe:

```
exit
```

```

