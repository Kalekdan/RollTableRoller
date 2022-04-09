# RollTableRoller

Utility to roll 'roll tables'. Includes the ability to wrap roll tables within roll tables recursively.

## Roll Table Syntax
Roll tables can be created and rolled. Each new outcome must be on a new line in the roll table file.

### Random Values
To include some random features in your outcome, the `[]` syntax can be used.

If you want to include a **random number** in your roll, include it in the string in the format `[d20]`. This example will replace `[d20]` with a random value between 1 and 20 inclusive.

If you want to include another table's roll in your roll, include it in the string in the format `[examples/creatures.txt]`. In this example, a second roll will be made on the creatures roll table, and the value will be substituted into your roll.

_NB: You can theoretically reference a table within itself, but this should usually be avoided to prevent maximum recursion dept errors._

### Example Roll Table
```
You see a pack of [d6] [example/creatures.txt]'s
You are caught in a thunderstorm
You find a [example/container.txt] filled with [d100] copper pieces and [d10] gold. 
```

