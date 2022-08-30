# Detecção de Fraude de cartão de crédito

# Projeto
- Detecção de fraudes - Classificação

# Repositório
- Deteccao de Fraude + EDA.ipynb - Notebook com EDA, tunagem e seleção de modelos.

# Repositório V 2.0 Projeto
- Notebook Projeto V 2.0: [V2.0 do Projeto](https://github.com/webercg/Data-Science-Projects/blob/main/CreditCard%20Fraud/Deteccao%20de%20Fraude%20-%20V%202.0%20.ipynb)

O projeto passou por uma atualização aplicando-se boas práticas para validação do modelos, evitar data leakage e melhorar a performance em produção.

# Introdução e Data Source

Dados de transações de cartão de créditos foram capturadas num período de 48h. A fim de anonimizar e proteger os clientes, aplicou-se a técnica de PCA (Principal Component Analysis) que reduziu o número de features para 30 no total, todas adotando um formato numérico.

Os dados foram rotulados por meio da coluna "Class" que diferencia uma transação comum de uma fraude.

Class: 1 - Transação Fraudulenta
Class: 0 - Transação Comum

Os dados são naturalmente desbalanceados, o número de transações fraudulentas registrados corresponde à apenas 0,17% das transações. (492 transações fraudulentas e 284.315 transações comuns).

#  Objetivos

O objetivo desse projeto é criar um modelo que seja capaz de identificar corretamente transações fraudulentas para que, dessa forma, as operadoras de cartões possam  impedir que a transação seja realizada e bloqueá-los como medida de segurança.

Obter um modelo com alta revocação e alta precisão para classificação de transações fraudulentas, portanto, é fundamental.

# Em andamento: Construção arquitetura (Kafka - streaming de dados) para consumo do modelo simulando uma transação real.


# Análise Exploratória de Dados (EDA)

    Observa-se que as transaçõs comuns tem um padrão:
    - Atingem o mínimo por volta das 04h da madrugada e crescem até atingir o pico ás 09h da manhã que se mantém até as 21h quando começa a cair o número de transações.
    
    As transações fraudulentas não possui um padrão de distribuição, no entanto, é possível verificar que ocorrem majoritariamente em 2 períodos:

    - As 03h da madrugada, quando não há muitas transações comuns ocorrendo.
    - As 11h da manhã. Embora seja um horário com alto número de transações comuns, é bastante anormal a queda do número de transações fraudulentas nos horários subjacentes 10h e 12h. 
    - As transações comuns possuem uma média estável e inferior comparada as transações fraudulentas que possuem médias altas e com alto desvio padrão.
    - É possível observar um pico nos valores das transações fraudulentasas 0h e as 10h, mas isso pode ser efeito da alta variância dessas observações.

# Resultados
  5 Modelos foram selecionados:
  - LGBMClassifier
  - XGBClassifier, 
  - RandomForestClassifier, 
  - DecisionTreeClassifier
  - LinearSVC. 
  
  O melhor modelo foi selecionado a partir de uma função de custo que contabiliza o tradeoff em erros de classificação de fraudes / não fraudes. O modelo LGBMClassifier eleito como preditor e apresenta as seguinte performance nos dados de teste:
  
  Revocação classe 1 - Fraudes: 89,03%
  Revocação classe 0 - Transações comuns: 99,54%
  Acurácia:  99,54%
  AUC:  0,9429


## Características e curiosidades do projeto
- Foi criado uma função de custo relacionados aos falsos positivos e falsos negativos para orientar a escolha do melhor modelo
- O modelo prioriza o acerto de 2843 (+1) transações não fraudulentas em detrimento de 165 fraudes devido aos custos e a proporção de ocorrencias de transações fraudulentas.
- Isso equivale a dizer que o modelo prioriza um ganho de 1% na taxa de acerto de não fraudes em detrimento de 33% na taxa de acertos de fraudes.
- Recomendação: Alterar a função de custo incorporando uma função de probabilidade de churn entre clientes vitimas de fraudes e não vítimas assim como os custos relacionados ao churn.


# GAP e possíveis melhorias

- Há poucos exemplos de transações fraudulentas (492), embora tenha-se validado as métricas com os dados de treino, é possível que ao colocar o modelo em produção haja uma queda na revocação sendo necessário o retreinamento com novos exemplos de transações fraudulentas. 

- Além disso, o dataset utilizado provém de uma coleta em 48h e não há mais informações sobre os dias em que foram coletados, pode ocorrer uma mudança de comportamento nas transações fraudulentas de acordo com o período do ano (Natal, Carnaval etc) ou com o dia da semana (Finais de Semana e Feriados prolongados). Dessa forma, pode ser necessário retreinar o modelo para contabilizar comportamentos atipicos possívelmente não considerados.


# Stack
Numpy, Pandas, Scikit-Learn, Seaborn, Matplotlib
