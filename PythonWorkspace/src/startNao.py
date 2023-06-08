from naoqi import ALProxy

"192.168.1.102"
"pepper.local."
"9559"

ip="192.168.43.229"
port = 9559

prova = ALProxy("ALBehaviorManager", ip, port)
prova.runBehavior('inizio')