from nodes import create_and_connect_nodes

def main():
    nodes = create_and_connect_nodes()
    for node in nodes:
        print(f"Nœud {node.id}: voisins -> {[neighbor.id for neighbor in node.neighbors]}")

if __name__ == "__main__":
    main()
