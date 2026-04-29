# A Lot of Games 🎮

A growing collection of games and interactive toys I've built in Python while learning Pygame, game loops, collision detection, and "wait, why does the dino keep falling through the floor?"

13 games and counting. All single-file, all runnable, all written from scratch.

---

## Why this repo exists

Every programmer learns by rebuilding the things they grew up playing. This is mine — a sandbox where I've reimplemented classics, prototyped weird ideas, and learned a new piece of game-loop or graphics logic with each one.

Some are polished. Some are jank. All of them taught me something.

---

## What's inside

| File | Game | What I learned building it |
|------|------|----------------------------|
| `snake.py` | Classic Snake | Game loops, grid-based movement, growing collections |
| `tertis.py` | Tetris | Rotation matrices, piece-locking, line clears, falling-block mechanics |
| `pacman.py` | Pac-Man | Pathfinding, ghost AI, tile-based collision |
| `brick breaker.py` | Brick Breaker | Vector reflection, ball physics, paddle dynamics |
| `dino game.py` | Chrome dino runner | Procedural obstacle spawning, jump physics, infinite scrolling |
| `Space Station Defense Game.py` | Space shooter | Projectile management, enemy waves, sprite collision |
| `egg_catcher.py` | Egg Catcher | Random spawning, scoring, lives, difficulty scaling |
| `maize.py` | Maze game | Grid generation, player movement constraints |
| `physics.py` | Physics sandbox | Gravity, drag, elastic collisions |
| `puzzle.py` | Sliding puzzle | Permutation logic, solvability checks, win-state detection |
| `e_pet.py` | Tamagotchi-style virtual pet | State machines, time-based decay, save/load |

---

## Running any of them

Each game is a single self-contained file. Pick one and go:

```bash
git clone https://github.com/RicKanjilal/A_LOT_OF_GAMES.git
cd A_LOT_OF_GAMES
pip install pygame
python snake.py        # or any other file
```

Most of them use only `pygame`. A few use `random`, `math`, `time` — all standard library. No assets folder required for most.

---

## Things I learned across the collection

- **Game loops are deceptively hard.** The first time you write `while True: handle_input(); update(); draw()` and the screen freezes, you learn what `clock.tick(60)` actually does
- **Collision detection is a rabbit hole.** AABB rectangles → circle-rectangle → pixel-perfect → quadtrees. Each game taught me where on this spectrum I actually needed to be
- **State management gets hairy fast.** A simple Snake clone doesn't need it. Pac-Man absolutely does. Knowing when to switch from "everything in main()" to proper state classes is a real skill
- **Vibes-based physics works for some games and breaks horribly in others.** Brick breaker forgives bad math. The physics sandbox does not
- **Polish is the last 80%.** Every one of these games hits "kind of works" in an evening. Making them *fun to play* takes another week per game

---

## What's next

- [ ] Pong (somehow not in the list yet)
- [ ] A proper top-down shooter with a level system
- [ ] Sokoban — the puzzle game I keep meaning to clone
- [ ] Convert the favorites to web (Pygame → Pyodide → playable on GitHub Pages)
- [ ] Add screenshots/GIFs to this README so people can see what they're getting into

---

## License

MIT — fork them, remix them, replace my janky physics with better physics.

---

Built by **Ric Kanjilal** · Grade 10, Don Bosco School, Liluah · Kolkata
