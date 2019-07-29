import math
dic = {1:31,2:0,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
mes = get_analysis_date().month
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

if dic[mes] == get_analysis_date().day:
    media = grid.history.mean("daily", (str(dic[mes]) + "d"), 0)
    if math.isnan(media): media = 0
    return media
else:
    return 0