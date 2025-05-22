# Precomputed list of initial move conditions
# Each entry: (turn, xmoves, omoves, board_to_play, move)
# All positions are represented as (a, b, c, d) tuples
# None is used where applicable

PRECOMPUTED_MOVES = [
    ('x', None, None, None, (1, 1, 1, 1)),
    ('o', [(1, 1, 1, 1)], None, (1, 1), (1, 1, 0, 0)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 0, 0)], (0, 0), (0, 0, 2, 2)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 0, 2)], (0, 2), (0, 2, 2, 0)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 2, 0)], (2, 0), (2, 0, 0, 2)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 2, 2)], (2, 2), (2, 2, 0, 0)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 1, 2)], (1, 2), (1, 2, 0, 1)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 1, 0)], (1, 0), (1, 0, 0, 1)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 0, 1)], (0, 1), (0, 1, 1, 2)),
    ('x', [(1, 1, 1, 1)], [(1, 1, 2, 1)], (2, 1), (2, 1, 1, 2)),
    ('o', [(1, 1, 1, 1), (0, 0, 2, 2)], [(1, 1, 0, 0)], (2, 2), (2, 2, 0, 0)),
    ('o', [(1, 1, 1, 1), (0, 2, 2, 0)], [(1, 1, 0, 2)], (2, 0), (2, 0, 0, 2)),
    ('o', [(1, 1, 1, 1), (2, 0, 0, 2)], [(1, 1, 2, 0)], (0, 2), (0, 2, 2, 0)),
    ('o', [(1, 1, 1, 1), (2, 2, 0, 0)], [(1, 1, 2, 2)], (0, 0), (0, 0, 2, 2)),
    ('o', [(1, 1, 1, 1), (0, 0, 0, 0)], [(1, 1, 0, 0)], (0, 0), (0, 0, 2, 0)),
    ('o', [(1, 1, 1, 1), (0, 2, 0, 2)], [(1, 1, 0, 2)], (0, 2), (0, 2, 0, 0)),
    ('o', [(1, 1, 1, 1), (2, 0, 2, 0)], [(1, 1, 2, 0)], (2, 0), (2, 0, 2, 2)),
    ('o', [(1, 1, 1, 1), (2, 2, 2, 2)], [(1, 1, 2, 2)], (2, 2), (2, 2, 0, 2)),
]


def extract_moves(board):
    xmoves = []
    omoves = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    val = board[a][b][c][d]
                    if val == 1:
                        xmoves.append((a, b, c, d))
                    elif val == -1:
                        omoves.append((a, b, c, d))
    return xmoves, omoves


def precomputed_move(board, board_to_play, turn):
    xmoves, omoves = extract_moves(board)

    for entry in PRECOMPUTED_MOVES:
        ent_turn, ent_x, ent_o, ent_btp, ent_move = entry

        if ent_turn != turn:
            continue
        if ent_btp != board_to_play:
            continue
        if ent_x is not None and sorted(xmoves) != sorted(ent_x):
            continue
        if ent_o is not None and sorted(omoves) != sorted(ent_o):
            continue
        return ent_move
    return False
