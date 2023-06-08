
import means;
import sys;
from naoqi import ALProxy;

nomeGesto = sys.argv[1]
ip="localhost"
username="root"
password="playertomm740"
datadb="sql2238489"

scenario= means.getScenario(ip, username, password, datadb, nomeGesto)

iprobot="192.168.43.229"
port = 9559
prova = ALProxy("ALBehaviorManager", iprobot, port)
prova.runBehavior(scenario)