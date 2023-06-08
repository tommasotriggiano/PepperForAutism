
import means
import sys 

nome= sys.argv[1]
formVer=[sys.argv[2]]
contesto=[ sys.argv[3]]
sinonimi=sys.argv[4]
significato=sys.argv[5]
gramm=sys.argv[6]
prag=sys.argv[7]
sem=sys.argv[8]
retorico=sys.argv[9]

ipdb="sql2.freesqldatabase.com"
username="sql2238489"
password="sB9*qI3%"
datadb="sql2238489"


    

means.insertSemantic(ipdb, username, password, datadb, nome, formVer, contesto, sinonimi, significato, gramm, prag, sem, retorico)


