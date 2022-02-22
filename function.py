
# verification de la validité du numéro d'étudiant
def num(c):
    r = False
    number = [str(i) for i in range(10)]
    if len(c) == 7 :
        if c.isupper() and c.isalnum():
            for elem in c:
                if elem in number:
                    r = True
                    break             
    else: 
        r = False
    return r            

# Calcul de la moyenne des devoir

def moy(liste):
    s = 0
    n = len(liste)
    for k in range(0,n):
        s = s + int(liste[k])
    return s/n

# verification de la validité du nom d'étudiant
def valide_nom(prenom, nom):
    n = 0
    m = 0
    if (prenom[0].isalpha and nom[0].isalpha):
        for n in nom:
            if n.isalpha:
                n += 1
        for p in prenom:
            if p.isalpha:
                m += 1
        if n >= 2 and m >= 3:
            return True
    else:    
        return False
    

# formatage de la date 
def date(chaine):
    separator = "/-.,:;_- @]{çà#]}'"
    mois = {"ja":"1","f":"2", "mars":"3", "av":"4", "mai":"5", "juin":"6", 
            "juil":"7", "ao":"8", "sep":"9", "oct":"10", "nov":"11", "dec":"12"}
    chaine = chaine.strip()
    for elem in chaine:
        if elem in separator:
            chaine = chaine.replace(elem, "/")
    chaine = chaine.split("/")  
    chaine = [chaine[i] for i in range(len(chaine)) if len(chaine[i]) != 0]
    for keys in mois:
        if str(chaine[1].lower()).startswith(keys):
            chaine[1] = mois[keys]
            break
    return "/".join(chaine)



# verification de la validité de la classe
def classe(chaine):
    chaine = chaine.strip()
    if len(chaine) == 0:
        return False
    else:
        if chaine[0] in [str(i) for i in range(3,7)] and chaine[-1] in ["A", "B"]:
            return True
        else:
            return False

def note_verification(n):
    char = ":;"
    sep = "# "
    sequence = n
    n = n.replace(",",".")
    for elem in n:
        if elem in char:
            n = n.replace(elem, ",")
    for elem in n:
            if elem in sep:
                n = n.replace(elem, "")
    n = (" ").join(n.split("["))
    n = (" ").join(n.split("]"))
    n = n.split()
    if len(n) % 2 == 0:
        dictionnaire = {n[i]: [(n[i + 1])] for i in range(0, len(n), 2)}
        dic = {}
        for mat in dictionnaire:
            s = dictionnaire[mat]
            # s1 = dictionnaire['la moyenne est :'] = moy(mat)
            dic[mat] = [e for e in ("").join(s).split(",")if e != '']
        return dic
    else:       
        return sequence
    

## Validité d'une date
def verify_date(c):
    c = c.strip()
    if len(c) == 0:
        return False
    else:
        c = c.split("/")
        # Condition de validité de la date 
        # avec si on a pas un jour superieur à 31 et inferieur à 1 etc...
        if int(c[0]) < 1 or int(c[0]) > 31 or int(c[1]) < 1 or int(c[1]) > 12 or ((c[1] == 2) and (int(c[0]) > 29) and (
            (int(c[2])% 4 == 0 and int(c[2]) % 100 != 0) or int(c[2]) % 400 == 0)) or (
            (int(c[1]) == 2) and (int(c[0]) > 28) and ((int(c[2]) % 4 != 0 or int(c[2]) % 100 == 0) and int(c[2]) % 400 != 0)):
            return False
        return True
        
        
        
# Fonction pour verifier si un chaine contient une lettre
def lettre(chaine):
    p=0
    for elem in range(len(chaine)):
        if chaine[elem].isalpha():
            p+=1
    if p >= 1:
        return True
    else:
        return False
    

def verf(num):
    p = 0
    for elem in num:
        if elem == ".":
            p += 1
    if p >= 2:
        return True
    else:
        return False