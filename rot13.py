def rot13(phrase):
    x=0
    new=""
    while x<len(phrase):
        if (phrase[x] >= 'A' and phrase[x] <= 'Z'):
            new = new + chr((ord(phrase[x]) - ord('A') + 13)%26 + ord('A'))
            x=x+1
        elif (phrase[x] >= 'a' and phrase[x] <= 'z'):
            new = new + chr((ord(phrase[x]) - ord('a') + 13)%26 + ord('a'))
            x=x+1
        else:
            new = new + phrase[x]
            x=x+1
    return new

print rot13('Justin Bieber')

def rotX(phrase,n):
    x=0
    new=""
    while x<len(phrase):
        if (phrase[x] >= 'A' and phrase[x] <= 'Z'):
            new = new + chr((ord(phrase[x]) - ord('A') + n)%26 + ord('A'))
        elif (phrase[x] >= 'a' and phrase[x] <= 'z'):
            new = new + chr((ord(phrase[x]) - ord('a') + n)%26 + ord('a'))
        else:
            new = new + phrase[x]
        x=x+1
    return new

def rotencrypt(phrase):
    x=0
    while x <= 26:
       print rotX(phrase,x)
       x=x+1
rotencrypt("deoh")
rotencrypt("ufwyd")
rotencrypt("udm")

i = 0
while i < 27:
    print rotX("Cnebnl Vtxltk bl max uxlm unm fr ykbxgw ebdxl Gtihexhg uxmmxk yhk patmxoxk kxtlhg. Ha pxee. Max yetz bl xtlrvmy{Gti0exhg_ol_Vt3l4k}",-i)
    i=i+1
