# PROJETO EM ANDAMENTO

Será desenvolvido os seguintes tópicos:

- Responder a pergunta de negócio: Quais seriam os ganhos financeiros ao identificar os clientes com alta probabilidade de indimplência?
- Tendo em mãos as probabilidades de inadimplência (Logistic Regression / Modelos Arvores): Montar o quadro com dez percentis e avaliar o threshold da probabilidade de operação para aprovação de crédito;
- Tendo em mãos as probabilidades de inadimplência (Logistic Regression / Modelos Arvores): Criar um score de 0 á 1000 de risco de crédito.


# RESULTADOS PARCIAIS

## TESTES DE HIPOTESE A/B - Técnica Bootstrap


H1: A taxa de inadimplência de clientes do sexo Masculino é maior em comparação aos clientes do sexo Feminino - VERDADEIRO
H2: A taxa de inadimplência de clientes que tem apenas o ensino médio completo é maior em comparação aos outros clientes - VERDADEIRO
H3: A taxa de inadimplência de clientes com estado civil "Outros" é maior em comparação aos outros clientes - FALSO
H4: A taxa de inadimplência de clientes com estado civil "Casado" é maior em comparação aos outros clientes - VERDADEIRO
H5: A taxa de inadimplência de clientes que atrasaram a fatura em 2 meses é maior em comparação aos clientes que não atrasaram - VERDADEIRO
H6: A taxa de inadimplência de clientes que pagaram o total da fatura e é maior em comparação aos clientes que pagaram parcialmente - VERDADEIRO


## MODELOS

LGBM  
Recall_0: 0.872030815322063  
Recall_1: 0.5508666164280331  
Acuracia: 0.801  
AUC: 0.7114487158750481  

NEAREST_CENTROID  
Recall_0: 0.8159640487909267  
Recall_1: 0.5772418990203466  
Acuracia: 0.7631666666666667  
AUC: 0.6966029739056365  

LOGISTIC REGRESSION
Recall_0: 0.8159640487909267    
Recall_1: 0.5772418990203466    
Acuracia: 0.7631666666666667    
AUC: 0.6966029739056365    

