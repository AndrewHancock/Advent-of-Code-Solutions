import copy


def loop_through(start: int, end: int, opcodes):
    x = 0
    """
    Note: Because this is just numbers, you can use the array "copy()" function instead of "deepcopy."
    Which one you use depends on what you have in the array.
    Things like ints, floats, strings, tuples, etc., can be shallow copied.
    
    For objects, arrays, dictionaries, etc., you would do deep copy ONLY if you need ot update some variable on the new 
    copy and not have it also update the old copy. 
    Arrays hold bindings (references, pointers) to objects. Therefore, a shallow just binds a new reference to the object.
    A deep copy, by contrast, calls either the special __copy__() or __deepcopy__() methods of the object in question, 
    which return appropriately copied objects. You may have to write these methods if you want to support deep copy,
    although there may be some default handler? 
    Read more here:
    https://docs.python.org/2/library/copyw.html
    
    Int never needs a deep copy so I changed this to copy.      
    """
    listofopcodes = copy.copy(opcodes)

    listofopcodes[1] = start
    listofopcodes[2] = end
    while True:
        op = listofopcodes[x]
        param1 = listofopcodes[listofopcodes[x+1]]
        param2 = listofopcodes[listofopcodes[x+2]]
        param3 = listofopcodes[listofopcodes[x+3]]
        if op == 1:
          listofopcodes[param3] = param1 + param2
        elif op == 2:
          listofopcodes[param3] = param1 * param2
        if listofopcodes[0] == 19690720:
          print(str(start) + " " + str(end))

        x+=4


def part2():
    with open("input.txt", "r") as f:
        data = f.read()

    opcodes = [int(x) for x in data.split(",")]

    for i in range(0, 100):
      for j in range (0, 100):
        loop_through(i, j)
