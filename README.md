# Roteiro de aula - Gabriel Silva - 3°C #

## Etapa 1

### Explique, em comentários no código, o que representam x e y.

R: O X representa as características de entrada (horas de estudo e número de faltas de cada aluno) e o y representa o resultado/resposta esperada (0 para reprovado, 1 para aprovado).

## Etapa 2 ##

### Explique por que não se deve treinar e testar com os mesmos dados. ###

R: Usar novos dados evita que o modelo apenas decore as respostas (overfitting). Serve para testar se ele aprendeu a lógica correta e se está pronto para seguir.

## Etapa 3

### Explique, em um comentário, o que significa “treinar um modelo”.

R: Significa fornecer os dados de entrada e as respostas corretas para que o algoritmo analise os padrões e crie as regras de decisão.

## Etapa 4

### Explique o papel dos dados de treino nesse processo.

R: Os dados de treino fornecem exemplos com perguntas e respostas para o algoritmo identificar padrões e criar suas regras de decisão.

## Etapa 5

### Explique o que essa métrica (acurácia) indica

R: A acurácia mostra a taxa geral de acerto do modelo, indicando a porcentagem de vezes que ele previu corretamente a situação final do aluno.

## Etapa 6

O modelo teve um ótimo desempenho no teste, acertando 100% das previsões. Porém, árvores de decisão podem memorizar padrões simples demais quando há poucos dados. Por isso, este projeto funciona apenas como um primeiro passo para entender a estrutura do Scikit-Learn. Em uma aplicação real, precisaríamos de milhares de dados e mais informações sobre os estudantes.


## Modelo de relato explicativo

O objetivo desta atividade foi desenvolver um modelo de classificação supervisionada para prever o status de aprovação ou reprovação de alunos. O conjunto de dados foi organizado com a matriz X contendo duas características preditoras (horas semanais de estudo e número de faltas) e o vetor y com os rótulos de classe (0 para reprovado e 1 para aprovado). Aplicou-se a função train_test_split dividindo a base em dados de treino (67%) e teste (33%), garantindo que a validação ocorresse com amostras inéditas para evitar overfitting (memorização dos dados). O algoritmo escolhido foi a Árvore de Decisão (DecisionTreeClassifier), motivado por sua alta interpretabilidade e facilidade de rastreabilidade das regras de negócio. O treinamento foi realizado por meio do método .fit(), seguido da geração de predições com .predict() nos dados de teste. A acurácia obtida refletiu o acerto integral das previsões sobre o conjunto de teste didático. Como principal limitação técnica, destaca-se o tamanho extremamente reduzido da amostra (6 registros), insuficiente para cobrir a variabilidade de um cenário real. Em sistemas em produção, seriam necessários milhares de registros e mais dimensões, como histórico de notas e notas em avaliações parciais. Conclui-se que o experimento cumpriu seu papel de introduzir a estrutura completa do fluxo de Machine Learning com a biblioteca Scikit-Learn.


## Checklist, antes de entregar

O código executa sem erros - sim;

Todas as etapas do fluxo estão presentes - sim;

Há comentários explicativos no código - sim;

O texto final explica o processo com clareza - sim.

