import random
import datetime
from datetime import timedelta
from raizbot import Bot, UndefinedRoutError
from choices import LESTE, DIRCEU, SUL, NORTE, TIMON, SUB_GRUPOS, SEXOS, ROTAS, REPS, LOJAS, RESIDENCIAS, MESES, TP_CLIENTE

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

def calendario():
    periodo = 1095 #Anos convertidos em dias.
    _lista = []
    for i in range(periodo):
        _lista.append(datetime.datetime.now() - datetime.timedelta(i+1))
    _data1 = random.choice(_lista)
    _dia = datetime.datetime.strftime(_data1, '%d/%m/%Y') #Retorna dia formatado
    _mes = datetime.datetime.strftime(_data1, '%B') #Retorna mês formatado
    _ano = datetime.datetime.strftime(_data1, '%Y') #Retorna mês formatado

    return _dia, _mes, _ano 

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
        # Ativa a função calendario e retorna os valores
        _calendario = calendario()
        data_compra = _calendario[0]
        mes = _calendario[1]
        ano = _calendario[2]
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
        tp_cliente = _choice(TP_CLIENTE)

        #Mandar informações para a classe
        bot = Bot(id_cliente=id_cliente, data_aniversario=data_aniversario, sexo=sexo, rep=rep, telefone=telefone,
            email=email, loja=loja, minuta=minuta, pedido=pedido, data_compra=data_compra, mes=mes, ano=ano,
            valor_mercadoria=valor_mercadoria, nce=nce, sub_grupo=sub_grupo, mercadoria=mercadoria,
            rota=rota, bairro=bairro, cidade=cidade, uf=uf, zona=zona, tp_residencia=tp_residencia, tp_cliente=tp_cliente)
        bot.show_info()
        #bot.gravar_dados()

def user():
    qtd = input('INFORME A QUANTIDADE DE INFORMAÇÕES DESEJADAS: ')
    return qtd

qtd = int(user())
start(qtd)
