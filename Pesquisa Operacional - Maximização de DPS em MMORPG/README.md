

# Contextualização do problema

Tibia, lançado em 1998, é um dos primeiros MMORPGs que, mesmo após várias atualizações, mantém sua relevância como um dos maiores do gênero até hoje. As constantes melhorias no jogo introduziram uma diversidade de criaturas e locais de caça, cada uma apresentando estatísticas únicas como a vida máxima, fraquezas ou fortalezas á elementos, quantidade de golpes distintos, dano de cada golpe, dano por turno (DPS), além de outras estatísticas calculadas previamente (dado as características do meu personagem) como quantidade de turnos de dano que a criatura deve receber para morrer.

Existem diversas maneiras de aumentar o dano causado pelo personagem, sendo que neste estudo focaremos em duas: as runas elementais (físico, veneno, fogo, morte, sagrado, gelo) e as runas refletoras de dano. As runas podem ser alocada apenas em 1 criatura por runa, e cada criatura, por sua vez pode ter alocada apenas 1 runa.

As runas elementais concedem dano baseado na vida máxima da criatura e a sua chance de ativação é proporcional á quantidade de turnos de dano que ela recebe antes de morrer. Por outro lado a runa refletora de dano concede dano baseado no dano recebido pelo personagem, sua chance de ativação é proporcional á quantidade de turnos de dano que a criatura desfere antes de morrer.

Os locais de caça apresentam uma diversidade de criaturas, e a proporção de sua aparição varia também de acordo com o caminho escolhido pelo jogador para explorar e enfrentá-las repetidamente, buscando pontos de experiência.

O objetivo deste trabalho é responder à seguinte pergunta: dadas as restrições de alocação de runas, as características do local de caça (proporção de aparição de criaturas) e as estatísticas das criaturas, como vida máxima, dano aumentado ou reduzido á elementos, quantidade de golpes deferidos pela criatura, dano dos golpes e quantidade de golpes para derrotar cada criatura, 

**Como devemos alocar as runas e em quais criaturas alocá-las para maximizar o dano adicional e extrair o máximo que um local de caça, pode oferecer? (como o dos elfos de fogo em Feyrist).**

# Estatisticas de criatura
- Vida maxima da criatura
- Fraqueza / Resistência contra elemento de dano físico - Fator de multiplicação de dano físico que a criatura recebe
- Fraqueza / Resistência contra elemento de dano de veneno -  Fator de multiplicação de dano de veneno que a criatura recebe
- Fraqueza / Resistência contra elemento de dano de fogo -  Fator de multiplicação de dano de fogo que a criatura recebe
- Fraqueza / Resistência contra elemento de dano de morte - Fator de multiplicação de dano de morte que a criatura recebe
- Fraqueza / Resistência contra elemento de dano de energia - Fator de multiplicação de dano de energia que a criatura recebe
- Fraqueza / Resistência contra elemento de dano sagrado - Fator de multiplicação de dano sagrado que a criatura recebe
- Fraqueza / Resistência contra elemento de dano de gelo - Fator de multiplicação de dano de gelo que a criatura recebe
- Quantidade de golpes distintos que a criatura pode deferir em 1 turno

# Estatísticas do local de caça
- Proporção de aparição da criatura dado o local de caça e o caminho escolhido para repetir.

# Estatística do personagem
- Número de golpes que criatura deve receber para ser derrotada dado as estatisticas do meu personagem (Armas, set, rotação de magia, talentos, skills, encantamentos (imbuements), chance de dano crítico etc) e as estatísticas da criatura (armadura, vida etc)

# Pesquisa Operacional

## Variáveis de decisão
Nesse estudo de caso são 6 criaturas e 8 runas distintas. Serão, portanto, 48 variáveis binárias para indicar se o conjunto [runa,criatura] estará habilitado (1) ou não (0).

## Função Objetivo
A função objetivo escolhida foi a maximização do DPS (dano por segundo) que foi dividida em duas equações. Uma referente as runas de dano elemental e outra referente as runas de dano refletido.
- ![](funcao_objetivo.png)
## Restrição 1: Cada runa deve ter, no máximo, 1 criatura alocada
- ![](eq_restricao1.png)
- ![](eq_restricao1.1.png)
## Restrição 2: Cada criatura deve ter, no máximo, 1 runa alocada.
- ![](eq_restricao1.1.png)
