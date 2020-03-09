arquivo = open('out1.txt', 'w')
conteudo = ("Hello, world!")
arquivo.writelines(conteudo)
arquivo.close()