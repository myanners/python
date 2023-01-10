import enchant

# Crie um verificador de ortografia para o português do Brasil
verificador = enchant.Dict("en_US")

# Verifique se a palavra "amor" está escrita corretamente
if verificador.check("peace"):
   print("A palavra 'peace' está escrita corretamente.")
else:
    print("A palavra 'peace' está escrita incorretamente.")