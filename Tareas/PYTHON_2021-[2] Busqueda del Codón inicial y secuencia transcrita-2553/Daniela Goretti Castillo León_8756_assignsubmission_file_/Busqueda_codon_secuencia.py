adn = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'   # Aquí se muestra la secuencia de ADN donde queremos buscar los codones
inicio = 'TAC'   # Este es el codón de inicio de la secuencia (AUG -> TAC)
paro = 'TAA'   # Este es el codón de paro de la secuencia (UAA -> TAA)
print("El codón de inicio TAC se encuentra en la posición ", adn.find(inicio), "y termina en ", adn.find(paro)+2)
# Aquí se busca la posición en donde se encuentra el codón de inicio, mientras que para ver dónde termina se le suma un
# dos a la posición del codón de paro dado que termina dos bases después de donde empieza (es un triplete)

print("Fragmento de DNA que será transcrito: ", adn[(adn.find(inicio)):(adn.find(paro))])
# Aquí se menciona las bases que conforman el fragmento desde el codón de inicio hasta antes del codón de paro
