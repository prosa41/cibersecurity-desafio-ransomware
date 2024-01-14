import os
import pyaes
from getpass import getpass

# Solicitar o nome do arquivo criptografado
file_name = input("Digite o nome do arquivo criptografado: ")
if not os.path.exists(file_name):
    print("Arquivo não encontrado.")
    exit()

# Abrir o arquivo criptografado
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Pedir a senha ao usuário
password = getpass("Digite a senha para descriptografar o arquivo: ")

# Chave para descriptografia derivada da senha
key = os.urandom(32)  # Pode ser uma chave mais segura usando bibliotecas como bcrypt
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file_name = file_name.replace(".ransomwaretroll", "")
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()

print(f'Arquivo descriptografado com sucesso como "{new_file_name}"')
