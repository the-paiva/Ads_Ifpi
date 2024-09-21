from ulid import ULID


# Gerando um novo ULID
meu_ulid = ULID()
print(meu_ulid.timestamp)  # Retorna o timestamp
print(meu_ulid) # Retorna a parte aleatória
