
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
        
        
        sqlTable="CREATE TABLE Gesti (nome VARCHAR(50) NOT NULL , form_verbale VARCHAR(255) NOT NULL, contesto VARCHAR(255) NOT NULL, sinonimo VARCHAR(255) NULL , significato VARCHAR(100) NOT NULL , clas_grammaticale VARCHAR(20) NOT NULL , clas_pragmatica VARCHAR(100) NULL , clas_semantica VARCHAR(100) NOT NULL , sign_retorico VARCHAR(200) NULL , PRIMARY KEY (nome));"
        cursor.execute(sqlTable)
        
    except:
        print "Error to create database"
    
    
def insertSemantic(ip,usr, psw, database, nome, formVerbale, cont, sinonimo,sign,classGram,classPrag,classSem,signRetorico ):
    db=establishConnectionDb(ip, usr, psw, database)
    cursor1=db.cursor()
   
    
    gesture={
        'nom':nome,
        'fv':formVerbale,
        'con':cont,
        'sin':sinonimo,
        'signi':sign,
        'gram':classGram,
        'prag':classPrag,
        'sem':classSem,
        'reto':signRetorico
    }
    
    sqlGestu="INSERT INTO Gesti (nome,form_verbale,contesto, sinonimo,significato,clas_grammaticale,clas_pragmatica, clas_semantica, sign_retorico) VALUES (%(nom)s,%(fv)s,%(con)s,%(sin)s,%(signi)s,%(gram)s,%(prag)s,%(sem)s,%(reto)s)"
    try:
        cursor1.execute(sqlGestu, gesture)
        db.commit()
    except:
        print "Error to insert into Gesture table"
    
    
    db.close()
    
    

    
def getSpecificSemanticGesture(ip, username, password, datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    sql="SELECT * from Gesti WHERE nome='%s';" % nomeGesto
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        
        
        for row in result:
        
            GestureName = row[0]
            FormulazioneVerbale = row[1]
            Contesto = row[2]
            Sinonimo = row[3]
            Significato = row[4]
            Classificazione_Grammaticale= row[5]
            Classificazione_Pragmatica=row[6]
            Classificazione_Semantica=row[7]
            Significato_Retorico=row[8]
            # Now print fetched result
            
            return "GestureName=%s\nFormulazioneVerbale=%s\nContesto=%s\nSinonimo=%s\nSignificato=%s\nClassificazione_Grammaticale=%s\nClassificazione_Pragmatica=%s\nClassificazione_Semantica=%s\nSignificato_Retorico=%s" %  (GestureName,FormulazioneVerbale,Contesto, Sinonimo,Significato, Classificazione_Pragmatica, Classificazione_Grammaticale, Classificazione_Semantica, Significato_Retorico )
        db.close()
    except:
        print "Error to return a Gesture Specific Semantic "

def getFormVerb(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT form_verbale as Formulazione_Verbale FROM Gesti WHERE nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getFormVerb"

def getContesto(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT contesto  FROM Gesti WHERE  nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close
        return res
    except:
        print "Error getContesto"

def getSinonimo(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.sinonimo  FROM Gesti as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getSinonimo"

def getSignificato(ip, username, password,datadb, nomeGesto):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    sql= "SELECT g.significato  FROM Gesti as g  WHERE g.nome='%s'" % nomeGesto
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
    
    sql= "SELECT g.clas_grammaticale  FROM Gesti as g  WHERE g.nome='%s'" % nomeGesto
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
    
    sql= "SELECT g.clas_pragmatica  FROM Gesti as g  WHERE g.nome='%s'" % nomeGesto
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
    
    sql= "SELECT g.clas_semantica  FROM Gesti as g  WHERE g.nome='%s'" % nomeGesto
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
    
    sql= "SELECT g.sign_retorico  FROM Gesti as g  WHERE g.nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        res= str(cursor.fetchone()[0])
        db.close()
        return res
    except:
        print "Error getSign_Retorico" 

def getAllDatabase(ip, username, password, datadb):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    sql="SELECT g.nome as Nome, g.form_verbale as Formulazione_Verbale, g.contesto as Contesto, g.sinonimo as Sinonimo, g.significato as Significato, g.clas_grammaticale as Classificazione_Grammaticale,g.clas_pragmatica as Classificazione_Pragmatica, g.clas_semantica as Classificazione_Semantica, g.sign_retorico as Significato_Retorico FROM Gesti as g;"
    try:
        cursor.execute(sql)
        for row in cursor:
            print row
        db.close()
        
    except:
        print "Error to return a Gesture Specific Semantic "  
        

def setFormVerb(ip, username, password, datadb, nomeGesto, newFormVerb):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'verb': newFormVerb,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET form_verbale=%(verb)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Formulazione Verbale "  
    db.close()
    
def setContesto(ip, username, password, datadb, nomeGesto, newContest):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'cont': newContest,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET contesto=%(cont)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Contesto "  
    db.close()

def setSinonimo(ip, username, password, datadb, nomeGesto, newSinonimo):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'sin': newSinonimo,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET sinonimo=%(sin)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Sinonimo  "  
    db.close()    

def setSignificato(ip, username, password, datadb, nomeGesto, newSignificato):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'sin': newSignificato,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET significato=%(sin)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Significato  "  
    db.close()
    
def setClassGrammaticale(ip, username, password, datadb, nomeGesto, newClassGrammaticale):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'gramm': newClassGrammaticale,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET clas_grammaticale=%(gramm)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Classificazione Grammaticale  "  
    db.close()  

def setClassPragmatica(ip, username, password, datadb, nomeGesto, newClassPragmatica):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'gramm': newClassPragmatica,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET clas_pragmatica=%(gramm)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Classificazione Pragmatica  "  
    db.close()        
    
def setClassSemantica(ip, username, password, datadb, nomeGesto, newClassSemantica):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'gramm': newClassSemantica,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET clas_semantica=%(gramm)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Classificazione Semantica  "  
    db.close()

def setSignRetorico(ip, username, password, datadb, nomeGesto, newSignRetorico):
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    
    ge={
        'ret': newSignRetorico,
        'nom': nomeGesto
    }
    sql="UPDATE Gesti SET sign_retorico=%(ret)s WHERE nome=%(nom)s" 
    try:
        
        cursor.execute(sql, ge)
        db.commit()
        return True
    except:
        print "Error to Modify Significato Retorico  "  
    db.close()

def deleteGesture(ip, username, password, datadb, nomeGesto):    
    db=establishConnectionDb(ip, username, password, datadb)
    cursor=db.cursor()
    sql= "DELETE FROM Gesti WHERE nome='%s'" % nomeGesto
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        print "Error to delete %s" % nomeGesto
    db.close()