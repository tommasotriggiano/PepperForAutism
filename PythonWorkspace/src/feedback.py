from naoqi import ALProxy
import sys


ipdb="localhost"
user="root"
psw="playertomm740"
datadb="sql2238489"

nome = sys.argv[1];
ip="192.168.43.229"
port = 9559

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

spec=ALProxy("ALTextToSpeech", ip, port)
prova = ALProxy("ALBehaviorManager", ip, port)
spec.say("Ci sei quasi. Puoi farcela! Ti mostro il gesto un altra volta")
prova.runBehavior(nome)
