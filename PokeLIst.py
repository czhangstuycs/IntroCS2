#!/usr/bin/python
print "Content-type: text/html\n"
def readFileIntoLists(filename):
        lines = open(filename).read().split("\n")
        return [line.split(",") for line in lines ]


def getHeader(L):
        return L[0]

def getData(L):
        while L[-1] == ['']:
                L=L[:-1]
        return L[1:]


data1 = readFileIntoLists("pokemon.csv")

_pokeGeneralH =  getHeader(data1)
_pokeGeneral = getData(data1)#[:10]

data1 = readFileIntoLists("pokemon_stats.csv")
_pokeStatsH = getHeader(data1)
_pokeStats = getData(data1)


data1 = readFileIntoLists("stats.csv")
_statsH = getHeader(data1)
_stats = getData(data1)

#uses _stats
def getStatName(id):
        if id < 1 or id > 8:
                print "invalid stat id:"+str(id)
                return "invalid!";
        id = str(id)
        id = str(id)
        for line in _stats:
                if line[0]==id:
                        return line[2]
        print "invalid value, reached end of getStatName"
        return "invalid value, reached end of getStatName"
                
#uses _stats
def getStatID(s):
        statNames = [ a[2] for a in _stats]
        statNames = ["error"]+statNames
        if not s.lower() in statNames:
                return -1
        return statNames.index(s.lower())

def getOtherAttributes(pokemon_ID):
    AttributesList=[]
    for i in range(3):
        pokeAttributes=_pokeStats[pokemon_ID*5+i]
        AttributesList.append(pokeAttributes[2])
    AttributesList.append(_pokeStats[pokemon_ID*5+5][2])
    return AttributesList

def makeSinglePokeList(pokemon_ID):
    Pokelist=[pokemon_ID+1,_pokeGeneral[pokemon_ID][1]]
    for i in range(3,5):
        Pokelist.append(_pokeGeneral[pokemon_ID][i])
        return Pokelist + getOtherAttributes(pokemon_ID)
   
def makePokeTable():
   tablestr="<tr><td>ID</td><td>NAME</td><td>Height</td><td>Weight</td><td>HP</td><td>Attack</td><td>Defense</td><td>Speed</td></tr>"
   for i in range(0,100):
        tablestr+="\n<tr>"
        for stat in makeSinglePokeList(i):
            tablestr+="\n<td>" + str(stat) + "</td>"
        tablestr+="\n</tr>"
   return tablestr + "\n</table>\n</body>"    

print makePokeTable()
