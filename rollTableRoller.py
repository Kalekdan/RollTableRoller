import re
from random import randrange

DEMO_TABLE = 'examples/example.txt'

def expressionParser(ref):
    stringValue = ref.group(0)[1:-1]
    # if dice roll
    diceRoll = re.search("d\d+", stringValue)
    if diceRoll is not None:
        num = int(diceRoll.group(0)[1:])
        return str(randrange(1,num))
    # otherwise return table value
    return rollTable(stringValue).strip()

def lineParser(rollToParse):
    keys = re.sub('\[.*?\]', lambda x: expressionParser(x) ,rollToParse)
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

print(rollTable("examples/example.txt"))
# rollParser()
