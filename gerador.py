import random
from random import randrange
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


# As seguintes marcas testam em animais (eu fui o animal):
# numpy, matplotlib, PyCharm, Crypto


# ------------------- MENUS ---------------------------

def menu_principal_func():
    print("----------------------------------------- Bem vindo! -----------------------------------------")
    print("    .--.")
    print(" _,-o   \              R-ANDONAUTICA")
    print("~ --.  , `--__	       O-RGANIZADA E")
    print("      \`-_____~-_pb_   L-ASTREADA NA")
    print("       `/~\--~~~~~--'  A-LEATORIEDADE")
    print("       ^   ^")
    print("1 - Jogo usual: você recebe um local, e descobre sua verdadeira natureza depois.")
    print("2 - Participar do estudo: você recebe um local, submete as informações e descobre sua natureza depois.")
    print("3 - Administrador: você recebe todos os locais e descobre sua natureza no mesmo momento.")
    print("4 - Sair.")
    menu_principal = str(input("O que deseja fazer? "))

    while menu_principal != "1" and menu_principal != "2" and menu_principal != "3" and menu_principal != "4":
        menu_principal = str(input("Insira um valor válido: "))

    if menu_principal == "4":
        quit()
    else:
        return int(menu_principal)


def menu_tipo_local_func():
    print("")
    print("------------------------------- Escolha agora o tipo de local: -------------------------------")
    print("1 - Ponto cego: um ponto aleatório.")
    print("2 - Atrator: um local em que muitos pontos aleatórios aparecem.")
    print("3 - Vazio: um local em que poucos ou nenhum ponto aleatório aparece.")
    print("4 - Anomalia: um atrator ou um vazio, dependendo do que for mais forte.")
    print("5 - Sair.")
    menu_tipo_local = str(input("Para onde deseja ir? "))

    while menu_tipo_local != "1" and menu_tipo_local != "2" and menu_tipo_local != "3" and menu_tipo_local != "4" and menu_tipo_local != "5":
        menu_tipo_local = str(input("Insira um valor válido: "))

    if menu_tipo_local == "5":
        quit()
    else:
        return int(menu_tipo_local)


# ---------------- CONVERSÃO DA COORDENADA --------------------
# Essa função recebe uma coordenada na forma de string
# e retorna a latitude ou longitude da coordenada.
def get_compon(tipo, texto):
    if tipo == 'lat':
        return texto.partition(",")[0]
    if tipo == 'lon':
        return texto.partition(",")[2].replace(' ', '')


# ---------------- PRODUÇÃO DE COORDENADA ALEATÓRIA ------------
# Essa função produz uma coordenada aleatória dentro do raio radius.
# x0 e y0 são as coordenadas do centro.
# u e v são números aleatórios entre 0 e 1.
def produce_random_coord(x0, y0, u, v, radius):
    radiusInDegrees = radius / 111000
    w = radiusInDegrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    foundLatitude = x + x0
    foundLongitude = y + y0

    return str(foundLatitude)[0:18] + ", " + str(foundLongitude)[0:18]


# ---------------- PRODUÇÃO DE NÚMERO ALEATÓRIO ------------
# Essa função produz um número aleatório pseudo ou verdadeiro.
# tipo pode ser pse ou quant.
# contador é o contador global utilizado.

def get_aleatorio(tipo):
    global contador
    global vetor_rand
    if tipo == 'pse':
        return random.random()
    if tipo == 'quant':
        if contador == 999 or contador == 0:
            response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint16")
            jsonRes = response.json()
            vetor_rand = (jsonRes['data'])
            contador = 1
        num = vetor_rand[contador]
        contador = contador + 1
        return num / 65535


# -------------- GERAÇÃO DA COORDENADA --------------------------

def get_coord(x0, y0, radius, tipo_geracao):
    # Caso em que a geração seja pseudoaleatória (grupo de controle, qualquer tipo de localização)
    if tipo_geracao == 1:
        u = get_aleatorio('pse')
        v = get_aleatorio('pse')

    # Caso em que a geração seja quântica.
    elif tipo_geracao == 2:
        u = get_aleatorio('quant')
        v = get_aleatorio('quant')

    return produce_random_coord(x0, y0, u, v, radius)


