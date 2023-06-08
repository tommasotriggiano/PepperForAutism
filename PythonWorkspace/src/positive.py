from naoqi import ALProxy
import sys


ip="192.168.43.229"
port = 9559
tentativi = sys.argv[1]
tempo = sys.argv[2]




spec=ALProxy("ALTextToSpeech", ip, port)


prova = ALProxy("ALBehaviorManager", ip, port)
prova.runBehavior("Positive")
t = int(tentativi)

if( t == 1):
	spec.say("Hai eseguito il gesto al primo tentativo. In un tempo di"+tempo+"secondi. Ora aspetta li mentre carico il prossimo gesto.")
else:
	spec.say("Hai effettuato."+tentativi+"tentativi. In un tempo di"+tempo+"secondi. Ora aspetta li mentre carico il prossimo gesto.")
	
	