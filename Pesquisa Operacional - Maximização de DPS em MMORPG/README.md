## Contextualização do problema

Tibia, lançado em 1998, é um dos primeiros MMORPGs que, mesmo após várias atualizações, mantém sua relevância como um dos maiores do gênero até hoje. As constantes melhorias no jogo introduziram uma diversidade de criaturas e locais de caça, cada uma apresentando estatísticas únicas como a vida máxima, fraquezas ou fortalezas á elementos, quantidade de golpes distintos, dano de cada golpe, dano por turno (DPS), além de outras estatísticas calculadas previamente (dado as características do meu personagem) como quantidade de turnos de dano que a criatura deve receber para morrer.

Existem diversas maneiras de aumentar o dano causado pelo personagem, sendo que neste estudo focaremos em duas: as runas elementais (físico, veneno, fogo, morte, sagrado, gelo) e as runas refletoras de dano. As runas podem ser alocada apenas em 1 criatura por runa, e cada criatura, por sua vez pode ter alocada apenas 1 runa.

As runas elementais concedem dano baseado na vida máxima da criatura e a sua chance de ativação é proporcional á quantidade de turnos de dano que ela recebe antes de morrer. Por outro lado a runa refletora de dano concede dano baseado no dano recebido pelo personagem, sua chance de ativação é proporcional á quantidade de turnos de dano que a criatura desfere antes de morrer.

Os locais de caça apresentam uma diversidade de criaturas, e a proporção de sua aparição varia também de acordo com o caminho escolhido pelo jogador para explorar e enfrentá-las repetidamente, buscando pontos de experiência.

O objetivo deste trabalho é responder à seguinte pergunta: dadas as restrições de alocação de runas, as características do local de caça (proporção de aparição de criaturas) e as estatísticas das criaturas, como vida máxima, dano aumentado ou reduzido á elementos, quantidade de golpes deferidos pela criatura, dano dos golpes e quantidade de golpes para derrotar cada criatura, COMO DEVEMOS ALOCAR AS RUNAS E EM QUAIS CRIATURAS ALOCÁ-LAS PARA MAXIMIZAR O DANO ADICIONAL E EXTRAIR O MÁXIMO QUE UM LOCAL DE CAÇA, COMO O DOS ELFOS DE FOGO EM FEYRIST, PODE OFERECER?

