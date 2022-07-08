import numpy as np
import os
from flask import Flask, request, render_template, make_response
import joblib
import pandas as pd
from PIL import Image

import streamlit.components.v1 as components
import streamlit as st

#model = joblib.load('model.pkl')
model = joblib.load(open(os.path.join('model/model.pkl'),"rb"))


st.set_page_config(page_title="Random Forest", page_icon="🌱")


st.sidebar.image('static/rf team2.png', use_column_width=True )
st.sidebar.title('Menu')
pagSelecionada = st.sidebar.selectbox('Escolha uma seção',['Home','EDA', 'Previsão de vendas', 'Arquitetura do Projeto', 'Premissas, objetivos e desafios', 'Resultados','Equipe e Agradecimentos'])



if pagSelecionada == 'Home':

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col2:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col3:
        img = Image.open("static/rf3 logo.png" ) 
        st.image(img)
    with col4:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col5:
        img = Image.open("static/rf2.png" ) 
        st.image(img)

    st.title("Bem-vindo!")  
      
    st.markdown("Este trabalho foi realizado pelo grupo [Random Forest](https://github.com/Chitolina/RandomForestTeam) do curso de treinamento para cientista de dados [Stack Academy](https://www.youtube.com/c/Stack_tecnologias). Os componentes do grupo são: [Alex Graziani](https://github.com/awildt01), [Bruno Freitas](https://github.com/Freitashbruno), [Lucas Chitolina](https://github.com/Chitolina) e [Weber Godoi](https://github.com/webercg).")
    st.markdown("O tema escolhido para elaboração do projeto foi: [Health Insurance Cross Sell Prediction 🏠 🏥](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction).")
    st.markdown("Do que se trata o projeto?")
    st.markdown("Nosso cliente é uma seguradora que forneceu seguro de saúde para seus clientes, agora eles precisam de sua ajuda na construção de um modelo para prever se os segurados (clientes) do ano passado também terão interesse no seguro de veículos fornecido pela empresa.")
    st.markdown("Construir um modelo para prever se um cliente estaria interessado em seguro de veículo é extremamente útil para a empresa, pois ela pode planejar adequadamente sua estratégia de comunicação para alcançar esses clientes e otimizar seu modelo de negócios e receita. Agora, para prever se o cliente estaria interessado em seguro de veículo, você tem informações sobre dados demográficos (gênero, idade, localização), características do veículos (tempo de uso, danos, habilitação), apólice (valor do seguro de saúde e canal de vendas) etc.")
    st.header("Repositório do Projeto:")
    st.markdown("● [Análise Exploratória](https://github.com/Chitolina/RandomForestTeam/tree/main/EDA)")     
    st.markdown("● [Gerenciamento de Tarefas](https://trello.com/b/Nypkyrp3/randomforest)")
    st.markdown("● Cloud (em desenvolvimento)")      
    st.markdown("● [Modelo Preditivo](https://github.com/Chitolina/RandomForestTeam/blob/main/EDA/Funcao%20de%20Custo%20e%20Selecao%20de%20Modelo.ipynb)")
    st.markdown("● [Dashboard BI](https://github.com/Chitolina/RandomForestTeam/tree/main/BI_RANDOMF)")
    st.markdown("● [Apresentação](https://github.com/webercg/Health-Insurance-Cross-Sell-Prediction)")
    
elif pagSelecionada == 'EDA':
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col2:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col3:
        img = Image.open("static/rf3 logo.png" ) 
        st.image(img)
    with col4:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col5:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    
    st.title("Análise Exploratória dos dados")

    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiOGNmYjk3NGYtMzNkYy00NWU2LWEzMzYtZWExMjkyNjViOGZlIiwidCI6IjNmOGRhZmZlLTY4NzAtNGYzNy05NjdmLWFkMzE4ZGFhNDA4OSJ9&pageName=ReportSection", width=600, height=373.5)

