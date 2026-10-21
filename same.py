import os
from tkinter import *
from random import *

class Case:
    def __init__(self, couleur):
        self._couleur = couleur

    def couleur(self):
        return self._couleur

    def change_couleur(self, n):
        self._couleur = n

    def supprime(self):
        self._couleur = -1

    def est_vide(self):
        return self._couleur == -1

class ModeleSame:
    def __init__(self, nb_l=15, nb_c=20, nb_coul=4):
        self._nblig = nb_l
        self._nbcol = nb_c
        self._nbcouleurs = nb_coul
        self._score = 0
        self._mat = [[Case(randint(0, nb_coul - 1)) for _ in range(nb_c)] for _ in range(nb_l)]

    def score(self):
        return self._score

    def nblig(self):
        return self._nblig

    def nbcol(self):
        return self._nbcol

    def nbcouleurs(self):
        return self._nbcouleurs

    def coords_valides(self, i, j):
        return 0 <= i < self._nblig and 0 <= j < self._nbcol

    def couleur(self, i, j):
        return self._mat[i][j].couleur()

    def supprime_bille(self, i, j):
        if self.coords_valides(i, j):
            self._mat[i][j].supprime()

    def nouvelle_partie(self):
        self._mat = [[Case(randint(0, self._nbcouleurs - 1)) for _ in range(self._nbcol)] for _ in range(self._nblig)]
        self._score = 0

class VueSame:
    def __init__(self, same):
        self._same = same
        self._fen = Tk()
        self._fen.title("Jeu du Same")
        
        # Define the path to the images directory
        image_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")

        # Load images with error handling
        self._images = []
        try:
            for i in range(1, self._same.nbcouleurs() + 1):
                # Construct the full path to the image file
                image_path = os.path.join(image_directory, f"medium_sphere{i}.gif")
                self._images.append(PhotoImage(file=image_path))
            # Load the empty sphere image
            self._images.append(PhotoImage(file=os.path.join(image_directory, "medium_spherevide.gif")))
        except TclError as e:
            print(f"Error loading images: {e}")
            # Fallback: Use default images or handle the error gracefully
            self._images = [PhotoImage(file=os.path.join(image_directory, "default.gif"))] * (self._same.nbcouleurs() + 1)

        self._les_btns = [[None for _ in range(self._same.nbcol())] for _ in range(self._same.nblig())]

        for i in range(self._same.nblig()):
            for j in range(self._same.nbcol()):
                btn = Button(self._fen, image=self._images[self._same.couleur(i, j)], command=self.creer_controller_btn(i, j))
                btn.grid(row=i, column=j)
                self._les_btns[i][j] = btn

        self._lbl_score = Label(self._fen, text=f"Score : {self._same.score()}")
        self._lbl_score.grid(row=0, column=self._same.nbcol(), columnspan=2)

        btn_nvlpartie = Button(self._fen, text="Nouvelle Partie", command=self.nouvelle_partie)
        btn_nvlpartie.grid(row=1, column=self._same.nbcol(), columnspan=2)

        btn_quit = Button(self._fen, text="Au revoir !", command=self._fen.destroy)
        btn_quit.grid(row=2, column=self._same.nbcol(), columnspan=2)

        self._fen.mainloop()

    def redessine(self):
        for i in range(self._same.nblig()):
            for j in range(self._same.nbcol()):
                self._les_btns[i][j].config(image=self._images[self._same.couleur(i, j)])

    def nouvelle_partie(self):
        self._same.nouvelle_partie()
        self.redessine()
        self._lbl_score.config(text=f"Score : {self._same.score()}")

    def creer_controller_btn(self, i, j):
        def controller_btn():
            self._same.supprime_bille(i, j)
            self.redessine()
        return controller_btn

if __name__ == "__main__":
    same = ModeleSame()
    vue = VueSame(same)