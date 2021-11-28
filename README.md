# Segundo Trabalho de Programação para Web - INF1407
### Caio Graça Melo - 1621170 
### Fernando Santos - 1710160

Domínio oficial do site: https://trab2-inf1407.herokuapp.com/

## Sobre o site
O site implementado é uma plataforma voltada para usuários que desejam cadastrar seus jogadores favoritos e visualizá-los em uma formato de lista sempre que possível. O sistema também permite atualizar as informações dos jogadores ou até mesmo excluí-los da lista.

## O que foi desenvolvido?
Primeiramente implementamos operações de acesso e criação de conta. Assim, ao efetuar login, cada usuário tem uma visão diferente da página de lista de jogadores.

Em seguida, foi desenvolvido um CRUD no myapp - nossa aplicação dentro do projeto Django - com todas as views e templates necessários para poder gerenciar um banco de dados de jogadores de futebol. Uma instância de jogador no sistema é composta de nome, time, nação e usuário (ex: Neymar, PSG, Brasil, Caio). Nesse caso, usuário representa o usuário que criou o jogador. Um usuário pode visualizar/gerenciar somente jogadores que ele criou.

Além disso, foi desenvolvido um script AJAX na tela de cadastrar um jogador. Esse script faz uma simples requisição GET para buscar a quantidade de jogadores cadastrados no banco de dados.

## Funcionamento do site
Ao entrar no site, o usuário tem a possibilidade de criar uma conta ou fazer login em uma conta já existente. Após efetuar o login com sucesso, o usuário é redirecionado para a homepage do programa.

Acessando a homepage do programa, o usuário tem a opção de ir para a lista de jogadores, onde através das opções para cada jogador (exclusão e atualização) e da barra de opções na parte superior da tela, o usuário pode gerenciar e adicionar novos jogadores ao sistema.

Por fim, temos a opção de sair da conta onde o usuário e deslogado do sistema e redirecionado para a tela inicial.
