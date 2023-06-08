from naoqi import ALProxy
import sys


ip="192.168.43.229"
port = 9559
nome=sys.argv[1]




if(nome == "baciareProgress"):
    nome = "Baciare"
if(nome == "pregareProgress"):
    nome = "To_PrayProgress"
if(nome == "pauraProgress"):
	nome = "FearProgress"
if(nome=="salutareProgress"):
	nome="Salutare"
if(nome=="pensareProgress"):
	nome="Indicare"
if(nome=="ChiedereParolaProgress"):
	nome= "ChiedereParolaProgress"

prova = ALProxy("ALBehaviorManager", ip, port)
prova.runBehavior(nome)






