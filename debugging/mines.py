#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))  # Placer les mines de manière aléatoire
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Initialisation de la grille
        self.revealed = [[False for _ in range(width)] for _ in range(height)]  # Initialisation des cases révélées

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))  # Affiche les numéros de colonne
        for y in range(self.height):
            print(f"{y:2} ", end='')  # Affiche le numéro de ligne
            for x in range(self.width):
                if reveal or self.revealed[y][x]:  # Si on veut révéler la case ou elle est déjà révélée
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Affiche le nombre de mines voisines ou un espace
                else:
                    print('.', end=' ')  # Affiche un point pour les cases non révélées
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:  # Parcourt les cases voisines
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:  # Si la case est dans les limites
                    if (ny * self.width + nx) in self.mines:  # Vérifie si la case voisine contient une mine
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:  # Si on a trouvé une mine, le jeu est terminé
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:  # Si aucune mine n'est à proximité, on révèle aussi les cases adjacentes
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)  # Récursion pour révéler les cases voisines
        return True

    def check_victory(self):
        # Vérifie si toutes les cases sans mine sont révélées
        revealed_count = 0
        total_non_mines = self.width * self.height - len(self.mines)  # Nombre total de cases sans mine
        for y in range(self.height):
            for x in range(self.width):
                if not (y * self.width + x) in self.mines and self.revealed[y][x]:
                    revealed_count += 1
        return revealed_count == total_non_mines  # Si toutes les cases sans mine sont révélées, on a gagné

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):  # Si une mine est rencontrée
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.check_victory():  # Si toutes les cases non-mines sont révélées
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()  # Initialisation du jeu avec une grille de 10x10 et 10 mines
    game.play()

