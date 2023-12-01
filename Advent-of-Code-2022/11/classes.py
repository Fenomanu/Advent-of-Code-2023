class Monkey:
    id = 0
    objects = []
    op1 = 0 # 0 = old
    op = 0 # 0 = + | 1 = *
    op2 = 0 # 0 = old
    test = 1
    monkey_true = 0
    monkey_false = 0
    inspected = 0

    def __init__(self, id: int, objs: list, op1: int, op: int, op2: int, test : int, monkey_true : int, monkey_false : int):
        self.id = id
        self.inspected = 0
        self.op = op
        self.op1 = op1
        self.op2 = op2
        self.objects = objs
        self.test = test
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false

    def calculate(self):
        res = 0
        if self.op==0:
            res = self.opN(self.op1) + self.opN(self.op2)
        elif self.op==1:
            res = self.opN(self.op1) * self.opN(self.op2)
        return res

    def inspect(self):
        new_value = self.calculate()
        self.inspected += 1
        head = self.objects.pop(0)
        return new_value

    def chill(self, obj):
        return int(obj/3)

    def to_string(self):
        res = "Monkey {0}: \n Starting Items: {1} \n Operation: new = {2} {3} {4} \n Test: divible by {5} \n \t If true: throw to monkey {6} \n \t If false: throw to monkey {7}"

        return res.format(self.id, self.objects, self.op1, self.op, self.op2, self.test, self.monkey_true, self.monkey_false)
    
    def throw_obj(self, value):
        if value % self.test == 0:
            return self.monkey_true
        else: return self.monkey_false

    def opN(self, val):
        if val==0: return self.objects[0]
        else : return val


class Monkey2:
    id = 0
    objects = []
    op1 = 0 # 0 = old
    op = 0 # 0 = + | 1 = *
    op2 = 0 # 0 = old
    test = 1
    monkey_true = 0
    monkey_false = 0
    inspected = 0

    def __init__(self, id: int, objs: list, op1: int, op: int, op2: int, test : int, monkey_true : int, monkey_false : int):
        self.id = id
        self.inspected = 0
        self.op = op
        self.op1 = op1
        self.op2 = op2
        self.objects = objs
        self.test = test
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false

    def calculate(self):
        res = 0
        if self.op==0:
            res = self.opN(self.op1) + self.opN(self.op2)
        elif self.op==1:
            res = self.opN(self.op1) * self.opN(self.op2)
        return res

    def inspect(self):
        new_value = self.calculate()
        self.inspected += 1
        head = self.objects.pop(0)
        return new_value

    def chill(self, obj):
        return int(obj/3)
    
    def chill_mod(self, obj, module):
        return obj % module

    def to_string(self):
        res = "Monkey {0}: \n Starting Items: {1} \n Operation: new = {2} {3} {4} \n Test: divible by {5} \n \t If true: throw to monkey {6} \n \t If false: throw to monkey {7}"

        return res.format(self.id, self.objects, self.op1, self.op, self.op2, self.test, self.monkey_true, self.monkey_false)
    
    def throw_obj(self, value):
        if value % self.test == 0:
            return self.monkey_true
        else: return self.monkey_false

    def opN(self, val):
        if val==0: return self.objects[0]
        else : return val