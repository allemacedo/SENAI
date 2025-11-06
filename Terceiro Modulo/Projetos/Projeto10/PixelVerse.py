import sqlite3
from datetime import date

conn = sqlite3.connect("game_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Jogadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    data_criacao TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    classe TEXT,
    nivel INTEGER,
    jogador_id INTEGER,
    FOREIGN KEY (jogador_id) REFERENCES Jogadores(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    tipo TEXT,
    valor INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    personagem_id INTEGER,
    item_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (personagem_id) REFERENCES Personagens(id),
    FOREIGN KEY (item_id) REFERENCES Itens(id)
);
""")

conn.commit()

cursor.executemany("""
INSERT INTO Jogadores (name, email, data_criacao)
VALUES (?, ?, ?)
""", [
    ("Arthur", "arthur@gmail.com", "2007-10-02"),
    ("Gabriel", "gabriel@gmail.com", "2007-10-10")
])

cursor.executemany("""
INSERT INTO Personagens (nome, classe, nivel, jogador_id)
VALUES (?, ?, ?, ?)
""", [
    ("Arthas", "Guerreiro", 10, 1),
    ("Luna", "Mago", 15, 2),
    ("Tyr", "Arqueiro", 8, 1)
])

cursor.executemany("""
INSERT INTO Itens (nome, tipo, valor)
VALUES (?, ?, ?)
""", [
    ("Espada Lendária", "Arma", 1000),
    ("Arco Élfico", "Arma", 750),
    ("Poção de Cura", "Poção", 50),
    ("Elmo de Aço", "Armadura", 300),
    ("Cajado Arcano", "Arma", 900)
])

cursor.executemany("""
INSERT INTO Inventario (personagem_id, item_id, quantidade)
VALUES (?, ?, ?)
""", [
    (1, 1, 1),
    (1, 4, 1),
    (2, 5, 1),
    (2, 3, 5)
])

conn.commit()


def listar_jogadores():
    print("\nLista de todos os jogadores:")
    for lista in cursor.execute("SELECT id, name, email, data_criacao FROM Jogadores;"):
        print(lista)

def jogadores_com_mago():
    print("\nJogadores com personagens da classe 'Mago':")
    query = """
    SELECT DISTINCT j.name
    FROM Jogadores j
    JOIN Personagens p ON j.id = p.jogador_id
    WHERE p.classe = 'Mago';
    """
    for row in cursor.execute(query):
        print(row[0])

def item_mais_valioso():
    print("\nItem mais valioso do jogo:")
    query = "SELECT nome, valor FROM Itens ORDER BY valor DESC LIMIT 1;"
    result = cursor.execute(query).fetchone()
    if result:
        print(f"{result[0]} - Valor: {result[1]}")
    else:
        print("Nenhum item encontrado.")


listar_jogadores()
jogadores_com_mago()
item_mais_valioso()

conn.close()