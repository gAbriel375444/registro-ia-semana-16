# trazendo a biblioteca numpy pro código
# e dando um apelido pra ela (np)
import numpy as np

# trazendo a matriz x 
# a coluna da esquerda são as horas de estudo (coluna 0)
# a coluna da direita  são o número de faltas (coluna 1)
# obs: tô usando X em maiúsculo, porque vi que é uma convenção da comunidade, pois representa
# uma tabela com varias linhas e colunas 
X = np.array([
    [2, 1],
    [4, 0],
    [1, 3],
    [3, 1],
    [5, 0],
    [2, 2]
])

# trazendo o vetor y
# 1 pra aprovado e 0 pra reprovado
y = np.array([0, 1, 0, 1, 1, 0])


# digo para o python acessar a pasta dentro do Scikit-Learn que guarda as ferramentas para organizar e testar modelos
# e importo a que eu preciso, que é a de treinar dados 
from sklearn.model_selection import train_test_split


# X_train recebe as horas e faltas de 4 alunos
# X_test  recebe as horas e faltas de 2 alunos de teste
# y_test  recebe os resultados se os 4 alunos foram ou não aprovados
# y_teste recebe os resultados se os 2 alunos de teste foram ou não aprovados

# separando 33% dos dados para teste (2 dos 6 alunos)
# e fixando o random_state (tipo a seed do teste) para manter o mesmo resultado
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)