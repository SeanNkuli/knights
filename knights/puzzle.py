from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
knowledge0 = And(
    Or(AKnight, AKnave),
    Or(And(AKnight, AKnave), And(Not(AKnight), Not(AKnave)))
)

# Puzzle 1
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnave, BKnave))
)

# Puzzle 2
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(And(AKnight, BKnight), And(AKnave, BKnave)),
    Or(And(AKnight, BKnave), And(AKnave, BKnight))
)

# Puzzle 3
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    
    Implication(BKnave, Said(A, 'I am a knave')),
    Implication(BKnight, Not(Said(A, 'I am a knave'))),
    
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),
    
    Or(And(AKnight, BKnight, CKnave), 
       And(AKnight, BKnave, CKnight), 
       And(AKnave, BKnight, CKnight))
)



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
