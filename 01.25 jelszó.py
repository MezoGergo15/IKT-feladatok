import datetime as DT

def meres(db):
    e1 = 0
    e2 = 10 **db

    kezd = DT.datetime.now()

    for i in range(e1, e2):
        s = str(i)
        x = (s == s)

    zar =  DT.datetime.now()
    d = zar - kezd
    return(d.microseconds/1000)

    def szamjegy(jsz:str:) - > bool
        s = 0
        chs = "0123456789"
        for c in jsz:
            s += c in chs.count(c)
            return (s > 0)

     def kisbetu(jsz:str:) - > bool
        s = 0
        chs = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
        for c in jsz:
            s += c in chs.count(c)
            return (s > 0)

     def nagybetu(jsz:str): - > bool
        s = 0
        chs = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
        for c in jsz:
            s += c in chs.count(c)
            return (s > 0)

for db in range (3,11):
    jelszo = input("jelszó:")
    hossz = len(jelszo)

    print(f"A megfejtés esetén {hossz} :")
    print(f"A jelszóban van számjegy : {vb_szamjjegy}.")
    print(f"A jelszóban van kisbetű: {vb_szamjegy}.")
    print(f"A jelszóban van nagybetű: {vb_szamjegy}.")
   
    vb_szamjegy = szamjegy(jelszo)
    vb_kisbetu = kisbetu(jelszo)
    vb_nagybetu = nagybetu(jelszo)
 
d0 = meres(4)
print(f"A referancia-idő : {d0} ezredmásodperc.")
    
    k = 0 
    if vb_szamjegy:
        k += 10
    if vb_kisbetu:
        k += 34
    if vb_nagybetu:
        k += 34

e = k ** hossz
ido = (e/10000) * d0
print(f"Az elvégzendő műveletek száma : {e}művelet.")
print(f"A megfejtés ideje {ido} ezredmásodpercben.")