from naoqi import ALProxy

ip="192.168.43.229"
port = 9559
spec=ALProxy("ALTextToSpeech", ip, port)
spec.say("Non ti scoraggiare. Puoi chiedere, al tuo tutor di ripetere il gesto, se vuoi.")