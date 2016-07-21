# Practice: Adventure Game

Save your solution in a directory in `practice/` named `adventure`.

Write a [NetHack](https://en.wikipedia.org/wiki/NetHack)-like terminal based dungeon crawler game.

There are various **entities** in the game.
Make each entity a class in it's own module.

*   Creature
    * Location
    * Health
    * Weapon

*   Weapon
    * Location (or None if picked up)
    * Damage

*   Potion
    * Location
    * Health Restored

Put any functions that manipulate these classes in their respective modules.

Start with just one level that's ten characters by ten characters.
Use different symbols for each kind of entity: `# % ^ P` or whatever.
Place the **player** creature somewhere in it.
Place **monster** creatures somewhere in it.
Place some **potions** and a **weapon** for the player to pick up.

Keep a global list of all entities, and update that list as the game progresses.
Have a `render()` function that renders the whole level from that giant list.
(If you're interested, this is on the way towards a [entity-component system](https://en.wikipedia.org/wiki/Entity_component_system) which is a real-life way of architecting games.)

The game will work in a **stepwise** fashion.
Pause and ask the user where to move or what to do, then re-draw the screen.
