import re
from random import randrange

DEMO_TABLE = 'examples/example.txt'

def rollParser(ref):
    stringValue = ref.group(0)[1:-1]
    # if dice roll
    diceRoll = re.search(r"d\d+", stringValue)
    if diceRoll is not None:
        num = int(diceRoll.group(0)[1:])
        return str(randrange(1,num))
    # otherwise return table value
    return rollTable(stringValue).strip()

def selectionParser(val):
    stringValue = val.group(0)[1:-1]
    choices = stringValue.split(",")
    return choices[randrange(len(choices))]

def lineParser(lineToParse):
    keys = re.sub(r'\[.*?\]', lambda x: rollParser(x), lineToParse)
    keys = re.sub(r'\{.*?\}', lambda x: selectionParser(x), keys)
    return keys

def rollTable(tableName = DEMO_TABLE):
    f = open("tables/" + tableName)
    num_lines = sum(1 for line in f)
    f.seek(0)
    line_rolled = randrange(num_lines)
    # print(f.readlines())
    line = f.readlines()[line_rolled]
    line = lineParser(line)
    f.close()
    return line

# print(rollTable("Deck of Many Things (22 Cards).txt"))
# rollParser()
print(rollTable("examples/example.txt"))
