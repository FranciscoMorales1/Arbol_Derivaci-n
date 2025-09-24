import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

# ===============================
# Lectura de la gramática
# ===============================
def leer_gramatica(archivo):
    gramatica = {}
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            izquierda, derecha = linea.split("->")
            izquierda = izquierda.strip()
            producciones = [p.strip().split() for p in derecha.split("|")]
            gramatica[izquierda] = producciones
    return gramatica

# ===============================
# Tokenizador básico
# ===============================
def tokenizar(cadena):
    tokens = []
    for parte in cadena.split():
        if parte.isdigit():
            tokens.append("num")
        elif parte.isidentifier():
            tokens.append("id")
        elif parte in ["+", "-", "*", "/"]:
            if parte in ["+", "-"]:
                tokens.append("opsuma")
            else:
                tokens.append("opmult")
        elif parte == "(":
            tokens.append("par_izq")
        elif parte == ")":
            tokens.append("par_der")
        else:
            raise ValueError(f"Token no reconocido: {parte}")
    tokens.append("$")  # fin de cadena
    return tokens

# ===============================
# Tabla LL(1) para la gramática
# ===============================
tabla_ll1 = {
    ("E", "id"): ["T", "Ep"],
    ("E", "num"): ["T", "Ep"],
    ("E", "par_izq"): ["T", "Ep"],

    ("Ep", "opsuma"): ["opsuma", "T", "Ep"],
    ("Ep", "par_der"): ["EPS"],
    ("Ep", "$"): ["EPS"],

    ("T", "id"): ["F", "Tp"],
    ("T", "num"): ["F", "Tp"],
    ("T", "par_izq"): ["F", "Tp"],

    ("Tp", "opsuma"): ["EPS"],
    ("Tp", "opmult"): ["opmult", "F", "Tp"],
    ("Tp", "par_der"): ["EPS"],
    ("Tp", "$"): ["EPS"],

    ("F", "id"): ["id"],
    ("F", "num"): ["num"],
    ("F", "par_izq"): ["par_izq", "E", "par_der"],
}

# ===============================
# Parser LL(1) con árbol
# ===============================
def parsear(tokens, gramatica):
    pila = ["$", "E"]
    indice = 0

    # Árbol como grafo dirigido
    G = nx.DiGraph()
    root = "E_0"
    G.add_node(root, label="E")
    nodos = [(root, "E")]
    contador = 1

    while pila:
        cima = pila.pop()
        token = tokens[indice]

        if cima == "EPS":
            continue

        if cima == token:  # match terminal
            indice += 1
            continue

        if (cima, token) not in tabla_ll1:
            return None  # error

        produccion = tabla_ll1[(cima, token)]

        # expandir en el árbol
        padre = None
        for n, sim in nodos:
            if sim == cima:
                padre = n
                nodos.remove((n, sim))
                break

        hijos = []
        for simbolo in produccion:
            nombre = f"{simbolo}_{contador}"
            contador += 1
            G.add_node(nombre, label=simbolo)
            G.add_edge(padre, nombre)
            if simbolo not in ["EPS", "id", "num", "opsuma", "opmult", "par_izq", "par_der"]:
                hijos.append((nombre, simbolo))
        nodos.extend(hijos)

        for simbolo in reversed(produccion):
            if simbolo != "EPS":
                pila.append(simbolo)

    if indice == len(tokens):
        return G, root
    return None

# ===============================
# Impresión textual del árbol
# ===============================
def imprimir_arbol(G, nodo, nivel=0, prefijo=""):
    hijos = list(G.successors(nodo))
    etiqueta = G.nodes[nodo].get("label", nodo)
    print(" " * (2 * nivel) + prefijo + etiqueta)
    for i, hijo in enumerate(hijos):
        nuevo_prefijo = "├── " if i < len(hijos) - 1 else "└── "
        imprimir_arbol(G, hijo, nivel + 1, nuevo_prefijo)

# ===============================
# Dibujar árbol con NetworkX + pydot
# ===============================
def dibujar_arbol(G, root):
    pos = graphviz_layout(G, prog="dot")
    etiquetas = {n: G.nodes[n].get("label", n) for n in G.nodes}
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, labels=etiquetas, arrows=True,
            node_color="lightblue", node_size=1500, font_size=8)
    plt.show()

# ===============================
# Programa principal
# ===============================
def main():
    gramatica = leer_gramatica("gramatica.txt")
    print("Gramática cargada")
    print("Escribe una cadena (o 'exit' para salir):")

    while True:
        cadena = input(">> ")
        if cadena.strip().lower() == "exit":
            break
        try:
            tokens = tokenizar(cadena)
            print("Tokens:", tokens)
            resultado = parsear(tokens, gramatica)
            if resultado:
                G, root = resultado
                print("Cadena aceptada")
                imprimir_arbol(G, root)
                dibujar_arbol(G, root)
            else:
                print("Cadena rechazada")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()


