version = "1.0.0"

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
        self.table.append(toAppend)
    
    def __str__(self):
        string = "Table: " + str(self.title) + "\nColumns: "
        for x in self.heads:
            string += str(x) + ", " if x != self.heads[-1] else str(x)
        string += "\n\n"
        for x in self.table:
            vals = []
            for v in x.values():
                vals.append(str(v))
            string += ", ".join(vals)
            string += "\n"
        return string
    
    def __repr__(self):
        return f"<Table: {self.title} with values {self.table}>"
