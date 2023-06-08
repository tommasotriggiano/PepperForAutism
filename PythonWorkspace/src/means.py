import MySQLdb

def establishConnectionDb(ip, username, password, datadb):
    try:
        db=MySQLdb.connect(ip, username,password, datadb)
    
        return db;
    except:
        print "Error to establish connection to db"
        
def createDb(ip, user, psw,datadb):
    try:
        db=establishConnectionDb(ip, user, psw, datadb)
        cursor=db.cursor()
        sqlUse="USE %s" %datadb
        cursor.execute(sqlUse)
        
        sqlTable="CREATE TABLE Gesture (id_gesture INT NOT NULL AUTO_INCREMENT , nome VARCHAR(50) NOT NULL , sinonimo VARCHAR(255) NULL , significato VARCHAR(100) NOT NULL , clas_grammaticale VARCHAR(20) NOT NULL , clas_pragmatica VARCHAR(100) NULL , clas_semantica VARCHAR(100) NOT NULL , sign_retorico VARCHAR(200) NULL , PRIMARY KEY (id_gesture, nome));"
        cursor.execute(sqlTable)
        
        sqlTable2="CREATE TABLE form_Verbale ( id_form_verbale INT NOT NULL AUTO_INCREMENT , descrizione VARCHAR(255) NOT NULL , gesture INT NOT NULL , PRIMARY KEY (id_form_verbale));"
        cursor.execute(sqlTable2)
        
        sqlTable3="CREATE TABLE contesto ( id_contesto INT NOT NULL AUTO_INCREMENT , descrizione VARCHAR(255) NOT NULL , gesture INT NOT NULL , PRIMARY KEY (id_contesto));"
        cursor.execute(sqlTable3)
        
        sqlFK1= "ALTER TABLE contesto ADD FOREIGN KEY(gesture) REFERENCES Gesture(id_gesture) ON DELETE CASCADE;"
        sqlFK2= "ALTER TABLE form_Verbale ADD FOREIGN KEY(gesture) REFERENCES Gesture(id_gesture) ON DELETE CASCADE;"
        cursor.execute(sqlFK1)
        cursor.execute(sqlFK2)
    except:
        print "Error to create database"
    
    
def insertSemantic(ip,usr, psw, database, nome, formVerbale, cont, sinonimo,sign,classGram,classPrag,classSem,signRetorico ):
    db=establishConnectionDb(ip, usr, psw, database)
    cursor1=db.cursor()
    sqlUse="USE %s" %database
    cursor1.execute(sqlUse)
    
    gesture={
        'nom':nome,
        'sin':sinonimo,
        'signi':sign,
        'gram':classGram,
        'prag':classPrag,
        'sem':classSem,
        'reto':signRetorico
    }
    
    sqlGestu="INSERT INTO Gesture(nome, sinonimo,significato,clas_grammaticale,clas_pragmatica, clas_semantica, sign_retorico) VALUES (%(nom)s,%(sin)s,%(signi)s,%(gram)s,%(prag)s,%(sem)s,%(reto)s)"
    try:
        cursor1.execute(sqlGestu, gesture)
        db.commit()
    except:
        print "Error to insert into Gesture table"
    
   
   
    
    insertFormVerb(ip,usr,psw,database, nome, formVerbale)
    insertContest(ip,usr,psw,database, nome, cont)
    db.close()
    
    
def insertFormVerb(ip,usr,psw,database, nameGesture, desc):
    name="SELECT id_gesture FROM Gesture as g WHERE g.nome='%s'" % nameGesture
    db=establishConnectionDb(ip, usr, psw, database)
    cursor2=db.cursor()
    sqlUse="USE %s" %database
    cursor2.execute(sqlUse)
    for i in range(len(desc)):
       
        sqlVerb="INSERT INTO form_Verbale(descrizione, gesture) VALUES('%s', (%s))" % (desc[i], name)
        try:
            cursor2.execute(sqlVerb)
            db.commit()
        except:
            print "Error to insert into form_Verbale table"
    
