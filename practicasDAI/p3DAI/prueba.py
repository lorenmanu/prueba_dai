import dbm

db = dbm.open('datos.dat', 'c')

# Insert (en disco)
db['237483J'] = 'Hola'

# Select (desde el disco)
datos = db['237483J'].split('|')

db.close()
