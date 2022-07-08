# Detecção de Fraude de cartão de crédito

# Projeto
- Detecção de fraudes - Classificação

# Repositório
- Deteccao de Fraude + EDA.ipynb - Notebook com EDA, tunagem e seleção de modelos.

# 1 Introdução e Data Source

Dados de transações de cartão de créditos foram capturadas num período de 48h. A fim de anonimizar e proteger os clientes, aplicou-se a técnica de PCA (Principal Component Analysis) que reduziu o número de features para 30 no total, todas adotando um formato numérico.

Os dados foram rotulados por meio da coluna "Class" que diferencia uma transação comum de uma fraude.

Class: 1 - Transação Fraudulenta
Class: 0 - Transação Comum

Os dados são naturalmente desbalanceados, o número de transações fraudulentas registrados corresponde à apenas 0,17% das transações. (492 transações fraudulentas e 284.315 transações comuns).

# 2 Objetivos

O objetivo desse projeto é criar um modelo que seja capaz de identificar corretamente transações fraudulentas para que, dessa forma, as operadoras de cartões possam  impedir que a transação seja realizada e bloqueá-los como medida de segurança.

Obter um modelo com alta revocação e alta precisão para classificação de transações fraudulentas, portanto, é fundamental.

# Em andamento: Construção arquitetura (Kafka - streaming de dados) para consumo do modelo simulando uma transação real.

# 3 Metodologia

- Uma analise exploratória dos dados foi conduzida no próprio notebook para traçar o perfil das transações fraudulentas.

- Experimentos iniciais com LazyPredictor para pré-seleção 5 modelos com maiores AUC (Área sobre a curva (FP vs TP). LGBMClassifier, XGBClassifier, RandomForestClassifier, DecisionTreeClassifier e LinearSVC.

- Para cada modelo realizou-se diversos variando-se o fator de balanceamento dos dados que seriam alimentados ao modelo avaliando-se a AUC. O fator de balaceamento foi determinado a partir da maximização da métrica AUC. Uma vez determinado o fator de balanceamento os dados foram separados em dados de treino e teste.

- Para cada modelo e fator de balanceamento foi realizado experimentos para determinar os melhores hyperparâmetros. A métrica utilizada para retorno dos melhores hyperparâmetros foi a revocação para classe 1 (recall 1), contudo,  foram selecionados os 3 melhores conjuntos de hiperparâmetros que maximizavam a AUC. Por fim, um único modelo foi selecionado a partir de validação estatística por meio de teste de hipoteses entre os 3 conjuntos candidatos.
 
- Ao final das experimentações haviam 5 modelos tunados. Um único modelo foi selecionado validando-o estatisticamente a superioridade do modelo via testes de hipoteses.

# 4 Resultados Análise Exploratória de Dados

## 4.1 Em que hora do dia há maior ocorrência de transações? e transações fraudulentas?
    Observa-se que as transaçõs comuns tem um padrão:
    - Atingem o mínimo por volta das 04h da madrugada e crescem até atingir o pico ás 09h da manhã que se mantém até as 21h quando começa a cair o número de transações.
    
    As transações fraudulentas não possui um padrão de distribuição, no entanto, é possível verificar que ocorrem majoritariamente em 2 períodos:

    - As 03h da madrugada, quando não há muitas transações comuns ocorrendo.
    - As 11h da manhã. Embora seja um horário com alto número de transações comuns, é bastante anormal a queda do número de transações fraudulentas nos horários subjacentes 10h e 12h. 
    
## 4.2 Há alguma tendência no valor médio das transações fraudulentas de acordo com o horário do dia?
    - As transações comuns possuem uma média estável e inferior comparada as transações fraudulentas que possuem médias altas e com alto desvio padrão.

    - É possível observar um pico nos valores das transações fraudulentasas 0h e as 10h, mas isso pode ser efeito da alta variância dessas observações.

## 4.3 Quantas transações fraudulentas foram registradas? e quantas transações comuns?

     - Os dados são altamente desbalanceados, a base possui 284315 registros comuns e 492 registros de fraudes. Será necessário aplicar técnicas para o balanceamento.

## 4.4 Como estão distribuidos os dados de cada variável?
   
   Nenhuma variável apresentou distribuição normal, foi aplicado logarítmo na variável "Amount" que corresponde ao valor da transação a fim de normalizá-la e aumentar a performance dos algorítmos de Machine Learning

# Resultados Machine Learning
  5 Modelos foram selecionados:
  - LGBMClassifier
  - XGBClassifier, 
  - RandomForestClassifier, 
  - DecisionTreeClassifier
  - LinearSVC. 
  
  O modelo LGBMClassifier eleito como preditor e apresenta as seguinte performance nos dados de teste:
  
  Revocação classe 1 - Fraudes: 96,13%
  Revocação classe 0 - Transações comuns: 98,33%
  Acurácia:  98,33%
  AUC:  0,9723


# GAP e possíveis melhorias


- Há poucos exemplos de transações fraudulentas (492), embora tenha-se validado as métricas com os dados de treino, é possível que ao colocar o modelo em produção haja uma queda na revocação sendo necessário o retreinamento com novos exemplos de transações fraudulentas. 

- Além disso, o dataset utilizado provém de uma coleta em 48h e não há mais informações sobre os dias em que foram coletados, pode ocorrer uma mudança de comportamento nas transações fraudulentas de acordo com o período do ano (Natal, Carnaval etc) ou com o dia da semana (Finais de Semana e Feriados prolongados). Dessa forma, pode ser necessário retreinar o modelo para contabilizar comportamentos atipicos possívelmente não considerados.


# Stack
Numpy, Pandas, Scikit-Learn, Seaborn, Matplotlib
