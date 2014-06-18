Gallerytest - HeyPhoto!
===========

Projeto em Django demonstrando criação de uma galeria de imagens, feito para a equipe da globo.com!


### Como projetei?
Criei um mini projeto em Django tentando usar os padrões, alguns poucos testes de unidade (só pra não passar batido) e um plugin jquery pra ser o ponto chave desse desafio.
O dei o nome de "Robgallery" em homenagem a meu sobrinho, de 13 anos, que me viu programá-lo ontem. (Ele é doido pra aprender. rs)

### Como instalar?
Criei um Makefile pra facilitar a vida.
Fazendo do zero (sem ao menos ter baixado esse repositório), faça:

    git clone https://github.com/joepreludian/gallerytest.git heygallery
    cd heygallery
    make setup
    
Para rodar o projeto web basta fazer:

    make run

Isto fará com que seja levantado um servidor de desenvolvimento prontinho pra trabalhar.
Acesse o endereço <http://127.0.0.1:8000> e tudo certo! =P

### Do que precisamos pra instalar?
Basicamente um sistema xNix com python 2.7, pip e virtualenv instalados.

### Quais tecnologias utilizadas?
Usei as seguintes:

|Tecnologia | Propósito|
|-----------|----------|
|Django | Obviamente pra o suporte do projeto. Optei pela versão estável até agora. (1.6)|
|django-bootstraped-admin | Uma "skin" bonitinha pro painel administrativo do django|
|django-versatileimagefield | Uma classe bastante rápida e prática para se trabalhar com imagens|
|South | Já é costume eu usar migrações no sistema, apesar da versão 1.7 já ter incluída por padrão.|
|Bootstrap | Para um frontend mais bonito [tanto pra vocês quanto pra mim! rs]|
|Bower | Gerenciador de pacotes pra frontend. Apesar de ter colocado o arquivo de configuração, resolvi versionar tudo pra não sofrer o risco de não ter aí.|
|Coffeescript | Para o Robgallery desenvolvi toda a funcionalidade do plugin em Coffescript. Confere lá no static! =P|
|Less | Usei tanto para customizar o bootstrap quanto pra o css do robgallery. Pensei em interpolar com o Sass, mas seria desnecessário.|
|Makefile | Só pra não perder o bom e velho costume. Criado ferramenta pra facilitar nossa vida na hora de iniciar, rodar e limpar o projeto|

### Obrigado
Qualquer coisa *mail me*.
