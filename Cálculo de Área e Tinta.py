n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))
área = n1 * n2
tinta = área / 2
print('Sua parede tem a dimensao de {}x{} e sua área é de {}m²'.format(n1,n2,área))
print('Para pintar sua parede, você precisará de {}l de tinta'.format(tinta))