# Detecção de Fraudes em sistemas de pagamento online

# Projeto
- Detecção de fraudes - Classificação

# Repositório
- Notebook.ipynb - Notebook com EDA, limpeza, amostragem, balanceamento, pré-processamento, seleção de modelos, seleção de features, tunagem e métricas de modelos

# 1 Introdução e Data Source

Dados de transações de pagamentos, debitos, saques, depósitos e transferencias foram disponibilizados em um dataset no Kaggle. O dataset compõe dados de tipo de pagamento, saldo antes e após da transação da conta de origem e destino e rótulos de operações comuns (rótulo = 0) e fraudulentas (rótulo = 1)

https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset

Os dados são naturalmente desbalanceados, o número de transações fraudulentas registrados corresponde à apenas 1.29% das transações. (8.213 transações fraudulentas e 6.354.407 transações comuns).

# 2 Objetivos

O objetivo desse projeto é criar um modelo que seja capaz de identificar corretamente transações fraudulentas para que, dessa forma, as instituições financeiras possam  impedir que a transação seja realizada e bloqueá-los como medida de segurança.

Obter um modelo com alta revocação e alta precisão para classificação de transações fraudulentas, portanto, é fundamental.

# Em andamento: Construção arquitetura (Kafka - streaming de dados) para consumo do modelo simulando uma transação real.

# 3 Metodologia

- Análise Exploratória: Uma analise exploratória dos dados foi conduzida no próprio notebook para traçar o perfil das transações fraudulentas.
- Pré-Processamento: OneHotEncoding no tipo de transação, Normalização em dados numéricos
- Amostragem: Realizado uma amostragem com dados de 20% fraudes e 80% transações comuns
- Taxa de balanceamento e seleção de modelo: Conduzido experimentos com diversos modelos para definir a melhor taxa de balanceamento para identificar as transações fraudulentas.
- Seleção de features: com o modelo selecionado, analizou-se a correlação da variável entre si e com a variável alvo e foi conduzido experimentos com o modelo para definir o melhor conjunto de features


# Resultados
  
  O modelo RandomForest eleito como preditor e apresenta as seguinte performance nos dados de teste:
  
  Revocação classe 1 - Fraudes: 99,70%  
  Revocação classe 0 - Transações comuns: 98,77%  
  Acurácia:  98,97%  
  AUC:  0,9925  


# Stack
Numpy, Pandas, Scikit-Learn, Matplotlib
