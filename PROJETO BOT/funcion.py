import random
from raizbot import Bot, UndefinedRoutError
from choices import LESTE, DIRCEU, SUL, NORTE, TIMON, SUB_GRUPOS, SEXOS, ROTAS, REPS, LOJAS, RESIDENCIAS, MESES

def _choice(option):
    return random.choice(option)

def get_bairro(rota):
    ZONAS = {'SUL': SUL, 'DIRCEU': DIRCEU, 'LESTE': LESTE, 'NORTE': NORTE, 'TIMON': TIMON}

    if rota in [1, 2]:
        _rota = 'SUL'
    elif rota in [3]:
        _rota = 'DIRCEU'
    elif rota in [4, 5]:
        _rota = 'LESTE'
    elif rota in [6, 7]:
        _rota = 'NORTE'
    elif rota in [8, 9]:
        _rota = 'TIMON'      
    else:
        raise UndefinedRoutError(f'{rota}')
        
    return random.choice(ZONAS[_rota])

def msg_inicio():
    print('********************\nMY BOT IN PYTHON WITH SQL\n********************')

def start(qtd):
    for i in range(qtd):
        id_cliente = random.randint(1, 100)
        data_aniversario = str(random.randrange(1,28)) + '/' + str(random.randrange(1,13)) + '/' + str(random.randrange(1940,2003))
        sexo = _choice(SEXOS)
        rep = _choice(REPS)
        telefone = '86 9xxxx-xxxx'
        email = 'teste@...'
        loja = _choice(LOJAS)
        minuta = random.randrange(1,2000)
        pedido = loja + str(minuta)
        data_compra = str(random.randrange(1,28)) + '/' + str(random.randrange(1,13)) + '/' + str(random.randrange(2019,2021))
        _start_mes = data_compra.find('/') + 1
        _end_mes = data_compra.find('/', _start_mes)
        _mes = data_compra[_start_mes:_end_mes]
        mes = MESES[_mes]
        ano = data_compra[_end_mes + 1 :]
        nce = mercadoria = '#'
        valor_mercadoria = int(random.randrange(500, 10000))
        sub_grupo = _choice(SUB_GRUPOS)
        rota = int(_choice(ROTAS))
        bairro = get_bairro(rota)
        if rota <=7:
            cidade = 'TERESINA'
            uf = 'PI'
        else:
            cidade = 'TIMON'
            uf = 'MA'
        zona = 'URBANA'
        tp_residencia = _choice(RESIDENCIAS)

        #Mandar informações para a Memoria
        bot = Bot(id_cliente=id_cliente, data_aniversario=data_aniversario, sexo=sexo, rep=rep, telefone=telefone,
            email=email, loja=loja, minuta=minuta, pedido=pedido, data_compra=data_compra, mes=mes, ano=ano,
            valor_mercadoria=valor_mercadoria, nce=nce, sub_grupo=sub_grupo, mercadoria=mercadoria,
            rota=rota, bairro=bairro, cidade=cidade, uf=uf, zona=zona, tp_residencia=tp_residencia)
        bot.show_info()
        bot.gravar_dados()

def user():
    qtd = input('INFORME A QUANTIDADE DE INFORMAÇÕES DESEJADAS: ')
    return qtd

qtd = int(user())
start(qtd)
