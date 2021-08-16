Atenção: se você é participante do estudo, baixe a [versão executável](https://github.com/NatanaelAntonioli/Randonautica-Organizada-e-Lastreada-na-Aleatoriedade/releases/tag/v1.0-exe) e leia atentamente o conteúdo das seções abaixo. A seção de perguntas frequentes é a única cuja leitura pode ser dispensada.
## O que é Randonautica Organizada e Lastreada na Aleatoriedade? ##

[Randonautica](https://www.randonautica.com) é um aplicativo cuja proposta é levar o jogador a lugares inesperados nas redondezas através de coordenadas aleatórias geradas enquanto o usuário mentaliza um objetivo. As coordenadas são geradas através de um método quântico, e muitos apontam que o aplicativo possui alguma natureza subjacente, uma vez que as coordenadas indicadas muitas vezes carregam algum significado para o usuário. Assim, supõe-se que mentalizar um objetivo influencia na geração de números aleatórios quânticos. 

**R**andonautica **O**rganizada e **L**astreada na **A**leatoriedade (sim, nós pensamos no nome após decidir a sigla) é um programa em Python que visa testar a hipótese "a impressão de que as coordenadas possuem significado se devem ao viés de confirmação" através de uma abordagem controlada, na qual cada geração de coordenadas pode produzir uma coordenada verdadeiramente aleatória e quântica (tal como no aplicativo original) ou produzir uma coordenada pseudoaleatória, gerada a partir da data do sistema momentos antes do usuário ter mentalizado seu objetivo. 

O programa é feito de forma que o usuário só descobre a verdadeira natureza do local que visitou após ter dado seu veredito a respeito dele. Assim, é possível checar se a fração de lugares que carregam algum significado para o usuário é ou não diferente entre coordenadas verdadeiramente aleatórias geradas durante a mentalização e coordenadas pseudoaleatórias geradas antes dela. Esse programa será usado no estudo a esse respeito conduzido pelo canal Fábrica de Noobs.

## Como jogar? ##

Para jogar, basta iniciar o programa através do arquivo executável. É fundamental que o arquivo de chave pública, `public_key.pem`, esteja na mesma pasta que o executável. É possível que haja alguma demora (cerca de 30 segundos a 1 minuto) para carregar o programa. Aguarde até que informações sejam exibidas na tela.

Iniciar o programa através do executável permitirá que você escolha entre três opções de jogo: *jogo usual*, na qual você saberá a natureza da coordenada assim que a avaliar, *participar do estudo*, na qual você deverá enviar um arquivo criptografado com chave pública assimétrica (gerado automaticamente) para o Natanael, e só após o final de sua participação descobrirá a natureza das coordenadas que visitou, e *administrador*, na qual todas as coordenadas são exibidas imediatamente para fins de teste do programa.


Ao escolher uma opção, o programa irá lhe solicitar uma coordenada central, que deve ser obrigatoriamente informada na forma decimal. Para facilmente obter uma coordenada de qualquer local, basta acessá-lo no Google Maps, clicar com o botão direito sobre o ponto desejado e então clicar com o botão esquerdo sobre o número que aparecerá no topo do menu. Você pode, então, colar a coordenada obtida na linha de comando. Um raio em metros será então solicitado. Recomendamos valores entre 1000 (1 quilômetro) e 10000 (10 quilômetros), já que valores acima disso podem tornar a geração lenta.

    O que deseja fazer? 1
    Insira as coordenadas, na forma decimal, com ponto de separador: -23.56116158718288, -46.65597786087111
    Insira o raio em metros: 2000

![](https://i.imgur.com/bdjhMd2.png)

Em seguida, você será confrontado com quatro possibilidades de locais, todas elas que fazem parte da experiência original do aplicativo Randonautica e que - assim como no aplicativo - são geradas de forma verdadeiramente aleatória, aqui através de um [gerador de números aleatórios quânticos com flutuações no vácuo](https://qrng.anu.edu.au/) e, no aplicativo, a partir da chegada de fótons na câmera do celular. 

- Um *ponto cego* é um único ponto aleatório gerado no raio em questão.

Os demais pontos dependem da geração de um número grande (na casa dos milhares) de pontos dentro do raio.

- Um *atrator* é um ponto que possui muitos outros pontos em sua vizinhança próxima.
- Um *vazio* é um ponto que possui poucos ou nenhum ponto em sua vizinhança próxima.
- Uma *anomalia* pode ser ou um atrator ou um vazio, dependendo de qual desviar-se mais da média de vizinhos.

Escolher uma das opções define o tipo de local nessa rodada, e será possível escolher outros tipos de locais posteriormente.

	------------------------------- Escolha agora o tipo de local: -------------------------------
	1 - Ponto cego: um ponto aleatório.
	2 - Atrator: um local em que muitos pontos aleatórios aparecem.
	3 - Vazio: um local em que poucos ou nenhum ponto aleatório aparece.
	4 - Anomalia: um atrator ou um vazio, dependendo do que for mais forte.
	5 - Sair.
	Para onde deseja ir? 2

Há ainda um quinto tipo, denominado *ponto de controle*. Esse é um ponto gerado de forma pseudoaleatória (a partir do tempo do sistema operacional), que não possui qualquer ligação com o que o usuário mentalizou, uma vez que 100 destes pontos são gerados no momento em que a coordenada foi primeiro informada, e cada considera, de forma sequencial, o próximo ponto dessa lista.

Ao escolher a opção, o programa decide se você receberá uma coordenada verdadeiramente aleatória (conforme pediu) ou se receberá simplesmente um ponto de controle. Porém, você não saberá qual foi a decisão tomada, e será convidado a mentalizar seu objetivo da mesma forma que faria no aplicativo original.

	Preparando... mentalize seu objetivo (485/1757).
	Preparando... mentalize seu objetivo (486/1757).
	Preparando... mentalize seu objetivo (487/1757).
	Preparando... mentalize seu objetivo (488/1757).
	Preparando... mentalize seu objetivo (489/1757).
	Preparando... mentalize seu objetivo (490/1757).
	Preparando... mentalize seu objetivo (491/1757).
	Preparando... mentalize seu objetivo (492/1757).

Após o carregamento (que tipicamente leva entre alguns segundos e 2 minutos), o local será definido e você será informado de suas coordenadas na tela. Para o caso em que você pretenda ir presencialmente no lugar, decida se quer ou não visitá-lo, e lembre-se que você pode desistir disso (e gerar um novo local) a qualquer momento sem comprometer os resultados de sua participação no estudo.

	---------------------------------- Local definido (atrator) ----------------------------------
	Lembre-se: a decisão de visitar o local é sua. Julgue, com bom senso, se isso é seguro.
	A coordenada selecionada é: -23.54606539102067, -46.65498352539448
	1 - Visitei (virtualmente ou pessoalmente) o local e estou pronto para reportá-lo.
	2 - Desisti de visitar o local e irei descartá-lo.
	Informe quando estiver pronto: 1

Não feche o programa até o momento em que você visitar o local (ou desistir dele), uma vez que isso fará com que seu progresso para esse local seja perdido. Quando estiver pronto, informe a linha de comando, e você será então convidado a avaliar se o local possuía ou não algum significado para você.

	------------------------------------------ Veredito ------------------------------------------
	O que você achou do local visitado?
	1 - De alguma forma, o local foi relevante para mim.
	2 - O local não  significou nada para mim.
	Informe seu veredito: 

É difícil dizer precisamente o que "possuir algum significado" compreende, mas usuários de Randonautica frequentemente usam os seguintes critérios:

- O local possui alguma relação com o que você mentalizou . Para alguns, uma relação mesmo que remota já é suficiente.
- Você escolheu um vazio, e foi enviado para um local que dificilmente visitaria de outra forma, ou foi enviado para o meio do mato.
- Você escolheu um atrator, e foi enviado para um local que possui algum significado na sua rotina (por exemplo, um ponto em que frequentemente transita) ou para sua história (por exemplo, uma escola em que estudou).
- Os mesmos critérios acima para vazio e atrator, mas vice-versa.
- O local possui algum tipo de elemento peculiar (um grafite ou pichação, uma pessoa curiosa, um animal inesperado, um imóvel abandonado, uma pareidolia, uma vista bonita, um artefato inesperado, etc.).

Se você optou por um jogo usual, que é a forma pretendia de se usar o programa caso você não esteja participando do estudo conduzido no momento, você imediatamente descobrirá a verdadeira natureza da localização, que pode ser atrelada com o que mentalizou (e verdadeiramente aleatória) ou desatrelada com o que mentalizou (e apenas pseudoaleatória gerada a partir da lista).

	----------------------------------------- Resultados -----------------------------------------
	Voce disse que o local foi relevante para voce.
	Voce apenas visitou uma coordenada desatrelada com o que mentalizou (atrator).

## O que mais preciso fazer participando do estudo? ##


Os passos acima são válidos, até o veredito, também para quem participa do estudo. Porém, participantes do estudo não podem saber a verdadeira natureza da coordenada visitada até que sua participação no estudo esteja terminada. Essa é uma forma de garantir que a sua decisão de enviar ou não o resultado não seja influenciada por ele (por exemplo, enviar apenas resultados que você julgou o local relevante) e que você não seja influenciado por resultados anteriores (por exemplo, deduzir que o próximo local deve ser pseudoaleatório porque os últimos 3 foram verdadeiramente aleatórios). 

Sendo assim, dar seu veredito produzirá um arquivo criptografado com [chave assimétrica](https://en.wikipedia.org/wiki/Public-key_cryptography) que contém as informações presentes no último bloco de código: qual foi seu veredito e o que a coordenada visitada realmente era, além de uma sequência de 30 letras e números pseudoaleatórios que serve para tornar o processo de reverter a *hash* obtida mais difícil. **O arquivo não contém a localização visitada, a localização central, o raio, ou qualquer outra informação que permita lhe identificar**.

Além disso, você receberá uma *hash* em [*MD5*](https://en.wikipedia.org/wiki/MD5) da mensagem enviada, cujo uso abordaremos mais adiante.

O arquivo será gerado com extensão *.encry* na pasta onde o executável e a chave pública estão, e ele possui um nome dependente unicamente do dia, mês, ano, hora, minuto e segundo de sua geração. Você deve enviá-lo, da forma que preferir (Discord, *e-mail*, Facebook, Twitter, *upload* na nuvem, etc.), para o Natanael. Não é necessário incluir qualquer outra informação, já que o arquivo contém todas as informações necessárias.

	----------------------------------------- Resultados -----------------------------------------
	Como informado, você só poderá descobrir a natureza do local  ao final do estudo quando a chave 
	privada for publicada. Até lá, envia o arquivo para o Natanael. Ela não contém qualquer
	informação que lhe permite identificá-lo, como dados do dispositivo ou as coordenadas,
	 mas sim apenas o tipo de local (ponto cego, atrator, vazio, anomalia), o seu veredito
	e a sua natureza.
	
	Para submeter os resultados do estudo, envie o arquivo 130821183313.encry para o Natanael.
	Use a hash MD5 abaixo para, após decifrada, conferir a integridade da mensagem enviada:
	
	d77577ae84aa6f4068ac5c0cd4582f84

![](https://i.imgur.com/y0aeM7C.png)

Uma vez enviado os arquivos, comunique o Natanael quando deseja encerrar sua participação no estudo. Ao encerrar sua participação na série do estudo, arquivos que você enviar posteriormente não serão mais considerados a menos que um novo estudo seja iniciado. 

Quando você encerrar sua participação, o Natanael irá lhe devolver um relatório com a tradução de cada arquivo que você enviou, ao lado da *hash* calculada. Se você fez alguma jogada cujo resultado gostaria de conhecer, anote a hash devolvida, assim você pode localizá-la no relatório. A hash também permite que você confira a integridade da mensagem contida no arquivo.

	--------------------------------------------------130821183313.encry--------------------------------------------------
	HASH: d77577ae84aa6f4068ac5c0cd4582f84
	Voce disse que o local nao significou nada para voce. Voce apenas visitou uma coordenada desatrelada com o que mentalizou (atrator). SALT: KDLLDF42BG1BN4C77EYIY4I9M0SE5I
	--------------------------------------------------130821193702.encry--------------------------------------------------
	HASH: 18fc397eabe87373902ff23d0a37f1b0
	Voce disse que o local foi relevante para voce. Voce visitou uma coordenada atrelada com o que mentalizou (vazio). SALT: OR3NJWXB15YIE5AKM2KXZ8CQK0VXHM
	--------------------------------------------------130821193728.encry--------------------------------------------------
	HASH: 510c436368d5abbd66d1f86ac0cc0a41
	Voce disse que o local nao significou nada para voce. Voce visitou uma coordenada atrelada com o que mentalizou (anomalia atrator). SALT: 2TH84JRQD925P8PK6QY28TCDPXTUGM
	--------------------------------------------------130821193741.encry--------------------------------------------------
	HASH: dcda7a7a37723671f3371546b64b649e
	Voce disse que o local foi relevante para voce. Voce apenas visitou uma coordenada desatrelada com o que mentalizou (ponto cego). SALT: AAZHTL99DCCYWESMM9HELC5YDSDKAN



## Perguntas técnicas ##

### Quais garantias tenho a usar o programa? ###

O programa não possui qualquer afiliação com o aplicativo Randonautica ou seus desenvolvedores e está sob a [licença MIT](https://choosealicense.com/licenses/mit/), o que significa que (como [ocorre ](https://choosealicense.com/appendix/) na maioria das demais licenças de código aberto) ele não possui com qualquer garantia de funcionamento e que não nos responsabilizamos por nada decorrente de seu uso.

Entretanto, não temos razões para imaginar que seu uso acarretará em problemas para o computador, uma vez que as operações não envolvem acessos de baixo nível em regiões críticas ou cálculos dispendiosos. 

O programa é provavelmente adequado para funcionar em conexões franquiadas, uma vez que cada requisição de números aleatórios pesa 256 bytes, e portanto a geração de 26000 coordenadas (uma jogada com raio de 10 quilômetros) baixa apenas 13 kilobytes.

Da mesma forma que um fabricante de dados não se responsabiliza caso você os use para apostar toda sua fortuna, é evidente que não nos responsabilizamos por qualquer ocorrência ao visitar as coordenadas sugeridas pelo programa. O programa é, em última instância, apenas uma ferramenta que sorteia localizações em um raio, e não é capaz de determinar se uma visita é ou não segura, muito menos saber o que você irá encontrar no local.  

### Quais informações são enviadas para a internet? ###

Apenas uma requisição à [API](https://qrng.anu.edu.au/contact/api-documentation/) do gerador de números aleatórios quânticos da *Australian National University* para obter 1000 números aleatórios quânticos.

### Quais informações estão presentes no arquivo encriptado? ###

O arquivo encriptado contém apenas seu veredito, a natureza da coordenada e uma sequência aleatória que dificulta a reversão da *hash*. Não há qualquer informação pessoal. Abaixo, há um exemplo de arquivo encriptado.

	Voce disse que o local nao significou nada para voce. Voce apenas visitou uma coordenada desatrelada com o que mentalizou (atrator). SALT: KDLLDF42BG1BN4C77EYIY4I9M0SE5I

### Quais informações são lidas pelo programa? ###

Apenas a requisição feita na internet pelos números aleatórios, os valores inseridos, a data e hora do sistema e o arquivo `public_key.pem` presente no diretório do executável. 

### Quais informações farão parte do estudo e serão publicadas? ###

Todos os arquivos encriptados serão publicados, junto com a chave pública, logo todo o conteúdo de todos os arquivos encriptados será disponibilizado. Essas são as únicas informações que serão publicadas e que farão parte do estudo, a partir das quais as conclusões serão obtidas. 

### Quais os requisitos para rodar o código fonte do programa? ###

Python 3, além das bibliotecas presentes no cabeçalho.

	import random
	from datetime import datetime
	import numpy as np	
	import math
	from math import sin, cos, sqrt, atan2, radians	
	# import matplotlib.pyplot as plt # <MATPLOTLIB>	
	import scipy.spatial as spatial
	import numpy	
	import requests	
	import string	
	from cryptography.hazmat.primitives import serialization
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import hashes
	from cryptography.hazmat.primitives.asymmetric import padding
	import hashlib

### Como posso auditar o programa? ###

O programa é de código aberto, então um bom começo é a análise do código fonte presente neste repositório. Você também pode usar o modo de jogo *administrador* para verificar todas as coordenadas geradas.

	------------------------------------ Resultados da jogada ------------------------------------
	A coordenada de controle é:   -23.56092589546892, -46.64914573806245
	A coordenada de ponto cego é: -23.56654595290915, -46.65835338711839
	A coordenada do atrator é:    -23.57398247600342, -46.64698985086333
	A coordenada do vazio é:      -23.55097269694057, -46.65280478781868
	A coordenada da anomalia é:   -23.57398247600342, -46.64698985086333 e ela é um atrator.
	
	---------------------------------------- Nova Jogada! ----------------------------------------
	Deseja gerar nova jogada? 
	1 - Sim.
	2 - Não.
	Insira sua resposta: 
	 
Originalmente, o programa também desenhava os pontos em um gráfico. Porém, removemos essa função porque isso requer a biblioteca [matplotlib](https://matplotlib.org), que não funciona como deveria quanto exportamos o executável. Você ainda pode gerar o gráfico removendo todas as marcações de comentários à esquerda das linhas que terminam em `# <MATPLOTLIB>`.

No gráfico, pontos em vermelho são pontos válidos dentro do raio, pontos em cinza são pontos fora do raio (até 1,3 do raio) mas que são usados no cálculo de vizinhos, o ponto azul é o atrator, o ponto magenta é o vazio, o ponto ciano é o ponto cego e o ponto verde é o ponto de controle. O centro é um quadrado petro

![](https://i.imgur.com/kL716se.png)

### Como as coordenadas são geradas a partir dos números aleatórios? ###

A geração de números pseudoaleatórios entre 0 e 1 é feita com a biblioteca [random()](https://docs.python.org/3/library/random.html). 

Já a geração de números verdadeiramente aleatórios entre 0 e 1 e feita fazendo-se uma requisição de 1000 números entre 0 e 65535 para a [API](https://qrng.anu.edu.au/contact/api-documentation/) do gerador de números aleatórios quânticos da *Australian National University*. O valor recebido é então dividido por 65535. Uma nova requisição é feita toda vez que os 1000 números obtidos se esgotam, e isso ocorre a cada 500 coordenadas.  

### Como cada coordenada é gerada? ###

As coordenadas de controle são geradas quando a coordenada central é informada, de maneira sequencial, com coordenadas pseudoaleatórias. A coordenada de ponto cego é gerada produzindo-se uma única coordenada verdadeiramente aleatória.

Então, geramos um número grande de coordenadas verdadeiramente aleatórias e as distribuímos no mapa. Os pontos cuja distância ao centro é maior que o raio inserido são marcados em preto, e os cuja distância é menor são marcados em vermelho. O total de pontos é baseado em uma afirmação que colocava o máximo de pontos em 26000 para o raio máximo (que é de 10 quilômetros), e muda proporcionalmente à área do círculo.

Esses números são a base para a geração de coordenadas geográficas através de um sistema de coordenadas polares, que garante que todo ponto dentro da região tenha igual chance de ser selecionado.

Finalmente, computamos o número de vizinhos de cada ponto usando uma [árvore k-d](https://pt.wikipedia.org/wiki/%C3%81rvore_k-d). Calculamos então o ponto com mais e menos vizinhos em um raio de 111 metros, que satisfaça a condição de distar do centro menos que o raio informado. Assim, se o ponto com mais (ou menos) vizinhos estiver na região cinza, ele é descartado. Isso é especialmente útil para evitar que um ponto com menos vizinhos seja escolhido na borda, onde  trivialmente não há pontos em parte da região.


### Porque você não usou orientação a objetos? ###

Porque lidar com a coordenada como um objeto pode impactar a performance. Mas cá entre nós, eu esqueci que orientação a objetos existia até ser tarde demais.

