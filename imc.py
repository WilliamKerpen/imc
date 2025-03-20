# Função para calcular o IMC e determinar a classificação e recomendação
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return imc, "Baixo peso", (
            "É recomendado procurar um médico para avaliação criteriosa do resultado. "
            "Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados."
        )
    elif 18.5 <= imc <= 24.9:
        return imc, "Peso Adequado", (
            "Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da composição corporal, "
            "para compreender se estão dentro do recomendado. Algumas pessoas apresentam IMC dentro da normalidade, "
            "mas têm circunferência abdominal maior que a recomendada e/ou quantidade de massa gorda acima do ideal."
        )
    elif 25.0 <= imc <= 29.9:
        return imc, "Sobrepeso", (
            "O sobrepeso está associado ao risco de doenças como diabetes e hipertensão. Então, atenção! "
            "Consulte um médico e reveja hábitos para reverter o quadro. Também é importante avaliar outros parâmetros, "
            "como a circunferência abdominal."
        )
    elif 30.0 <= imc <= 34.9:
        return imc, "Obesidade Grau I", (
            "É importante buscar orientação médica e nutricional para entender melhor o seu caso, "
            "mesmo que os exames (colesterol e glicemia, por exemplo) estejam normais."
        )
    elif 35.0 <= imc <= 39.9:
        return imc, "Obesidade Grau II", (
            "Indica um quadro de obesidade mais evoluído em relação à classificação anterior e, mesmo com exames laboratoriais "
            "dentro da normalidade, não se deve atrasar a busca por orientação médica e nutricional."
        )
    else:  # IMC >= 40
        return imc, "Obesidade Grau III", (
            "Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada. "
            "É fundamental buscar orientação médica."
        )

# Entrada de dados do usuário, tratando vírgulas e pontos
peso = float(input("Digite seu peso em kg: ").replace(",", "."))
altura = float(input("Digite sua altura em metros: ").replace(",", "."))

# Calcula o IMC e obtém a classificação e recomendação
imc, classificacao, comentario = calcular_imc(peso, altura)

# Exibe os resultados
print(f"\nSeu IMC é {imc:.2f}. Classificação: {classificacao}")
print(f"Comentário: {comentario}")