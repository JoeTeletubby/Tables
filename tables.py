import texttable

version = "1.2.0"

class MultipleInstancesError(Exception):
    pass

class Table:
    def __init__(self, title, columns, headers):
        self.title = title
        self.col_a = columns
        self.heads = headers
        self.table = []
    
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
        table.header(self.heads)
        for x in self.table:
            table.add_row(x.values())
        return table.draw()
    
    def __repr__(self):
        return f"<Table: {self.title} with values {self.table}>"
