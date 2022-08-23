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

Nosso cliente é uma seguradora que forneceu seguro de saúde para seus clientes, agora eles precisam de sua ajuda na construção de um modelo para prever se os segurados (clientes) do ano passado também terão interesse no seguro de veículos fornecido pela empresa.

Construir um modelo para prever se um cliente estaria interessado em seguro de veículo é extremamente útil para a empresa, pois ela pode planejar adequadamente sua estratégia de comunicação para alcançar esses clientes e otimizar seu modelo de negócios e receita. Agora, para prever se o cliente estaria interessado em seguro de veículo, você tem informações sobre dados demográficos (gênero, idade, tipo de código de região), veículos (idade do veículo, danos), apólice (premium, canal de fornecimento) etc.


# Objetivos:

1) Produzir um modelo preditivo para classificação de potenciais clientes a firmar seguro de veículo com a companhia.

2) Avaliar o impacto do Canal de Vendas sobre o interesse de clientes e inferir o Canal de Venda que maximiza a probabilidade de clientes adquirirem o seguro de veículos

3) Avaliar a quantidade de pessoas que terão interesse no seguro de veículos após a oferta de desconto no seguro de saúde.

4) Modelar uma função de custo considerando as regras de negócio para selecão do melhor modelo

5) Deploy no StreamLit para consumo do modelo de Machine Learning


# Desafios.

1) Classificação de clientes de seguro de saúde que podem se interessar por seguros de veículos.  

2) Utilização da função de custo como critério de seleção de modelos de Machine Learning, em detrimento das métricas convencionais de acurácia, precisão, revocação, ROC, AUC, F1-score  

3) Simular um ambiente de produção em cloud (DataBricks) integrado a um banco de dados relacional (Azure) para leitura de dados em batch, consumo de modelo de machine learning e escrita de predições no banco de dados.  

4) Lidar com base de dados desbalanceados.  


# Conclusões

- O maior desconto que poderia ser dado para evitar perdar e agarriar mais clientes é de 2.67%.  
-  Mesmo após a oferta de 2% de desconto nenhum cliente da base de clientes sem interesse passaria a ter interesse, sendo, portanto, a oferta de desconto geradora de prejuízos.
- O canal de venda que maximiza a probabilidade do cliente aceitar o seguro é sugerido na API.  
- Ao realizar o comparativo das operações utilizando-se Machine Learning e sem utilizar há um ganho total de 4.3 Mi com a implementação de Machine Learning.  
- Isso equivale a um ganho de 11.36 reais por cliente do seguro de saúde.  


A função de custo elaborada de acordo com as regras de negocio selecionou um modelo que:

-  Acerta 97,76% de clientes interessados (Recall classe 1)  
-  Acerta 58,78% de CLients não interessados (Recall classe 0)  
-  AUC: 0.7827   



# Stack
Numpy, Pandas, Seaborn, Matplotlib, Spark, PySpark, Azure Databricks, PowerBI, Streamlit, Flask.
