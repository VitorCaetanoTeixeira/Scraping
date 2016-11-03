import urllib
import urllib2
import re
import csv



url = []
#print url
with open('c://Users/apprenticebr/Desktop/Estudo/exel formatado para buscar.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #row
        #print(row[0])
        #print(row[0].split(';'))
        temp = row[0].split(';')
        nome = temp[1].lower()
        se_nome = nome.replace(' ','')
        nome = se_nome.replace('.','')
        nome = nome.replace('/','')
        #print nome
        
        
               

        
        url.append("http://www.cnpjbrasil.com/e/cnpj/"+nome+"/"+temp[0])       
        

i = 0
a = 0

while a < len(url):
    #while i< len(urls):
    htmlfile = urllib.urlopen(url[a])
    print url[a]
    htmltext = htmlfile.read()
    #print (htmltext)
    regex = '<p class="ae1">(.+?)</p>'
    pattern = re.compile(regex)
    #print "//////////"
    #print pattern
    quotation = re.findall(pattern, htmltext)
    #print "//////////"
    print len(quotation)
    
    if len(quotation) > 0:
        regex = '<span class="text">(.+?)</span>'
        pattern = re.compile(regex)
        quotation = re.findall(pattern, quotation[0])
        while i < len(quotation):
            print (quotation)
            i+=1
    a+=1
