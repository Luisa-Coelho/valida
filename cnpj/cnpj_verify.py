i = 0
elem = 0
check = []
multipliers = [9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5]


cnpj = list(input('insira seu cnpj'))
cnpj_real = []
for sublist in cnpj:
    for item in sublist:
        cnpj_real.append(item)
cnpj_verify = cnpj_real      

                 
try:
    if len(cnpj_verify)<14:
        print('insira 14 digitos')
            
    else:
        while elem < 12:
            if cnpj_verify[elem] == cnpj_verify[0]:
                check.append(cnpj_verify[elem] * multipliers[i])
                elem+=1
            else:
                i+=1
                check.append(cnpj_verify[elem] * multipliers[i])
                elem+=1
except:
    raise AttributeError


print(check)         
