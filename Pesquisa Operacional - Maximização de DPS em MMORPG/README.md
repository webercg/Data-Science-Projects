

# Contextualização do problema

Tibia, lançado em 1998, é um dos primeiros MMORPGs que, mesmo após várias atualizações, mantém sua relevância como um dos maiores do gênero até hoje. As constantes melhorias no jogo introduziram uma diversidade de criaturas e locais de caça, cada uma apresentando estatísticas únicas como a vida máxima, fraquezas ou fortalezas á elementos, quantidade de golpes distintos, dano de cada golpe, dano por turno (DPS), além de outras estatísticas calculadas previamente (dado as características do meu personagem) como quantidade de turnos de dano que a criatura deve receber para morrer.

Existem diversas maneiras de aumentar o dano causado pelo personagem, sendo que neste estudo focaremos em duas: as runas elementais (físico, veneno, fogo, morte, sagrado, gelo) e as runas refletoras de dano. As runas podem ser alocada apenas em 1 criatura por runa, e cada criatura, por sua vez pode ter alocada apenas 1 runa.

As runas elementais concedem dano baseado na vida máxima da criatura e a sua chance de ativação é proporcional á quantidade de turnos de dano que ela recebe antes de morrer. Por outro lado a runa refletora de dano concede dano baseado no dano recebido pelo personagem, sua chance de ativação é proporcional á quantidade de turnos de dano que a criatura desfere antes de morrer.

Os locais de caça apresentam uma diversidade de criaturas, e a proporção de sua aparição varia também de acordo com o caminho escolhido pelo jogador para explorar e enfrentá-las repetidamente, buscando pontos de experiência.

O objetivo deste trabalho é responder à seguinte pergunta: dadas as restrições de alocação de runas, as características do local de caça (proporção de aparição de criaturas) e as estatísticas das criaturas, como vida máxima, dano aumentado ou reduzido á elementos, quantidade de golpes deferidos pela criatura, dano dos golpes e quantidade de golpes para derrotar cada criatura, COMO DEVEMOS ALOCAR AS RUNAS E EM QUAIS CRIATURAS ALOCÁ-LAS PARA MAXIMIZAR O DANO ADICIONAL E EXTRAIR O MÁXIMO QUE UM LOCAL DE CAÇA, COMO O DOS ELFOS DE FOGO EM FEYRIST, PODE OFERECER?

# Estatisticas de criatura
vida: Vida maxima da criatura
dano_fisico: Fator de multiplicação de dano físico que a criatura recebe
dano_poison: Fator de multiplicação de dano de veneno que a criatura recebe
dano_fire: Fator de multiplicação de dano de fogo que a criatura recebe
dano_death: Fator de multiplicação de dano de morte que a criatura recebe
dano_energy: Fator de multiplicação de dano de energia que a criatura recebe
dano_holy: Fator de multiplicação de dano sagrado que a criatura recebe
dano_ice: Fator de multiplicação de dano de gelo que a criatura recebe
qtd_golpes_distintos: Quantidade de golpes distintos que a criatura pode deferir em 1 turno

# Estatísticas do local de caça
proporcao_respawn: Proporção de aparição da criatura em número de criaturas dado o caminho da caçada.

# Estatística do personagem
turnos_dano_para_morte: Média do número de turnos de dano a criatura recebe antes de morrer dado as estatisticas do meu personagem (Armas, set, rotação de magia, talentos, skills, encantamentos (imbuements), chance de dano crítico etc)

# Pesquisa Operacional

## Função Objetivo
- ![](image/funcao_objetivo.png)
## Restrição 1: Cada runa deve ter, no máximo, 1 criatura alocada
- ![](image/eq_restricao1.png)
- ![](image/eq_restricao1.1.png)
## Restrição 2: Cada criatura deve ter, no máximo, 1 runa alocada.
- ![](image/eq_restricao1.1.png)
