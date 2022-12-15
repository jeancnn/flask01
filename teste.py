import hashlib


jean = "teste"

cript = hashlib.sha256(jean.encode('utf-8')).hexdigest()
print(cript)
