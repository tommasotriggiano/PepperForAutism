from naoqi import ALProxy
import sys
import means

ipdb="localhost"
user="root"
psw="playertomm740"
datadb="sql2238489"

nome = sys.argv[1];



ip="192.168.43.229"
port = 9559
sinonimo = means.getSinonimo(ipdb, user, psw, datadb, nome)
significato = means.getSign_Retorico(ipdb, user, psw, datadb, nome)
spec=ALProxy("ALTextToSpeech", ip, port)
spec.say("Il nome del gesto che vedrai, E. "+sinonimo+ ". In che modo si usa?: " + significato)


