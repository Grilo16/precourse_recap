from random import choice

def main():

    # Set up players

    p1Name = "Charmander"
    player1 = 50
    p1Attacks = {"ember": 15, "tackle": 10}

    p2Name = "Bulbasaur"
    p2Attacks = {"razor leaf": 15, "tackle": 10}
    player2 = 50

    # Continue until either players health is equal or lower to 0
    while True:
        # Player 1 turn
        healthBars(player1, p1Name, player2, p2Name)

        # Get a valid pokemon move
        while True:
            try:
                p1Attack = p1Attacks[
                    input(
                        f"{p1Name} attack !! \nattacks: {', '.join([attack for attack in p1Attacks.keys()]).title()}\n{p1Name} uses: "
                    ).lower()
                ]
            except KeyError:
                print("\nInvalid attack\n")
                continue
            break
        p1Attack = p1Attack + choice(range(5))
        player2 -= p1Attack

        print(f"\n{p2Name} lost {p1Attack}hp!!")
        if player2 <= 0:
            print(f"\n{p2Name} is no longer able to battle")
            print(f"\n{p1Name} Wins !!!\n")
            break

        # Player 2 turn
        healthBars(player1, p1Name, player2, p2Name)

        # Get a valid pokemon move
        while True:
            try:
                p2Attack = p2Attacks[
                    input(
                        f"{p2Name} attack !! \nattacks: {', '.join([attack for attack in p2Attacks.keys()]).title()}\n{p2Name} uses: "
                    ).lower()
                ]
            except KeyError:
                print("\nInvalid attack\n")
                continue
            break

        p2Attack = p2Attack + choice(range(5))
        player1 -= p2Attack

        print(f"\n{p1Name} lost {p2Attack}hp!!")
        if player1 <= 0:
            print(f"\n{p1Name} is no longer able to battle")
            print(f"\n{p2Name} Wins !!!\n")
            break


# Function to show and update healthbars
def healthBars(player1, p1Name, player2, p2Name):
    p1Health = f"{'#'* player1}"
    p2Health = f"{' '*(50-len(p1Health))}{'#'* player2}"
    healthBars = f"\n\n{p1Name}{' '*(51-len(p1Name))}{p2Name} \n{p1Health} {p2Health}\n"
    print(healthBars)


if __name__ == "__main__":
    main()
