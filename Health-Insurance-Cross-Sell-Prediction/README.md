<h1 align=center><a target="_blank" href="https://demo.gethugothemes.com/liva" rel="nofollow">Time Random Forest</a> <a  target="_blank"></a></h1>
</div>
 <div style="display: inline_block"><br>
<img align="right" img class="giphy-gif-img giphy-img-loaded" src="https://media1.giphy.com/media/4mc6Dsn9gyWTS/200w.gif?cid=ecf05e47bhsy1gj453r24ma84o3sdpb5x0l5uys3qfp3il1h&amp;rid=200w.gif&amp;ct=s" width="200" height="200" alt="car accident smoke Sticker" style="background: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4AQMAAACSSKldAAAABlBMVEUhIiIWFhYoSqvJAAAAGElEQVQY02MAAv7///8PWxqIPwDZw5UGABtgwz2xhFKxAAAAAElFTkSuQmCC&quot;) 0px 0px;">
 </div>
 
# Projeto: [Health Insurance Cross Sell Prediction 🏠 🏥](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction)
- Projeto de classificação de clientes interessados em seguros de veículos

# Live no Youtube
- [Data Science aplicado a otimização de Cross-Selling de Seguros de Veículos](https://www.youtube.com/watch?v=u38TWKPP_Q4)

# Colaboradores:  
[Alex Graziani](https://github.com/awildt01),    
[Bruno Freitas](https://github.com/Freitashbruno),  
[Lucas Chitolina](https://github.com/Chitolina) e     
[Weber Godoi](https://github.com/webercg)    


<img align="center" img class="giphy-gif-img giphy-img-loaded" src="https://github.com/webercg/Data-Science-Projects/blob/main/Health-Insurance-Cross-Sell-Prediction/app-streamlit2.gif" width="800" height="600" alt="car accident smoke Sticker" style="background: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4AQMAAACSSKldAAAABlBMVEUhIiIWFhYoSqvJAAAAGElEQVQY02MAAv7///8PWxqIPwDZw5UGABtgwz2xhFKxAAAAAElFTkSuQmCC&quot;) 0px 0px;">

# Repositórios v1.0 Projeto
● [Análise Exploratória](https://github.com/webercg/Health-Insurance-Cross-Sell-Prediction/tree/main/EDA) <img align="center" alt="Jupyter" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">  
● [Gerenciamento de Tarefas](https://trello.com/b/Nypkyrp3/randomforest)  
● [Notebooks na núvem - Spark](https://github.com/webercg/Data-Science-Projects/tree/main/Health-Insurance-Cross-Sell-Prediction/Engenharia%20de%20dados/pyspark)  
● [Modelo Preditivo](https://github.com/webercg/Health-Insurance-Cross-Sell-Prediction/tree/main/API/model)  
● [Dashboard BI](https://github.com/webercg/Health-Insurance-Cross-Sell-Prediction/tree/main/DashBoard-PowerBI)  
● [Apresentação](https://github.com/webercg/Health-Insurance-Cross-Sell-Prediction/tree/main/apresentacao)  
● [Live no Youtube](https://www.youtube.com/watch?v=u38TWKPP_Q4)

# Repositórios v2.0 Projeto
● [Notebook com modelagem da V2.0 Projeto](https://github.com/webercg/Data-Science-Projects/blob/main/Health-Insurance-Cross-Sell-Prediction/Cross-Selling%20V2.0.ipynb) 


# Contextualização e regras de negócio

Uma seguradora de saúde, visando expandir seu portfólio de produtos ao ofertar também seguros de veículos realizou uma pesquisa de opinião com seus clientes para identificar o interesse pelo novo seguro. A seguradora, a partir das respostas precisa identificar padrões no perfil de clientes interessados e traçar as estratégias mais assertivas na conversão de novos clientes.

Construir um modelo para prever se um cliente estaria interessado em seguro de veículo é extremamente útil para a empresa, pois ela pode planejar adequadamente sua estratégia de comunicação para alcançar esses clientes e otimizar seu modelo de negócios e receita. Para construção da maquina preditiva é elencado dados dados demográficos (gênero, idade, tipo de código de região), informações sobre o veículo (idade do veículo, danos), e características da apólice (premium, canal de fornecimento).


# Objetivos:

1) Produzir um modelo preditivo para classificação de potenciais clientes a firmar seguro de veículo com a companhia.

2) Avaliar o impacto do Canal de Vendas sobre o interesse de clientes e inferir o Canal de Venda que maximiza a probabilidade de clientes adquirirem o seguro de veículos

3) Avaliar os possíveis ganhos com a conversão de clientes de seguros de veículos que possam adquirí-lo após oferta de descontos no seguro de saúde.

4) Modelar uma função de custo considerando as regras de negócio para selecão do melhor modelo

5) Deploy no StreamLit para consumo do modelo de Machine Learning



# Resultados

## Conclusões gerais e ganhos financeiros
- O maior desconto que poderia ser dado para evitar perdar e agarriar mais clientes é de 30.68%.
- Ao realizar o comparativo das operações utilizando-se Machine Learning há um ganho total de 4.2 Mi com a implementação do modelo.
- Isso equivale a um ganho de 11.10 reais por cliente do seguro de saúde.

## Analise desconto vs interesse pelo seguro
- Não foi realizada uma análise do desconto sobre o interesse de clientes. Na prática, o efeito de ofertar um desconto aos clientes, fomenta um sentimento de escassez na oferta do seguro de veículo. Esse comportamento de escassez não é aprendido pela maquina preditiva, ao optarmos por alimentar a base com um valor menor no seguro de saúde, o modelo de machine learning aplicaria apenas os padrões aprendidos nos dados, portanto, faria a relação direta com o poder aquisitivo do cliente vs interesse por outro seguro, enviesando toda a análise.

## Analise canal de venda vs interesse pelo seguro
- Na v1.0 desse projeto o canal de venda compunha o conjunto de features do modelo final, nesse modelo não há como inferir, uma vez que essa feature não foi selecionada. A probabilidade de cada cliente adquirir o seguro era calculada por meio do método predict_proba() do RandomForest, essas probabilidades eram calculadas para todos os canais de vendas a cada predição realizada pelo usuário final no streamlit. Dessa forma, o usuário poderia escolher o melhor canal de vendas para abordar o cliente.


## Regras de negócio aplicada a modelagem:
- Dado o desbalanceamento das classes e os custos o modelo priorizará o acerto de 1 cliente interessado em detrimento de 40 clientes não interessados.
- Isso equivale a dizer que o modelo priorizará no tradeoff um ganho acima de +8.5% na taxa de acerto de pessoas interessadas em detrimento de uma taxa de até -1% na taxa de acertos de pessoas sem interesse, ou um ganho acima de +1% na taxa de acerto de pessoas sem interesse em detrimento de uma taxa de até -8.5% de pessoas interessadas.

## Performance do modelo
- Acerta 99,69% de clientes interessados (Recall classe 1)
- Acerta 51,86% de Clients não interessados (Recall classe 0)
- AUC: 0.7577 


# Stack
Numpy, Pandas, Seaborn, Matplotlib, Spark, PySpark, Azure Databricks, PowerBI, Streamlit, Flask.
