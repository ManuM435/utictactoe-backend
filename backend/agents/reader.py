import csv

def load_opening_book(filepath):
    book = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entry = {
                "turn": row["turn"],
                "xmoves": row["xmoves"].split(" | ") if row["xmoves"] != "None" else [],
                "omoves": row["omoves"].split(" | ") if row["omoves"] != "None" else [],
                "btp": tuple(map(int, row["btp"].split("_"))) if row["btp"] != "None" else None,
                "move": tuple(map(int, row["move"].split("_")))
            }
            book.append(entry)
    return book

def board_has_moves(board, moves, player):
    for move_str in moves:
        a, b, c, d = map(int, move_str.split("_"))
        if board[a, b, c, d] != player:
            return False
    return True

book = load_opening_book("backend/agents/hashes/opening_book.csv")

print(book)