
from naoqi import ALProxy


"192.168.1.102"
"pepper.local."
"9559"

ip="pepper.local."
port = 9559
prova = ALProxy("ALBehaviorManager", ip, port)
prova.runBehavior('ChiedereParolaProgress')