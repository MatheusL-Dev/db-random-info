import mysql.connector

class UndefinedRoutError(Exception):
    pass

class Bot:
    def __init__(self, id_cliente='', data_aniversario='', sexo='', rep='', telefone='', email='', loja='', minuta='', pedido='', data_compra='', mes='', ano='', valor_mercadoria='', nce='', sub_grupo='', mercadoria='', rota='', bairro='', cidade='', uf='', zona='', tp_residencia='', tp_cliente=''):
        self.id_cliente = id_cliente
        self.data_aniversario = data_aniversario
        self.sexo = sexo
        self.rep = rep
        self.telefone = telefone
        self.email = email
        self.loja = loja
        self.minuta = minuta
        self.pedido = pedido
        self.data_compra = data_compra
        self.mes = mes
        self.ano = ano
        self.valor_mercadoria = valor_mercadoria
        self.nce = nce
        self.sub_grupo = sub_grupo
        self.mercadoria = mercadoria
        self.rota = rota
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.zona = zona
        self.tp_residencia = tp_residencia
        self.tp_cliente = tp_cliente

    def show_info(self):
        print('GRAVANDO AS INFORMAÇÕES NO CAMINHO: ','{}'.format(self))
        print(self.id_cliente, self.data_aniversario, self.sexo, self.rep, self.telefone, self.email, self.loja, self.minuta, self.pedido, self.data_compra, self.mes, self.ano, self.valor_mercadoria, self.nce, self.sub_grupo, self.mercadoria, self.rota, self.bairro, self.cidade, self.uf, self.zona, self.tp_residencia, self.tp_cliente)

    def gravar_dados(self):
        conexao = mysql.connector.connect(db='db_ucase', user='root', passwd='')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO tb_bot (cd_cliente, dt_aniversario, sexo, rep, telefone, email, loja, minuta, pedido, dt_compra, mes, ano, vl_mercadoria, nce, sub_grupo, mercadoria, rota, bairro, cidade, uf, zona, tp_residencia, tp_cliente) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.id_cliente, self.data_aniversario, self.sexo, self.rep, self.telefone, self.email, self.loja, self.minuta, self.pedido, self.data_compra, self.mes, self.ano, self.valor_mercadoria, self.nce, self.sub_grupo, self.mercadoria, self.rota, self.bairro, self.cidade, self.uf, self.zona, self.tp_residencia, self.tp_cliente))
        print ('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        conexao.commit()
        conexao.close()