# Same Game (Jeu du Same)

A Python / Tkinter implementation of the classic **Same** puzzle game, built with a model/view separation. The board is a grid of colored spheres displayed as clickable buttons.

> **Status:** work in progress. The current version covers the first step: displaying the grid, removing a sphere on click, and starting a new game. Group removal, gravity and scoring are not implemented yet.

## Features

- 15 × 20 grid of randomly colored spheres (4 colors by default)
- Click a sphere to remove it
- Score label
- "Nouvelle Partie" button to reset the board
- "Au revoir !" button to quit

## Project structure

```
same/
├── img/          # Sphere images (.gif) in 4 sizes
├── same.py       # Model (Case, ModeleSame) + view (VueSame) + entry point
├── vue1.py       # Alternative view, reuses the model from same.py
└── tki.py        # Separate Tkinter exercises (messages, minesweeper images)
```

## Requirements

- Python 3.8+
- Tkinter (included with Python on Windows and macOS)

On Linux, install it with:

```bash
sudo apt install python3-tk
```

No other dependencies are needed.

## Running the game

```bash
cd same
python same.py
```

Or the alternative view:

```bash
python vue1.py
```

On macOS / Linux, use `python3` instead of `python` if needed.

## Changing the sphere size

The game uses the `medium_sphere` images (56 × 38 px). If the window is too large or too small for your screen, change the file prefix in the image-loading lines of `same.py` and `vue1.py`:

| Prefix            | Image size |
| ----------------- | ---------- |
| `grand_sphere`    | 75 × 50    |
| `medium_sphere`   | 56 × 38    |
| `petit_sphere`    | 38 × 25    |
| `tres_petit_sphere` | 29 × 19  |

## About `tki.py`

`tki.py` contains standalone Tkinter exercises. It loads images from an `images_demineur/` folder (`un.gif` ... `huit.gif`, `mine.gif`) that is **not included** in this repository, so add that folder next to the script before running it. It opens its windows one after another; close each one to see the next.

## How it works

- `Case` holds the color of one cell (`-1` means empty).
- `ModeleSame` holds the grid, the score and the game rules.
- `VueSame` builds the Tkinter window, draws the grid, and connects each button to the model.

## Roadmap

- [ ] Remove groups of adjacent same-colored spheres
- [ ] Gravity (spheres fall, empty columns shift left)
- [ ] Score computation
- [ ] End-of-game detection