def insertContest(ip,usr,psw,database, nameGesture, desc):
    name="SELECT id_gesture FROM Gesture as g WHERE g.nome='%s'" % nameGesture
    db=establishConnectionDb(ip, usr, psw, database)
    cursor3=db.cursor()
    sqlUse="USE %s" %database
    cursor3.execute(sqlUse)
    for i in range(len(desc)):
        
        sqlCont="INSERT INTO contesto(descrizione, gesture) VALUES('%s', (%s))" % (desc[i],name)
        try:
            cursor3.execute(sqlCont)
            db.commit()
        except:
            print "Error to insert into contesto tables"
    
    
def getSpecificSemanticGesture(ip, username, password, datadb, nomeGesto):
    try:   
        string= "NOME: " + nomeGesto
        string = string + "\nFORMVERB: " + getFormVerb(ip, username, password, datadb, nomeGesto) \
            + "\nCONTESTI: " + getContest(ip, username, password, datadb, nomeGesto)\
            + "\nSINONIMI: " + getSinonimo(ip, username, password, datadb, nomeGesto)\
            + "\nSIGNIFICATO: " + getSignificato(ip, username, password, datadb, nomeGesto)\
            + "\nCLASS_GRAMMATICALE: " + getClass_Gram(ip, username, password, datadb, nomeGesto) \
            + "\nCLASS_PRAGMATICA: " + getClass_Prag(ip, username, password, datadb, nomeGesto)\
            + "\nCLASS_SEMANTICA: " + getClass_Sem(ip, username, password, datadb, nomeGesto)\
            + "\nSIGN_RETORICO: " + getSign_Retorico(ip, username, password, datadb, nomeGesto)
         
        return string
         
    except:
        print "Error to return a Gesture Specific Semantic "

def getFormVerb(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT f.descrizione  FROM form_Verbale as f WHERE gesture=(SELECT id_gesture FROM Gesture as g WHERE g.nome='%s')" % nomeGesto
    try:
        cursor.execute(sql)
        res=cursor.fetchall()
        List=list();
        for t in res:
            List.append(str(t[0]))
        List= map(str, List)
        i=0
        string=""
        while i < len(List):
            string=string +" - " + str(List[i])
            i=i+1
        db.close()
        return string
    except:
        print "Error getFormVerb"

def getContest(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT c.descrizione  FROM contesto as c WHERE gesture=(SELECT id_gesture FROM Gesture as g WHERE g.nome='%s')" % nomeGesto
    try:
        cursor.execute(sql)
        res=cursor.fetchall()
        List=list();
        for t in res:
            List.append(str(t[0]))
        List= map(str, List)
        i=0
        string=""
        while i < len(List):
            string=string +" - " + str(List[i])
            i=i+1
        db.close()
        return string
    except:
        print "Error getContest"

def getSinonimo(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor();
    
    sql= "SELECT g.sinonimo  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getSinonimo"
        
def getScenario(ip,username,password,datadb,nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor();
    sql= "SELECT g.scenario  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getScenario"
    
    

def getSignificato(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.significato  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getSignificato"
    
def getClass_Gram(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.clas_grammaticale  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getClass_Gram" 

def getClass_Prag(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.clas_pragmatica  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getClass_Prag"     

def getClass_Sem(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.clas_semantica  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getClass_Sem" 

def getSign_Retorico(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.sign_retorico  FROM Gesture as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getSign_Retorico" 

 
        
def removeGesture(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "DELETE FROM Gesture  WHERE nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= cursor.fetchone()
        db.close()
        return res
    except:
        print "Error Delete gesture" 

def getListGesture(ip, username, password,datadb):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "Select nome from Gesture"
    try:
        cursor.execute(sql)
        res=cursor.fetchall()
        List=list();
        
        for t in res:
            List.append(str(t[0]))
            
        List= map(str, List)
        i=0
        
        string=list()
        while i < len(List):
            string.append(str(List[i]))
            i=i+1
            
        db.close()
        return string
    except:
        print "Error read list gesture" 
