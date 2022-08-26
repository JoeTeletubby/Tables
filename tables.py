import texttable

version = "1.3.0"

class MultipleInstancesError(Exception): pass
class ImportInstancesAmountError(Exception): pass

# Types:
# 0: Standard with prettyness
# 1: Without lines

class Table:
    def __init__(self, title, columns, headers, type_=0):
        self.title = title
        self.col_a = columns
        self.heads = headers
        self.table = []
        self.type = type_
    
    def insert(self, values):
        toAppend = {}
        for i in range(0, self.col_a):
            head = self.heads[i]
            toAppend[head] = values[i]
        if self.check(values[0]):
            pass
        else:
            raise MultipleInstancesError
        self.table.append(toAppend)
    
    def check(self, firstValue):
        vals = []
        for x in self.table:
            vals.append(list(x.values())[0])
        if firstValue in vals:
            return False
        return True

    def delete(self, firstValue):
        for x in self.table:
            if list(x.values())[0] == firstValue:
                del self.table[self.table.index(x)]

    def change(self, firstValue, newValues):
        for x in self.table:
            if list(x.values())[0] == firstValue:
                self.table[self.table.index(x)] = self.format(newValues)
                return True
        return False

    def format(self, values):
        toReturn = {}
        for i in range(0, self.col_a):
            head = self.heads[i]
            toReturn[head] = values[i]
        return toReturn

    def __str__(self):
        table = texttable.Texttable()
        if self.type:
            table.set_deco(texttable.Texttable.HEADER)
        table.header(self.heads)
        for x in self.table:
            table.add_row(x.values())
        return table.draw()
    
    def clear(self):
        self.table = []

    def xclear(self):
        self.col_a = 0
        self.heads = []
        self.table = []

    def export(self):
        string = ""
        string += str(self.col_a) + ";"
        string += ";".join(self.heads) + ";"
        for x in self.table:
            string += ";".join(list(map(str, x.values()))) + ";"
        return string[:-1]

    exportt = export

    def importt(self, string):
        values = string.split(";")
        self.xclear()
        self.col_a = int(values[0])
        for x in range(0, self.col_a):
            self.heads.append(values[x+1])
        for x in range(0, self.col_a+1):
            values.pop(0)
        if len(values) % self.col_a != 0:
            raise ImportInstancesAmountError
        for x in range(0, int(len(values) / self.col_a)):
            append = []
            for y in range(0, self.col_a):
                append.append(values[self.col_a * x + y])
            self.insert(append)

    def __repr__(self):
        return f"<Table: {self.title} with values {self.table}>"
