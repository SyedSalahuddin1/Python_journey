from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Friends name", ["Faisal", "Nabeel", "Ali", "Azeem", "Mujtaba"])
table.add_column("School Friends fields", ["Business", "Medical", "Self-employed", "Graduated", "Graduated"])
table.align = "r"
print(table)
