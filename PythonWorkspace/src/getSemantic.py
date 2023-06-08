
import sys
import means

ipdb="localhost"
username="root"
password="playertomm740"
datadb="sql2238489"

nome=sys.argv[1]

print(means.getSignificato(ipdb, username, password, datadb, nome));