elif pagSelecionada == 'Previsão de vendas':

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col2:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col3:
        img = Image.open("static/rf3 logo.png" ) 
        st.image(img)
    with col4:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col5:
        img = Image.open("static/rf2.png" ) 
        st.image(img)

    st.title("Cross-Selling: Previsão de vendas")
    st.write("Previsão de vendas de seguro veicular a clientes de seguro de saúde")

    ListaRegiao = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    ListaCanais = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 163]
    ListaIdadeVeiculo = ["Menos de 1 ano", "Entre 1 e 2 anos", "Mais de 2 anos"]

    sexo = st.radio(
     "Gênero",
     ('Masculino', 'Feminino'))

    if sexo == 'Masculino':
        sexo = 1
    else:
        sexo = 0

    idade = st.number_input(label = 'Idade', min_value=1, max_value=120)
    ##st.slider(label = 'Idade', min_value=1, max_value=180)

    habilitacao = st.radio(
     "Possui Habilitação?",
     ('Sim', 'Não'))

    if habilitacao == 'Sim':
        habilitacao = 1
    else:
        habilitacao = 0

    regiao = st.selectbox('Região',ListaRegiao)

    assegurado_antes = st.radio(
     "Já é assegurado?",
     ('Sim', 'Não'))

    if assegurado_antes == 'Sim':
        assegurado_antes = 1
    else:
        assegurado_antes = 0

    idade_veiculo = st.selectbox('Tempo de uso do veículo',ListaIdadeVeiculo)

    if idade_veiculo == 'Menos de 1 ano':
        idade_veiculo = 0
    elif idade_veiculo == 'Entre 1 e 2 anos':
        idade_veiculo = 1
    elif idade_veiculo == 'Mais de 2 anos':
        idade_veiculo = 2


    veiculo_danificado = st.radio(
     "Veiculo com Sinistro?",
     ('Sim', 'Não'))   

    if veiculo_danificado == 'Sim':
        veiculo_danificado = 1
    else:
        veiculo_danificado = 0

    valorsegurosaude = st.number_input(label = 'Valor anual do seguro de saúde', min_value=1, max_value=800000)

    canalvenda = st.selectbox('Canal de venda',ListaCanais)

    tempofidelidade = st.number_input(label = 'Tempo de fidelidade (Dias)', min_value=1, max_value=800000)


    verificar = st.button("Verificar")

    if verificar:
        Resumo = []
        teste = [sexo,idade,habilitacao,regiao,assegurado_antes,idade_veiculo,veiculo_danificado,valorsegurosaude,canalvenda,tempofidelidade]
        df_api = pd.DataFrame(np.array([teste]), columns=['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured', 'Vehicle_Age','Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage']) 
        X = df_api
        classe = int(model.predict(X)[0])

        max_proba = 0
        max_canal = 0


        if classe == 1:
            image = Image.open('static/sim.jpg')
            st.image(image)
        else:
            image = Image.open('static/nao.jpg')
            st.image(image)

        st.write("Avaliando outros canais de venda:")
        for i in ListaCanais:

            df_api['Policy_Sales_Channel'] = i
            X = df_api
            prob1 = model.predict_proba(X)[0][1]

            canal_formatado = '{0:.3g}'.format(i)
            prob1_formatado = prob1*100
            prob1_formatado = '{0:.3g}'.format(prob1_formatado)+"%"

            Resumo.append(np.array([canal_formatado,prob1_formatado]))

            if prob1 > max_proba:
                max_proba = prob1
                max_canal = i

        max_proba = max_proba*100
        max_proba = '{0:.3g}'.format(max_proba)+"%"

        df_resumo = pd.DataFrame(np.array(Resumo), columns=['Canal','Probabilidade']) 
        df_resumo.sort_values(by='Probabilidade',ascending=False, inplace = True)
        st.dataframe(df_resumo.style.highlight_max(axis=0))

        strretorno =  "Melhor canal de venda: "+str(max_canal)+"; Probabilidade: "+str(max_proba)
        stringretorno = str(strretorno)
        st.write(strretorno)

elif pagSelecionada == 'Arquitetura do Projeto':

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col2:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col3:
        img = Image.open("static/rf3 logo.png" ) 
        st.image(img)
    with col4:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col5:
        img = Image.open("static/rf2.png" ) 
        st.image(img)


    st.title("Arquitetura do Projeto")
    
    st.markdown('Para a nosssa engenharia de dados obtemos uma solução em cloud com o Databricks que nos deu a oportunidade de trabalhar com uma technologia basseada em Apache Spark.')
    st.markdown('A organização e o processo das datas (Data Lake) foi feita no Databricks.')
    img = Image.open("Roadmap2.jpg" ) 
    st.image(img)



