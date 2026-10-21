import os
import tkinter as tk
from same import ModeleSame

img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")

class VueSame:
    def __init__(self, same):
        self._same = same
        self._root = tk.Tk()
        self._root.title("Same Game - Étape 1")
        # Load images for the balls
        self._images = [
            tk.PhotoImage(file=os.path.join(img_folder, f"medium_sphere{i + 1}.gif")) for i in range(same.nbcouleurs())
        ]
        self._images.append(tk.PhotoImage(file=os.path.join(img_folder, "medium_spherevide.gif")))  # Empty image

        # Create the grid of buttons
        self._les_btns = []
        for i in range(same.nblig()):
            ligne_btns = []
            for j in range(same.nbcol()):
                btn = tk.Button(
                    self._root,
                    image=self._images[same.couleur(i, j)],
                    command=self.creer_controller_btn(i, j)
                )
                btn.grid(row=i, column=j)
                ligne_btns.append(btn)
            self._les_btns.append(ligne_btns)

        # Create the score label
        self._score_label = tk.Label(self._root, text=f"Score: {self._same.score()}")
        self._score_label.grid(row=same.nblig(), column=0, columnspan=same.nbcol())

        # Create the "New Game" button
        self._nouveau_btn = tk.Button(
            self._root, text="Nouvelle Partie", command=self.nouvelle_partie
        )
        self._nouveau_btn.grid(row=same.nblig() + 1, column=0, columnspan=same.nbcol() // 2)

        # Create the "Quit" button
        self._quitter_btn = tk.Button(self._root, text="Quitter", command=self._root.quit)
        self._quitter_btn.grid(row=same.nblig() + 1, column=same.nbcol() // 2, columnspan=same.nbcol() // 2)

        # Start the main loop
        self._root.mainloop()

    def redessine(self):
        for i in range(self._same.nblig()):
            for j in range(self._same.nbcol()):
                couleur = self._same.couleur(i, j)
                self._les_btns[i][j].config(image=self._images[couleur])
        self._score_label.config(text=f"Score: {self._same.score()}")

    def nouvelle_partie(self):
        self._same.nouvelle_partie()
        self.redessine()

    def creer_controller_btn(self, i, j):
        def controller_btn():
            self._same.supprime_bille(i, j)
            self.redessine()
        return controller_btn


if __name__ == "__main__":
    # Create the model
    same = ModeleSame()
    # Create the view, which also starts the main loop
    vue = VueSame(same)