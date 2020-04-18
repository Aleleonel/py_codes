from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world"

workbook.save(filename="hello_world.xlsx")
voluntarios = [ 'Alexandre', 'João', 'Natanael', 'Renato', 'Eduardo', 'Leonardo', 'Ronaldo', 'Ferreira', 'Santos', 'Monticelli', 'Claudio', 'Nelson']
print(print(f'{len(   voluntarios  )}'))