# ---------------------------------------------------------------------------
# TRABALHO ACADÊMICO - ESTATÍSTICA E MODELAGEM
# Disciplina: Introdução ao Cálculo
# Curso: Análise e Desenvolvimento de Sistemas
#
# Exemplo de Aplicação Prática:
# Cálculo de probabilidade utilizando a integral de uma Função Densidade
# de Probabilidade (f.d.p.) de uma distribuição normal.
# ---------------------------------------------------------------------------

# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# SciPy: Biblioteca fundamental para computação científica, que contém
#        módulos para estatística, otimização, álgebra linear e, mais
#        importante para nós, cálculo de integrais e distribuições.
# NumPy: Biblioteca para computação numérica, usada aqui para definir
#        os pontos para plotagem do gráfico.
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# 2. DEFINIÇÃO DOS PARÂMETROS DO PROBLEMA
# Cenário: Análise do tempo de resposta de um servidor web.
# Os dados seguem uma distribuição normal.

# Média (μ) do tempo de resposta em segundos.
# Representa o valor esperado ou o centro da distribuição.
media = 2.5

# Desvio padrão (σ) do tempo de resposta em segundos.
# Representa a dispersão ou variabilidade dos dados em torno da média.
desvio_padrao = 0.5

# Intervalo de interesse [a, b] para o qual queremos calcular a probabilidade.
# Queremos saber a probabilidade de o tempo de resposta estar entre 2s e 3s.
a = 2.0
b = 3.0

# 3. CÁLCULO DA PROBABILIDADE
# A probabilidade P(a <= X <= b) é calculada pela integral da f.d.p.
# no intervalo [a, b].
# Computacionalmente, usamos a Função de Distribuição Acumulada (CDF),
# que já representa o valor da integral da f.d.p. de -∞ até um ponto x.
# Portanto, P(a <= X <= b) = CDF(b) - CDF(a).

# A função `norm.cdf(x, loc=media, scale=desvio_padrao)` calcula a
# probabilidade acumulada até o ponto x.
prob_ate_b = norm.cdf(b, loc=media, scale=desvio_padrao)
prob_ate_a = norm.cdf(a, loc=media, scale=desvio_padrao)

# A probabilidade do intervalo é a diferença entre as probabilidades acumuladas.
probabilidade_intervalo = prob_ate_b - prob_ate_a

# 4. APRESENTAÇÃO DOS RESULTADOS
# Exibimos o resultado.
print("--- ANÁLISE DE TEMPO DE RESPOSTA DO SERVIDOR ---")
print(f"Parâmetros da Distribuição Normal:")
print(f"  - Média (μ): {media}s")
print(f"  - Desvio Padrão (σ): {desvio_padrao}s")
print("-" * 45)
print(f"Cálculo de Probabilidade para o intervalo [{a}s, {b}s]:")
# O resultado é multiplicado por 100 para ser exibido como percentual.
print(f"  - P({a} <= X <= {b}) = {probabilidade_intervalo:.4f}")
print(f"  - Probabilidade: {probabilidade_intervalo:.2%}")
print("-" * 45)
print("Conclusão: A probabilidade de o tempo de resposta do servidor estar")
print(f"entre {a} e {b} segundos é de aproximadamente {probabilidade_intervalo:.2%}.")


# 5. VISUALIZAÇÃO GRÁFICA
# Esta parte gera um gráfico da curva da distribuição normal e destaca a
# área que corresponde à probabilidade calculada.

# Cria um intervalo de valores de x para plotar a curva (de μ - 4σ a μ + 4σ).
x = np.linspace(media - 4 * desvio_padrao, media + 4 * desvio_padrao, 1000)

# Calcula a Função Densidade de Probabilidade (f.d.p.) para cada valor de x.
pdf_y = norm.pdf(x, loc=media, scale=desvio_padrao)

# Configura e plota o gráfico.
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_y, 'b-', label='f.d.p. da Distribuição Normal')

# Preenche a área sob a curva que corresponde ao intervalo [a, b].
x_fill = np.linspace(a, b, 100)
y_fill = norm.pdf(x_fill, loc=media, scale=desvio_padrao)
plt.fill_between(x_fill, y_fill, color='orange', alpha=0.6, label=f'Área = P({a} ≤ X ≤ {b})')

# Adiciona títulos e legendas para clareza.
plt.title('Distribuição Normal do Tempo de Resposta do Servidor', fontsize=16)
plt.xlabel('Tempo de Resposta (segundos)', fontsize=12)
plt.ylabel('Densidade de Probabilidade', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Exibe o gráfico.
plt.show()

