from random import randint
import tkinter as tk

DIM = 21

class VueMessage:
    def __init__(self, texte="Bonjour à tous"):
        fen = tk.Tk()
        fen.title("tk")
        lbl_message = tk.Label(fen, text=texte, fg="red")
        lbl_message.pack()
        btn_quitter = tk.Button(fen, text="Au revoir", command=fen.destroy)
        btn_quitter.pack()
        fen.mainloop()

class VueMessage2:
    def __init__(self, texte=""):
        fenetre = tk.Tk()
        fenetre.title("Exercice 2")
        self.__lbl_texte = tk.Label(fenetre, text="Bonjour", fg="red")
        self.__lbl_texte.pack()
        self.__saisie = tk.Entry(fenetre)
        self.__saisie.pack()
        btn_valide = tk.Button(fenetre, text="Valider", command=self.saisie_texte)
        btn_valide.pack(side="left")
        btn_quitter = tk.Button(fenetre, text="Au revoir", command=fenetre.destroy)
        btn_quitter.pack(side="left")
        fenetre.mainloop()

    def saisie_texte(self):
        message = self.__saisie.get()
        self.__lbl_texte.config(text="Bonjour " + message)
        self.__saisie.delete(0, len(message))

class VueDemineur:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Exercice 3")
        self.initialisation_images()
        self.canvas = tk.Canvas(self.fenetre, width=5 * DIM, height=DIM)
        self.canvas.pack()
        btn_changer = tk.Button(self.fenetre, text="Changer les images", command=self.afficher_images)
        btn_changer.pack()
        btn_quitter = tk.Button(self.fenetre, text="Au revoir", command=self.fenetre.destroy)
        btn_quitter.pack()
        self.afficher_images()
        self.fenetre.mainloop()

    def initialisation_images(self):
        self.images = [
            tk.PhotoImage(file="images_demineur/un.gif"),
            tk.PhotoImage(file="images_demineur/deux.gif"),
            tk.PhotoImage(file="images_demineur/trois.gif"),
            tk.PhotoImage(file="images_demineur/quatre.gif"),
            tk.PhotoImage(file="images_demineur/cinq.gif"),
            tk.PhotoImage(file="images_demineur/six.gif"),
            tk.PhotoImage(file="images_demineur/sept.gif"),
            tk.PhotoImage(file="images_demineur/huit.gif"),
            tk.PhotoImage(file="images_demineur/mine.gif")
        ]

    def afficher_images(self):
        self.canvas.delete("all")
        for i in range(5):
            indice = randint(0, len(self.images) - 1)
            x = i * DIM
            self.canvas.create_image(x, 0, anchor=tk.NW, image=self.images[indice])

class VueDemineurGrid:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Exercice 6")
        self.initialisation_images()
        self.canvas = tk.Canvas(self.fenetre, width=5 * DIM, height=5 * DIM)
        self.canvas.pack()
        btn_changer = tk.Button(self.fenetre, text="Recommencer", command=self.afficher_images)
        btn_changer.pack()
        btn_quitter = tk.Button(self.fenetre, text="Au revoir", command=self.fenetre.destroy)
        btn_quitter.pack()
        self.afficher_images()
        self.fenetre.mainloop()

    def initialisation_images(self):
        self.images = [
            tk.PhotoImage(file="images_demineur/un.gif"),
            tk.PhotoImage(file="images_demineur/deux.gif"),
            tk.PhotoImage(file="images_demineur/trois.gif"),
            tk.PhotoImage(file="images_demineur/quatre.gif"),
            tk.PhotoImage(file="images_demineur/cinq.gif"),
            tk.PhotoImage(file="images_demineur/six.gif"),
            tk.PhotoImage(file="images_demineur/sept.gif"),
            tk.PhotoImage(file="images_demineur/huit.gif"),
            tk.PhotoImage(file="images_demineur/mine.gif")
        ]

    def afficher_images(self):
        self.canvas.delete("all")
        for i in range(5):
            for j in range(5):
                indice = randint(0, len(self.images) - 1)
                x = j * DIM
                y = i * DIM
                self.canvas.create_image(x, y, anchor=tk.NW, image=self.images[indice])

if __name__ == '__main__':
    # Exercice 1
    mon_appli = VueMessage("Bonjour à tous")
    
    # Exercice 2
    mon_appli2 = VueMessage2()
    
    # Exercice 3, 4, 5
    mon_appli3 = VueDemineur()
    
    # Exercice 6
    mon_appli4 = VueDemineurGrid()