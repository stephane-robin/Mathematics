# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:32:52 2017

@author: Stephane Robin
lobster_library
"""
import sqlite3
conn = sqlite3.connect('lobster_db.db')
curseur = conn.cursor()
# LIBRARY
lettreChiffre = {'a':'100','b':'131','c':'132','d':'103','e':'134','f':'105',
                 'g':'136','h':'107','i':'138','j':'109','k':'110','l':'111',
                 'm':'112','n':'113','o':'114','p':'115','q':'116','r':'137',
                 's':'148','t':'119','u':'120','v':'141','w':'122','x':'133',
                 'y':'124','z':'125','A':'200','B':'231','C':'242','D':'203',
                 'E':'234','F':'205','G':'236','H':'247','I':'238','J':'209',
                 'K':'210','L':'211','M':'212','N':'213','O':'214','P':'215',
                 'Q':'216','R':'257','S':'248','T':'219','U':'220','V':'241',
                 'W':'282','X':'263','Y':'224','Z':'245','#':'301','-':'312',
                 '_':'303','@':'304','.':'305','0':'320','1':'321','2':'322',
                 '3':'323','4':'324','5':'325','6':'326','7':'327','8':'328',
                 '9':'329'}     
chiffreLettre = {'100':'a','131':'b','132':'c','103':'d','134':'e','105':'f',
                 '136':'g','107':'h','138':'i','109':'j','110':'k','111':'l',
                 '112':'m','113':'n','114':'o','115':'p','116':'q','137':'r',
                 '148':'s','119':'t','120':'u','141':'v','122':'w','133':'x',
                 '124':'y','125':'z','200':'A','231':'B','242':'C','203':'D',
                 '234':'E','205':'F','236':'G','247':'H','238':'I','209':'J',
                 '210':'K','211':'L','212':'M','213':'N','214':'O','215':'P',
                 '216':'Q','257':'R','248':'S','219':'T','220':'U','241':'V',
                 '282':'W','263':'X','224':'Y','245':'Z','301':'#','312':'-',
                 '303':'_','304':'@','305':'.','320':'0','321':'1','322':'2',
                 '323':'3','324':'4','325':'5','326':'6','327':'7','328':'8',
                 '329':'9'}  

# METHODES
def encodage(phrase):
    """use the library lettreChiffre, transform a string of characters without
       blank into a string of code without blank,
       rsa public key(391,47) private key(391,15)"""
    code = ''
    for i in phrase:
        lettre = int(lettreChiffre[i])
        chiffre = str((lettre**47)%391)
        code += chiffre
    return code

def decodage(code):
    """use the library chiffreLettre, transform a string of code without blank
       into a string of characters without blank, select digits 3 by 3 in the
       string of code"""
    phrase = ''
    tab = []
    while code:
        tab.append(code[:3])
        code = code[3:]
    for i in tab:
        i = int(i)
        chiffre = str((i**15)%391)
        lettre = chiffreLettre[chiffre]
        phrase += lettre
    return phrase

def testExistenceCompany(ins_company):
    """test if a company name is already in the table enregistrement_mp,
       ins_company is already encrypted, return a boolean"""
    bool = False
    curseur.execute("""SELECT company FROM enregistrement_mp""")
    requete = curseur.fetchall()
    # compare all company names of the table with ins_company
    for value in requete:
        if value[0]==ins_company:
            bool = True
    return bool

def inserer(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder):
    """insert an item in the table enregistrement_mp, the fields are already encrypted"""
    curseur.execute("""INSERT INTO enregistrement_mp(company,category,identifiant,mp,association,mp_finder) VALUES(?,?,?,?,?,?)""",(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder))
    conn.commit()
    
def consulter():
    """consult the whole table enregistrement_mp, decrypt the fiels of each item
       return a list of items"""
    compteur = 0
    chaineConsulter = ''
    listeConsulter = [['id','company','category','identifiant','mp','association','mp_finder']]
        
    curseur.execute("""SELECT id,company,category,identifiant,mp,association,mp_finder FROM enregistrement_mp""")
    requete = curseur.fetchall()
    for value in requete:
        compteur += 1
        listeConsulter.append([value[0],decodage(value[1]),decodage(value[2]),decodage(value[3]),decodage(value[4]),decodage(value[5]),decodage(value[6])])
    
    for i in range(0,compteur+1):
        for j in range(1,6):
            chaineConsulter += listeConsulter[i][j]+','
        chaineConsulter = chaineConsulter+'\n'
    return chaineConsulter   
   
def maj(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder):
    """update an item in the table enregistrement_mp, the fields are already encrypted"""
    curseur.execute("""UPDATE enregistrement_mp SET company=?,category=?,identifiant=?,mp=?,association=?,mp_finder=? WHERE id=?""",(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder,value[0]))
    conn.commit()
    
def supprimer(ins_id):
    """delete an item in the table enregistrement_mp, the id is not encrypted"""
    curseur.execute("""DELETE FROM enregistrement_mp WHERE id=?""",(ins_id,))
    conn.commit()
