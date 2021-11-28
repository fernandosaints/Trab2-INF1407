# Segundo Trabalho de Programação para Web - INF1407
### Caio Graça Melo - 1621170 
### Fernando Santos - 1710160

## O que foi desenvolvido?
Foi desenvolvido um CRUD no myapp - nossa aplicação dentro do projeto Django - com todas as views e templates necessários para poder gerenciar um banco de dados de jogadores de futebol. Uma instância de jogador no sistema é composta de nome, time, nação e usuário (ex: Neymar, PSG, Brasil, Caio). Nesse caso, usuário representa o usuário que criou o jogador. Um usuário pode visualizar/gerenciar somente jogadores que ele criou.

Além disso, foi desenvolvido um script AJAX na tela de cadastrar um jogador. Esse script faz uma simples requisição GET para buscar a quantidade de jogadores cadastrados no banco de dados.

## Funcionamento do site
Ao acessar a página inicial do programa, o usuário tem a opção de ir para a lista de jogadores, onde através das opções para cada jogador (exclusão e atualização) e da barra de opções na parte superior da tela, o usuário pode gerenciar e adicionar novos jogadores ao sistema.