def get_max_min(tipo, espaco, teto_ou_piso):
    if tipo == 'min':
        retornar = 99999999
        for x in np.nditer(espaco):
            if teto_ou_piso < x < retornar:
                retornar = x

    else:
        retornar = 0
        for x in np.nditer(espaco):
            if retornar < x < teto_ou_piso:
                retornar = x

    return retornar


def get_distancia(lat1, lon1, lat2, lon2):
    R = 6373.0

    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1000

    return distance


# ---------------------------------------- CÓDIGO PRINCIPAL ---------------------------------------

# Inicializar contadores e constantes

contador = 0
factor = 1.3

# Incializar chaves RSA

with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Pedir o tipo de jogo a ser feito.

MENU_principal = menu_principal_func()

# Precisamos, então, das coordenadas e do raio.

coord_confirmed = 2

while coord_confirmed != 1:

    while True:
        coord_text = input("Insira as coordenadas, na forma decimal, com ponto de separador: ")

        try:
            # Tentamos processar os valores da coordenada
            x0 = get_compon('lat', coord_text)
            y0 = get_compon('lon', coord_text)
            x0 = float(x0)
            y0 = float(y0)
            coord_confirmed = 1
            break

        except:
            print("O valor inserido não parece uma coordenada.")

    raio = "not int"
    while not (isinstance(raio, int)):
        raio = str(input("Insira o raio em metros: "))
        try:
            raio = int(raio)
        except:
            pass

    print("")


# Gerar uma lista de coordenadas pseudoaleatórias, que serão usadas uma a uma quando solicitado.
# Isso garante que as coordenadas pseudoaleatórias são totalmente desatreladas da mentalização do usuário,
# e fornecidas de forma sequencial.

list_pseudo = numpy.empty(shape=(1, 2))
contador_pseudo = 1
for i in range(100):
    pseudo_position = get_coord(x0, y0, raio, 1)
    pseudo_x0 = get_compon('lat', pseudo_position)
    pseudo_y0 = get_compon('lon', pseudo_position)
    list_pseudo = np.append(list_pseudo, [[pseudo_x0, pseudo_y0]], axis=0)

# Pedir o tipo de local a ser visitado e decidir o tipo de geração para cada caso.
MENU_tipo_local = "20"

