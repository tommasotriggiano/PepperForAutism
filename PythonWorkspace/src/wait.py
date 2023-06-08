from naoqi import ALProxy

ip="192.168.43.229"
port = 9559
nome = "wait"
prova = ALProxy("ALBehaviorManager", ip, port)
prova.runBehavior(nome)



