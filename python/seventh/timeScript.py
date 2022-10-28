import time

hour = time.localtime().tm_hour

if hour > 19:
    print("Es hora de ir a casa a descansar, el trabajo ha terminado : ) ")
else:
    hourLeft = 19 - hour
    print("Aún queda(n)",hourLeft,"hora(s) de trabajo... ¡Vamos! : )")