while MENU_tipo_local != 5:

    # fig = plt.gcf() # <MATPLOTLIB>
    # ax = fig.gca() # <MATPLOTLIB>
    # plt.xlabel('Longitude') # <MATPLOTLIB>
    # plt.ylabel('Latitude') # <MATPLOTLIB>
    # plt.axis('equal') # <MATPLOTLIB>
    # ax = fig.gca() # <MATPLOTLIB>
    # markers = 1 # <MATPLOTLIB>

    if MENU_principal == 3:
        print("")
        print("---------------------------------------- Nova Jogada! ----------------------------------------")
        print("Deseja gerar nova jogada? ")
        print("1 - Sim.")
        print("2 - Não.")
        Prosseguir = str(input("Insira sua resposta: "))

        if Prosseguir == "2":
            MENU_tipo_local = 5
            quit()

    else:
        MENU_tipo_local = menu_tipo_local_func()
        MENU_tipo_local = int(MENU_tipo_local)

    # Determinar como o local vai ser gerado, seja por input ou por aleatoriedade.

    # 1 = geração verdadeiramente aleatória.
    # 2 = geração pseudoaleatória. Sempre devolve um ponto aleatório no espaço gerado unicamente.
    MENU_tipo_geracao = random.randint(1, 2)

    # --------------- ESSE É O LOOP DE PRODUÇÃO DE LOCAL. REPETIDO EM TODA GERAÇÃO --------------------
    # Nem tudo precisa ser repetido em toda circunstância. Porém, o usuário não pode perceber
    # qualquer diferença (tempo, uso de CPU, etc) entre geração pseudoaleatória e aleatória.
    # por isso, geramos tudo em todos os casos, e depois encaminhamos a coordenada correta
    # de acordo com as configurações dessa jogada.

    # 1) Obtém a coordenada pseudoaleatória (ela já foi gerada antes), para qualquer circunstância do grupo de controle.

    coordenada_pseudo_controle = str(list_pseudo[contador_pseudo][0] + ", " + list_pseudo[contador_pseudo][1])
    # plt.plot(float(get_compon('lon', coordenada_pseudo_controle)), float(get_compon('lat', coordenada_pseudo_controle)), 'go',ms=markers * 1)  # <MATPLOTLIB>
    contador_pseudo = contador_pseudo + 1

    # 2) Gera a coordenada aleatória para o ponto cego.
    coordenada_ponto_cego = get_coord(x0, y0, raio, 2)
    # plt.plot(float(get_compon('lon', coordenada_ponto_cego)), float(get_compon('lat', coordenada_ponto_cego)), 'yo',ms=markers * 1)  # <MATPLOTLIB>

    # Essa seção produz o mapa com todos os pontos.

    list_random = numpy.empty(shape=(1, 2))
    list_grid = numpy.empty(shape=(1, 2))
    # print(list_random)

    # Quantos pontos gerar?
    # Em https://www.reddit.com/r/randonauts/comments/mrd6nn/randonautica_uses_ten_thousand_bit_anu_right/,
    # temos a informação de que o máximo raio utiliza 26 mil pontos quânticos.
    # o máximo raio permitido no aplicativo é de 10km.
    # O total de pontos quânticos deve ser diretamente proporcional à área do círculo,
    # de forma que a densidade de pontos/km² se mantenha constante.

    total_random_points = int(raio * raio * factor * factor * 26000 * math.pi / 314159200)

    for i in range(total_random_points):
        position = get_coord(x0, y0, raio * factor, 2)

        position_x = get_compon('lat', position)
        position_y = get_compon('lon', position)

        list_random = np.append(list_random, [[position_x, position_y]], axis=0)
        distancia = get_distancia(x0, y0, position_x, position_y)
        print("Preparando... mentalize seu objetivo (" + str(i) + "/" + str(total_random_points) + ").")

        if distancia <= raio:
            variavel_pra_nao_ficar_vazio_sem_plyplot = 1
            # plt.plot(float(position_y), float(position_x), 'ro', ms=markers) # <MATPLOTLIB>

        else:
            variavel_pra_nao_ficar_vazio_sem_plyplot = 1
            # plt.plot(float(position_y), float(position_x), 'ko', ms=markers * 0.2) # <MATPLOTLIB>

    list_random = np.delete(list_random, 0, axis=0)

    # Computa a distância com os vizinhos

    raio_busca_atrator = 0.001
    raio_busca_vazio = 0.001

    # Essa opção usa o antigo (e quebrado) método de encontrar atrator e vazio.
    legacy = 0

    if legacy == 1:

        index_max = numpy.where(frequency_atrator == numpy.amax(frequency_atrator))
        # intensidade_atrator = numpy.amax(frequency_atrator) # <MATPLOTLIB>

        index_min = numpy.where(frequency_vazio == numpy.amin(frequency_vazio))
        # intensidade_vazio = numpy.min(frequency_vazio) # <MATPLOTLIB>

    else:

        # 3) Gerar o atrator

        tree_atrator = spatial.KDTree(np.array(list_random))
        neighbors_atrator = tree_atrator.query_ball_tree(tree_atrator, raio_busca_atrator)
        frequency_atrator = np.array(list(map(len, neighbors_atrator)))
        mean_atrator = np.mean(frequency_atrator)
        std_atrator = np.std(frequency_atrator)
        forca_atrator = mean_atrator / std_atrator

        atrator_satisfeito = 0
        while atrator_satisfeito == 0:

            index_max = numpy.where(frequency_atrator == numpy.amax(frequency_atrator))
            intensidade_atrator = numpy.amax(frequency_atrator)

            dist = get_distancia(x0, y0, list_random[index_max][0][0], list_random[index_max][0][1])
            # print("O atrator calculado é " + str(dist) + " e o raio é" + str(raio))

            if dist < raio:
                atrator_satisfeito = 1
            else:
                np.put(frequency_atrator, index_max, [0])

        forca_atrator = abs(intensidade_atrator - mean_atrator) / std_atrator
        coordenada_atrator = (str(list_random[index_max][0][0])[0:18] + ", " + str(list_random[index_max][0][1])[0:18])

        # 4) Gerar o vazio

        tree_vazio = spatial.KDTree(np.array(list_random))
        neighbors_vazio = tree_vazio.query_ball_tree(tree_vazio, raio_busca_vazio)
        frequency_vazio = np.array(list(map(len, neighbors_vazio)))
        mean_vazio = np.mean(frequency_vazio)
        std_vazio = np.std(frequency_vazio)

        vazio_satisfeito = 0
        while vazio_satisfeito == 0:

            index_min = numpy.where(frequency_vazio == numpy.amin(frequency_vazio))
            intensidade_vazio = numpy.min(frequency_vazio)

            dist = get_distancia(x0, y0, list_random[index_min][0][0], list_random[index_min][0][1])
            # print("O vazio calculado é " + str(dist) + " e o raio é" + str(raio))

            if dist < raio:
                vazio_satisfeito = 1
            else:
                np.put(frequency_vazio, index_min, [99999])

        forca_vazio = 2 * abs(intensidade_vazio - mean_vazio) / std_vazio
        coordenada_vazio = (str(list_random[index_min][0][0][0:18]) + ", " + str(list_random[index_min][0][1][0:18]))

        if forca_vazio > forca_atrator:
            coordenada_anomalia = coordenada_vazio
            tipo_anomalia = "vazio"
        else:
            coordenada_anomalia = coordenada_atrator
            tipo_anomalia = "atrator"

    # ------------------------------ COORDENADAS GERADAS. INFORMAR AO USUÁRIO CONFORME SUA OPÇÃO --------------- #

    if MENU_principal == 3:
        print("------------------------------------ Resultados da jogada ------------------------------------")
        print("A coordenada de controle é:   " + coordenada_pseudo_controle)
        print("A coordenada de ponto cego é: " + coordenada_ponto_cego)
        print("A coordenada do atrator é:    " + coordenada_atrator)
        print("A coordenada do vazio é:      " + coordenada_vazio)
        print("A coordenada da anomalia é:   " + coordenada_anomalia + " e ela é um " + tipo_anomalia + ".")

    # ------------------------------------- TODA ESSA PARTE FAZ O PLOT ------------------------------

    # plt.plot(float(list_random[index_max][0][1]), float(list_random[index_max][0][0]), 'bo', ms=2)  # <MATPLOTLIB>
    # circle2 = plt.Circle((float(list_random[index_max][0][1]), float(list_random[index_max][0][0])), raio_busca_atrator, color='k', fill=False)  # <MATPLOTLIB>
    # ax.add_patch(circle2)  # <MATPLOTLIB>

    # plt.plot(float(list_random[index_min][0][1]), float(list_random[index_min][0][0]), 'mo', ms=2)  # <MATPLOTLIB>
    # circle3 = plt.Circle((float(list_random[index_min][0][1]), float(list_random[index_min][0][0])), raio_busca_vazio, color='k', fill=False)  # <MATPLOTLIB>

    # plt.plot(y0, x0, 'ks', ms=markers * 1)  # <MATPLOTLIB>
    # ax.add_patch(circle3)  # <MATPLOTLIB>

    # plt.grid()  # <MATPLOTLIB>
    # plt.show()  # <MATPLOTLIB>
    # plt.clf()  # <MATPLOTLIB>

    elif MENU_principal == 2 or MENU_principal == 1:

        if MENU_tipo_geracao == 2:
            visitar = coordenada_pseudo_controle
            if MENU_tipo_local == 1:
                visitar_tipo = "Coordenada desatrelada (ponto cego)."
            elif MENU_tipo_local == 2:
                visitar_tipo = "Coordenada desatrelada (atrator)."
            elif MENU_tipo_local == 3:
                visitar_tipo = "Coordenada desatrelada  (vazio)."
            elif MENU_tipo_local == 4:
                visitar_tipo = "Coordenada desatrelada  (anomalia - " + tipo_anomalia + ")."

        else:
            if MENU_tipo_local == 1:
                visitar = coordenada_ponto_cego
                visitar_tipo = "Coordenada atrelada (ponto cego)."
            elif MENU_tipo_local == 2:
                visitar = coordenada_atrator
                visitar_tipo = "Coordenada atrelada (atrator)."
            elif MENU_tipo_local == 3:
                visitar = coordenada_vazio
                visitar_tipo = "Coordenada atrelada (vazio)."
            elif MENU_tipo_local == 4:
                visitar = coordenada_anomalia
                visitar_tipo = "Coordenada atrelada (anomalia - " + tipo_anomalia + ")."

        print("")
        if MENU_tipo_local == 1:
            print("--------------------------------- Local definido (ponto cego) --------------------------------")
        elif MENU_tipo_local == 2:
            print("---------------------------------- Local definido (atrator) ----------------------------------")
        elif MENU_tipo_local == 3:
            print("----------------------------------- Local definido (vazio) -----------------------------------")
        elif MENU_tipo_local == 4:
            print("---------------------------------- Local definido (anomalia) ---------------------------------")
            print("A anomalia é um " + tipo_anomalia)

        print("Lembre-se: a decisão de visitar o local é sua. Julgue, com bom senso, se isso é seguro.")
        print("A coordenada selecionada é: " + visitar)
        print("1 - Visitei (virtualmente ou pessoalmente) o local e estou pronto para reportá-lo.")
        print("2 - Desisti de visitar o local e irei descartá-lo.")

        visitou = "0"
        visitou = str(input("Informe quando estiver pronto: "))

        while visitou != "1" and visitou != "2":
            visitou = str(input("Insira um valor válido: "))
        visitou = int(visitou)

        if visitou == 1:
            print("------------------------------------------ Veredito ------------------------------------------")
            print("O que você achou do local visitado?")
            print("1 - Visitei o local pessoalmente e, de alguma forma, o local foi relevante para mim.")
            print("2 - Visitei o local pessoalmente e o local não  significou nada para mim.")
            print("3 - Visitei o local pelo Street View e, de alguma forma, o local foi relevante para mim.")
            print("4 - Visitei o local pelo Street View e o local não  significou nada para mim.")
            veredito = str(input("Informe seu veredito: "))
            while veredito != "1" and veredito != "2" and veredito != "3" and veredito != "4":
                veredito = str(input("Insira um valor válido: "))
            veredito = int(veredito)

            if veredito == 1:
                veredito_resultado = "Visita presencial. Foi relevante."
            elif veredito == 2:
                veredito_resultado = "Visita presencial. Nao foi relevante."
            elif veredito == 3:
                veredito_resultado = "Visita virtual. Foi relevante."
            elif veredito == 4:
                veredito_resultado = "Visita virtual. Nao foi relevante."
            else:
                veredito_resultado = "CALL THE COPS! Tem algo errado com o programa. Serio." + str(veredito)

            if MENU_principal == 1:
                print("----------------------------------------- Resultados -----------------------------------------")
                print(veredito_resultado)
                print(visitar_tipo)
            if MENU_principal == 2:
                mensagem_plain = veredito_resultado + " " + visitar_tipo + " SALT: " + ''.join(
                    random.choice(string.ascii_uppercase + string.digits) for _ in range(30 - randrange(10)))
                mensagem_plain = bytes(mensagem_plain, 'ascii')

                # Faz a mensagem criptografada
                encrypted = public_key.encrypt(
                    mensagem_plain,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )

                # Escreve num arquivo identificado
                ind = datetime.now()
                ind = ind.strftime("%d%m%y%H%M%S")
                f = open('results/' + str(ind) + '.encry', 'wb')
                f.write(encrypted)
                f.close()

                print("----------------------------------------- Resultados -----------------------------------------")
                print("Como informado, você só poderá descobrir a natureza do local ao final do estudo quando a chave ")
                print("privada for publicada. Até lá, envia o arquivo para o Natanael. Ela não contém qualquer")
                print("informação que lhe permite identificá-lo, como dados do dispositivo ou as coordenadas,")
                print(" mas sim apenas o tipo de local (ponto cego, atrator, vazio, anomalia), o seu veredito")
                print("e a sua natureza.")
                print("")
                print("Para submeter os resultados do estudo, envie o arquivo " + str(ind) + ".encry para o Natanael.")
                print("Use a hash MD5 abaixo para, após decifrada, conferir a integridade da mensagem enviada:")
                print("")
                hashed = hashlib.md5(mensagem_plain)
                print(hashed.hexdigest())
