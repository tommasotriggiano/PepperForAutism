
import means

ip="localhost"
usr="root"
psw="playertomm740"
database="sql2238489"

string=list();
ciao=means.getListGesture(ip,usr,psw,database)
i=0
while i < len(ciao):
    print ciao[i]
    i=i+1