elif pagSelecionada == 'Premissas, objetivos e desafios':

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col2:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col3:
        img = Image.open("static/rf3 logo.png" ) 
        st.image(img)
    with col4:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col5:
        img = Image.open("static/rf2.png" ) 
        st.image(img)

    st.title("Premissas, objetivos e desafios")
    
    st.write('O principal desafio consiste em construir um modelo de previsão dos segurados que teriam interrese em Seguro de Veículos.')  
    st.write('Nosso cliente é uma Seguradora que fornece seguro de saúde para seus clientes e que pretende no futuro fornecer também seguro de veículos.')
   
    st.header('Premissas:')
    st.write('- Erros de classificação de pessoas interessadas no seguro de veículo possuem custo superior a classificação errônea de pessoas não interessadas.')
    st.write('- As variáveis que são manipuláveis pelo negócio são: Canal de Venda e Valor anual do seguro de saúde.')

    st.header('Objetivos:')
    st.write('- Avaliar o impacto do Canal de Vendas sobre o interesse de clientes e inferir o Canal de Venda que maximiza a probabilidade de clientes adquirirem o seguro de veículos')
    st.write('- Avaliar quantas pessoas terão interesse no seguro de veículos após a oferta de 10% de desconto no seguro de saúde.')
    st.write('- Simular um ambiente de produção em cloud integrado com data-lake, banco de dados relacionais, leitura de dados em batch e consumo de modelo de machine learning.')

    st.header('Desafios Superados:')
    st.write('- Elaboração de função de custo personalizada ao negócio')
    st.write('- Utilização da função de custo como critério de seleção de modelos de Machine Learning, em detrimento das métricas convencionais de acurácia, precisão, revocação, ROC, AUC, F1-score')
    st.write('- Lidar com base de dados desbalanceados. Para treinamento de modelos de classificação foram testados técnicas de amostragem estratificada, undersampling com variação da proporção de exemplos de classe minoritária sobre os dados de treino, oversampling (SMOTE), e variação de class_weights como forma de aumentar a penalização de erros de classes minoritárias')
    st.write('- Desenvolvimento de APIs em StreamLit e prototipação em Flask (Disponivel no repositório do github)')
 

    img = Image.open("static/kisspng2.jpg" ) 
    st.image(img)


if pagSelecionada == 'Resultados':

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col2:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col3:
        img = Image.open("static/rf3 logo.png" ) 
        st.image(img)
    with col4:
        img = Image.open("static/rf2.png" ) 
        st.image(img)
    with col5:
        img = Image.open("static/rf2.png" ) 
        st.image(img)

    st.title("Resultados") 

    st.markdown("A implementação do modelo de Machine Learning:")

    st.markdown("● Aumenta as receitas de entre  +1,39 mi (reais) á +R$8,71 mi (reais);")
    st.markdown("● Entre os clientes sem interesse há uma taxa de conversão +10,75% (35.942 pessoas) após a oferta de desconto de 10% sobre o seguro de saúde. É possível, dessa forma, aumentar a quantidade de pessoas interessadas em +76,9% e aumentar a receita em +R$26,23 mi;")

    st.markdown("Performance e Resultados:")
    st.markdown("● O Modelo acerta 97,54% dos clientes interessados;")     
    st.markdown("● A probabilidade do cliente ter interesse dado que o modelo a classificou como interessada é de 29,41%")
    st.markdown("● O canal de venda que maximiza a probabilidade do cliente aceitar o seguro é sugerido na API.")      



elif pagSelecionada == 'Equipe e Agradecimentos':
    st.title("Equipe e Agradecimentos")

    col1, col2, col3 = st.columns(3)

    with col1:
        img = Image.open("static/AG.png" ) 
        st.image(img)
        st.write('')
        img = Image.open("static/BF.png" ) 
        st.image(img) 
        st.write('')
        img = Image.open("static/LC.png" ) 
        st.image(img)
        st.write('')
        img = Image.open("static/WG.png" ) 
        st.image(img)    


    with col2:

        st.markdown("**Alexandre Graziani Wildt**")
        st.write('Data Scientist')
        st.markdown('[LinkedIn](https://www.linkedin.com/in/alexandre-wildt-graziani-73638b15a/?originalSubdomain=de)')
        
        st.write('')

        st.markdown("**Bruno Freitas**")
        st.write('Data Scientist')
        st.markdown('[LinkedIn](https://www.linkedin.com/in/bruno-hfreitas/)')

        #st.write('')

        st.markdown("**Lucas Chitolina**")
        st.write('Data Scientist | Data Analytics ')
        st.markdown('[LinkedIn](https://www.linkedin.com/in/lucas-chitolina/)')

        st.write('')

        st.markdown("**Weber Godoi**")
        st.write('Data Scientist | Chem Engineer')
        st.markdown('[LinkedIn](https://www.linkedin.com/in/webergodoi/)')