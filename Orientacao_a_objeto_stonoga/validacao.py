cpf_original = "145.382.206-20"

cpf_sem_validacao = 145382206

total = 0
for peso in range(2,11):
    digito = cpf_sem_validacao % 10
    resultado = digito * peso
    total = total + resultado

    print(total)