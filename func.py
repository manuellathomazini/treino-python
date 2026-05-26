def bin(numero):  # Função para transformar número em binário
    seq_bin = []  # Representa a sequência de números do resultado binário
    while True:   # Loop para calcular a sequência do número binário
        resto = numero % 2
        numero //= 2
        seq_bin.insert(0, str(resto))
        if numero == 0:
            break
    resultado_bin = ""   # Variável para armazenar o resultado concatenado do número binário
    for i in range(len(seq_bin)):   # Loop para concatenar a sequência do número binário
        resultado_bin += seq_bin[i]
    num_bin = int(resultado_bin)   # Variável para armazenar o resultado do número binário convertido para inteiro
    return num_bin   # Retorna o resultado do número inteiro binário