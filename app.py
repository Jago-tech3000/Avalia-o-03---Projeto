import sys
import json

# -----------------------------
# Tabela de Hash
# -----------------------------
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        if key in self.table:
            raise KeyError("Chave já existente!")
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)

    def delete(self, key):
        if key in self.table:
            del self.table[key]

# -----------------------------
# Árvore B (Simplificada)
# -----------------------------
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.t = t  # Grau da árvore
        self.root = BTreeNode(True)

    def insert(self, key):
        # Lógica de inserção (simplificada)
        pass

    def search(self, key):
        # Lógica de busca (simplificada)
        pass

# -----------------------------
# Funções Auxiliares - Merge Sort
# -----------------------------
def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# -----------------------------
# Classe Principal: Database
# -----------------------------
class Database:
    def __init__(self):
        self.hash_table = HashTable()
        self.b_tree = BTree(t=3)
        self.load_data()

    def insert(self, id, nome, idade):
        record = {"id": id, "nome": nome, "idade": idade}
        
        try:
            self.hash_table.insert(id, record)
        except KeyError:
            print("Erro: Chave já existe!")
            return

        self.b_tree.insert(record)
        self.save_data()

    def select(self, id):
        return self.hash_table.get(id)

    def update(self, id, campo, novo_valor):
        record = self.hash_table.get(id)
        if record:
            record[campo] = novo_valor
            self.save_data()
            return True
        return False

    def delete(self, id):
        record = self.hash_table.get(id)
        if record:
            self.hash_table.delete(id)
            # Remoção da Árvore B omitida (não implementada)
            self.save_data()
            return True
        return False

    def sort(self, campo):
        records = list(self.hash_table.table.values())
        merge_sort(records, campo)
        return records

    def load_data(self):
        try:
            with open("data/db_file.json", "r") as file:
                data = json.load(file)
                for record in data:
                    self.hash_table.insert(record["id"], record)
        except FileNotFoundError:
            pass

    def save_data(self):
        data = list(self.hash_table.table.values())
        with open("data/db_file.json", "w") as file:
            json.dump(data, file, indent=4)

# -----------------------------
# CLI - Interface de Linha de Comando
# -----------------------------
def main():
    db = Database()

    if len(sys.argv) < 2:
        print("Comando inválido!")
        return

    command = sys.argv[1].upper()

    if command == "INSERT":
        try:
            id = int(sys.argv[2])
            nome = sys.argv[3]
            idade = int(sys.argv[4])
            db.insert(id, nome, idade)
            print("Registro inserido com sucesso!")
        except IndexError:
            print("Uso: INSERT <id> <nome> <idade>")
    elif command == "SELECT":
        try:
            id = int(sys.argv[2])
            record = db.select(id)
            if record:
                print(f"Resultado: {record}")
            else:
                print("Registro não encontrado!")
        except IndexError:
            print("Uso: SELECT <id>")
    elif command == "UPDATE":
        try:
            id = int(sys.argv[2])
            campo = sys.argv[3]
            novo_valor = sys.argv[4]
            if db.update(id, campo, novo_valor):
                print("Registro atualizado com sucesso!")
            else:
                print("Erro ao atualizar registro!")
        except IndexError:
            print("Uso: UPDATE <id> <campo> <novo_valor>")
    elif command == "DELETE":
        try:
            id = int(sys.argv[2])
            if db.delete(id):
                print("Registro excluído com sucesso!")
            else:
                print("Erro ao excluir registro!")
        except IndexError:
            print("Uso: DELETE <id>")
    elif command == "SORT":
        try:
            campo = sys.argv[2]
            sorted_records = db.sort(campo)
            print(f"Registros ordenados por {campo}:")
            for record in sorted_records:
                print(record)
        except IndexError:
            print("Uso: SORT <campo>")
    else:
        print("Comando desconhecido!")

if __name__ == "__main__":
    main()
