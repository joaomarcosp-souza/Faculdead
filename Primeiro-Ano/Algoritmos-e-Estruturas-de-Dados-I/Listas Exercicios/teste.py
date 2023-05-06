import unidecode 

lista = ["hell°",  "tromsø",  "stävänger", "ölut", "és"] 
print('\nLista original:\n', lista) 
  
for i in range(len(lista)): 
    lista[i] = unidecode.unidecode(lista[i]) 
print('\n Resultado:\n', lista) 