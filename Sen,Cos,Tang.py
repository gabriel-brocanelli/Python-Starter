import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(ângulo,seno))
cos = math.cos(math.radians(ângulo))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(ângulo,cos))
tan = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tan))