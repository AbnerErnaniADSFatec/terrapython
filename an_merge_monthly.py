meses = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
dic = {1:31,2:0,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
an_mes = get_analysis_date().month
ano = get_analysis_date().year
bissexto = None

if ano % 4 == 0:
	if ano % 100 == 0:
	    if ano % 400 == 0: bissexto = True
	    else: bissexto = False
	else: bissexto = True
else: bissexto = False
if bissexto: dic[2] = 29
else: dic[2] = 28

geocodigo = get_value("geocodigo")
nome_municipio = get_value("nome1")
uf = get_value("uf")
# maxima = grid.zonal.max("monthly", 0)
# media = grid.zonal.mean("monthly", 0)
mes = meses[an_mes]

if dic[an_mes] == get_analysis_date().day:
    add_value("geocodigo", geocodigo)
    add_value("nome_municipio", nome_municipio)
    add_value("uf", uf)
    add_value("maxima", grid.zonal.max("monthly", 0))
    add_value("media", grid.zonal.mean("monthly", 0))
    add_value("mes", mes)
else:
    add_value("geocodigo", "")
    add_value("nome_municipio", "")
    add_value("uf", "")
    add_value("maxima", 0)
    add_value("media", 0)
    add_value("mes", "")