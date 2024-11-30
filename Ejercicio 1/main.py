pages = [
    "Page 0) Al principio pensé que era algún camión pasando a gran velocidad,\npero el temblor se sostubo... Me desperte de golpe y pensé -ES UN TEMBLOR...\nQué vas a hacer?\n1) Esperar a que pase \n2) Salir corriendo afuera \n3) Pedir ayuda",
    "Page 1) Me quede inmóvil, esperando a que el temblor pase...\nDe repente se hizo la oscuridad...\nHubo mucho... sentí que algo se caía... \nFIN",
    "Page 2) Sali corriendo por las escaleras... de repente se apagaron todas las luces y la puerta no abría...\nQue vas a hacer?\n3) Esconderme en el baño\n4) Intentar romper la puerta\n5) Saltar por la ventana",
    "Page 3) Me quede inmóvil, esperando a que el temblor pase... \nDe repente se hizo la oscuridad...\nHubo mucho ruido... sentí que algo se caía... \nFIN",
    "Page 4) Le di varias patadas a la puerta, pero esta no caía... \nHasta sentí que la casa se derrumbaba...\nFIN",
    "Page 5) Salté por la ventana... Había mucha gente en la calle, \nvi como mi casa se derrumbaba... Esperamos a que el temblor pase... Esperamos horas y hasta días, y el temblor seguía\nCONTINUARA"
]

def showPage(pageNumber):
    text = pages[pageNumber]
    print(text)
    response = input()
    showPage(int(response))

showPage(0)