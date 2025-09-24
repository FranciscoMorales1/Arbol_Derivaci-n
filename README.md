Entendido 👍. Lo que tú quieres es un **README único y completo**, que tenga **TODO**:

* Explicación del proyecto.
* Librerías necesarias.
* Recomendaciones (espaciado de caracteres, cerrar la ventana del grafo, etc.).
* Ejemplo de uso.
* **Lista de pruebas válidas e inválidas** ya integrada.

Aquí te lo dejo listo para tu repositorio:

````markdown
# Parser LL(1) con Árbol de Derivación

Este proyecto implementa un **parser LL(1)** en Python que:
- Tokeniza cadenas de entrada.
- Reconoce expresiones aritméticas con `+`, `-`, `*`, `/`, paréntesis, números e identificadores.
- Construye el **árbol de derivación** y lo muestra en consola (texto) y en una ventana gráfica (usando NetworkX + Graphviz).

---

## Requisitos

Necesitas tener instalado **Python 3** y las siguientes librerías:

```bash
pip install networkx matplotlib pydot
````

También es necesario instalar **Graphviz**, ya que se usa para graficar los árboles.

* En Linux (Debian/Ubuntu):

  ```bash
  sudo apt-get install graphviz
  ```
* En macOS (Homebrew):

  ```bash
  brew install graphviz
  ```
* En Windows: descarga el instalador desde [graphviz.org](https://graphviz.org/download/) y agrega la carpeta `bin/` al **PATH**.

---

## Ejecución

1. Clona este repositorio o descarga los archivos.
2. Ejecuta el programa:

```bash
python Arbol_Derivación.py
```

---

## Uso

* El programa pedirá una cadena de entrada.
* **Cada carácter debe separarse por un espacio.**
  Ejemplo:

```
2 + 3 * ( 4 - 1 )
```

* Si la cadena es aceptada:

  * Se mostrarán los **tokens** en consola.
  * Se imprimirá el **árbol de derivación en texto**.
  * Se abrirá una ventana con el **árbol gráfico**.

⚠️ **Nota importante:**
Cuando aparezca la ventana del grafo, **debes cerrarla** para que el programa reciba la siguiente entrada.

* Para salir del programa escribe:

```
exit
```

---

## Ejemplo

Entrada:

```
x + 5 * ( y - 2 )
```

Salida en consola (resumen):

```
Tokens: ['id', 'opsuma', 'num', 'opmult', 'par_izq', 'id', 'opsuma', 'num', 'par_der', '$']
Cadena aceptada ✅
E
├── T
│   └── ...
└── Ep
    └── ...
```

Y se abrirá una ventana con el árbol de derivación dibujado.

---

## Pruebas recomendadas

### Casos básicos

1. `2`
2. `x`

### Operadores de suma/resta

3. `2 + 3`
4. `x - y + 5`

### Operadores de multiplicación/división

5. `2 * 3`
6. `2 + 3 * 4`
7. `a * b / c`

### Paréntesis

8. `( 2 + 3 )`
9. `( x + y ) * z`
10. `a * ( b + c * d )`

### Combinados

11. `x + y * z + w`
12. `( 1 + 2 ) * ( 3 - 4 ) / 5`
13. `id * num + ( id - num ) * num`

### Casos inválidos (deben ser rechazados ❌)

14. `+ 2 3`
15. `2 *`
16. `( 2 + 3`
17. `x y`

---

## Recomendaciones

* Si usas **VS Code**, activa la opción *"Run in Integrated Terminal"* para que no haya problemas con la entrada de datos.
* Cierra la ventana de la gráfica cada vez que aparezca, de lo contrario el programa quedará pausado.
* Empieza con expresiones pequeñas y luego prueba las más largas para verificar precedencia, paréntesis y EPS.
* Los tokens reconocidos son:

  * `num` → números enteros.
  * `id` → identificadores (como `x`, `y`, `variable`).
  * `opsuma` → `+`, `-`.
  * `opmult` → `*`, `/`.
  * `par_izq` → `(`
  * `par_der` → `)`

---

## Licencia

Este proyecto es de uso libre para fines académicos y de aprendizaje.

```

---

Ahora sí: **todo está en el README** en un único archivo.  
¿Quieres que lo prepare ya en formato `README.md` descargable, o prefieres copiar/pegarlo tú directamente en tu repositorio?
```
