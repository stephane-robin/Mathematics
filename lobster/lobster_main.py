# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:32:52 2017

@author: Stephane Robin
lobster_main
"""

# IMPORT PACKAGES
#import lobster_library
import sqlite3
import tkinter

# CONNECTION TO DATABASE SQLITE lobster_db
# connection
conn = sqlite3.connect('lobster_db.db')
# creation of a cursor
curseur = conn.cursor()
# creation of the table enregistrement_mp if not exists
#curseur.execute("""CREATE TABLE IF NOT EXISTS enregistrement_mp(
#id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#company TEXT,
#category TEXT,
#identifiant TEXT,
#mp TEXT,
#association TEXT,
#mp_finder TEXT)""")
#conn.commit()
        
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

# CONSTANTS
COULEURFOND = '#93c59b'  
COULEURBOUTON = '#85CDC3'
# METHODES
# encryption
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

# decryption
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

def consulter():
    """consult the whole table enregistrement_mp, decrypt the fiels of each item
       display a string of items"""
    compteur = 0
    chaineConsulter = ''
    listeConsulter = [['id','company','category','identifiant','mp','association','mp_finder']]
    curseur.execute("""SELECT id,company,category,identifiant,mp,association,mp_finder FROM enregistrement_mp""")
    requete = curseur.fetchall()    
    for value in requete:
        compteur += 1
        listeConsulter.append([value[0],value[1],value[2],value[3],value[4],value[5],value[6]])
    for i in range(0,compteur+1):
        for j in range(1,6):
            chaineConsulter += listeConsulter[i][j]+'   //   '
        chaineConsulter = chaineConsulter+'\n'
    messageResultat = tkinter.Label(fenetre,text=chaineConsulter,bg=COULEURFOND,justify="left")
    messageResultat.pack()

def appuiInserer():
    """insert an item in the table enregistrement_mp, the fields are already encrypted"""
    # input the fields of the item
    # encrypt the fields
    util_company = tkinter.StringVar()
    #insCompany = encodage(newCompany)
    afficherCompany = tkinter.Label(fenetre,text='Company : ',bg=COULEURFOND,justify='left')
    afficherCompany.pack()
    saisieCompany = tkinter.Entry(fenetre,textvariable=util_company,width=30)
    saisieCompany.pack()
    #
    util_category = tkinter.StringVar()
    #insCategory = encodage(newCategory)
    afficherCategory = tkinter.Label(fenetre,text='Category : ',bg=COULEURFOND,justify='left')
    afficherCategory.pack()
    saisieCategory = tkinter.Entry(fenetre,textvariable=util_category,width=30)
    saisieCategory.pack()
    #
    util_identifiant = tkinter.StringVar()
    #insIdentifiant = encodage(newIdentifiant)
    afficherIdentifiant = tkinter.Label(fenetre,text='User Name : ',bg=COULEURFOND,justify='left')
    afficherIdentifiant.pack()
    saisieIdentifiant = tkinter.Entry(fenetre,textvariable=util_identifiant,width=30)
    saisieIdentifiant.pack()
    #
    util_mp = tkinter.StringVar()
    #insMp = encodage(newMp)
    afficherMp = tkinter.Label(fenetre,text='Password : ',bg=COULEURFOND,justify='left')
    afficherMp.pack()
    saisieMp = tkinter.Entry(fenetre,textvariable=util_mp,width=30)
    saisieMp.pack()
    #
    util_association = tkinter.StringVar()
    #insAssociation = encodage(newAssociation)
    afficherAssociation = tkinter.Label(fenetre,text='Associated information : ',bg=COULEURFOND,justify='left')
    afficherAssociation.pack()
    saisieAssociation = tkinter.Entry(fenetre,textvariable=util_association,width=30)
    saisieAssociation.pack()
    #
    util_finder = tkinter.StringVar()
    #insFinder = encodage(newFinder)
    afficherFinder = tkinter.Label(fenetre,text='How to remember the password : ',bg=COULEURFOND,justify='left')
    afficherFinder.pack()
    saisieFinder = tkinter.Entry(fenetre,textvariable=util_finder,width=30)
    saisieFinder.pack()
    
    btnValiderInserer = tkinter.Button(fenetre,text="Valider",bg=COULEURBOUTON,width=120,cursor="circle",command=lambda: inserer(util_company.get(),util_category.get(),util_identifiant.get(),util_mp.get(),util_association.get(),util_finder.get()))
    btnValiderInserer.pack(side="bottom",padx=200,pady=20)    
    
def inserer(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder):
    """test of the company name to insert, if it is already in the table then cancel
       else insert item in the table"""
    bool = testExistenceCompany(ins_company)
    if(bool==True):
        print('This company name already exists in the file. Please proceed again choosing another name')
    else:
        curseur.execute("""INSERT INTO enregistrement_mp(company,category,identifiant,mp,association,mp_finder) VALUES(?,?,?,?,?,?)""",(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder))
        conn.commit()
        
def appuiSupprimer():
    """choose the item to delete, confirm the item to delete or cancel"""
    #insCompany = encodage(newCompany)
    # display all table enregistrement_mp
    afficherMessage = tkinter.Label(fenetre,text='Please choose the company to be deleted from the file \n',bg=COULEURFOND,justify='left')
    afficherMessage.pack()
    consulter()
    # input company name to delete from the table
    util_company = tkinter.StringVar()
    saisieCompany = tkinter.Entry(fenetre,textvariable=util_company,width=30)
    saisieCompany.pack()
    # confirm deletion
    afficherConfirmerSupprimer = tkinter.Label(fenetre,text='Confirm deleting '+util_company.get(),bg=COULEURFOND,justify='left')
    afficherConfirmerSupprimer.pack()
    btnDelete = tkinter.Button(fenetre,text="Delete",bg=COULEURBOUTON,cursor="circle",command=lambda: supprimer(util_company.get()))
    btnDelete.pack(side="left",padx=5,pady=5)
    btnCancel = tkinter.Button(fenetre,text="Cancel",bg=COULEURBOUTON,cursor="circle",command=lambda: consulter())
    btnCancel.pack(side="left",padx=5,pady=5)    
    
def supprimer(ins_company):
    """delete selected item from the table enregistrement_mp"""
    curseur.execute("""DELETE FROM enregistrement_mp WHERE company=?""",(ins_company,))
    conn.commit()

def appuiMaj():
    """choose the item to update, confirm the item to update or cancel"""
    # display all table enregistrement_mp
    afficherMessage = tkinter.Label(fenetre,text='Please choose the company to update \n',bg=COULEURFOND,justify='left')
    afficherMessage.pack()
    consulter()
    # input company name to update
    util_company = tkinter.StringVar()
    saisieCompany = tkinter.Entry(fenetre,textvariable=util_company,width=30)
    saisieCompany.pack()
    # confirm update
    afficherConfirmerMaj = tkinter.Label(fenetre,text='Confirm deleting '+util_company.get(),bg=COULEURFOND,justify='left')
    afficherConfirmerMaj.pack()
    btnMaj = tkinter.Button(fenetre,text="Delete",bg=COULEURBOUTON,cursor="circle",command=lambda: maj(util_company.get()))
    btnMaj.pack(side="left",padx=5,pady=5)
    btnCancel = tkinter.Button(fenetre,text="Cancel",bg=COULEURBOUTON,cursor="circle",command=lambda: consulter())
    btnCancel.pack(side="left",padx=5,pady=5) 
    
def maj(ins_company):   
    bool = testExistenceCompany(ins_company)
    if(bool==True):
        print('This company name already exists in the file. Please proceed again choosing another name')
    else:
        maj(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder)
      
   
        # if the update concerns the company name, make sure the new company name
        # is not already in the table then update, else don't ask for the company name
        # and update
       
        # input the fields of the item
        # encrypt the fields
        ins_category = input('category')
        ins_category = encodage(ins_category)
        ins_identifiant = input('identifiant')
        ins_identifiant = encodage(ins_identifiant)
        ins_mp = input('mot de passe')
        ins_mp = encodage(ins_mp)
        ins_association = input('association')
        ins_association = encodage(ins_association)
        ins_finder = input('finder')
        ins_finder = encodage(ins_finder)
        
        if(changeName=='y'):
            ins_company = input('company')
            ins_company = encodage(ins_company)
            # test of the new company name, if it is already in the table then cancel
            # else update item in the table
            bool = testExistenceCompany(ins_company)
            if(bool==True):
                print('This company name already exists in the file. Please proceed again choosing another name')
            else:
                maj(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder)
        else:
            maj(value[1],ins_category,ins_identifiant,ins_mp,ins_association,ins_finder)

  
def maj(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder):
    """update an item in the table enregistrement_mp, the fields are already encrypted"""
    curseur.execute("""UPDATE enregistrement_mp SET company=?,category=?,identifiant=?,mp=?,association=?,mp_finder=? WHERE id=?""",(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder,value[0]))
    conn.commit()

"""def ecrire(texteResultat):
    messageResultat = tkinter.Label(fenetre,text=texteResultat,bg=couleurFond,justify="left")
    messageResultat.pack()"""
    

# MAIN PROCEDURE

#chaineConsulter = appuyerConsulter()

# create main window
fenetre = tkinter.Tk()
fenetre.title('Lobster 1.0')
fenetre.geometry('880x620')
fenetre.configure(bg=COULEURFOND)
# explane the app
messageExplication = tkinter.Label(fenetre,text='Lobster password manager stores your information and displays it on request.\nPlease choose an option bellow:',bg=COULEURFOND,justify='left')

"""valeur = 'coucou'

valeur = tkinter.StringVar()
saisie = tkinter.Entry(fenetre,textvariable=valeur,width=30)
btnValider = tkinter.Button(fenetre,text="Valider",bg="#85CDC3",width=120,cursor="circle",command=lambda: ecrire(valeur))
btnValider.pack(side="bottom",padx=200,pady=20)"""
# display buttons consult, insert, delete, update, cancel
btnConsulter = tkinter.Button(fenetre,text="Consult",bg="#85CDC3",cursor="circle",command=lambda: consulter())#ecrire(chaineConsulter))
btnInserer = tkinter.Button(fenetre,text="Insert",bg="#85CDC3",cursor="circle",command=lambda: appuiInserer())
btnMaj = tkinter.Button(fenetre,text="Update",bg="#85CDC3",cursor="circle",command=lambda: ecrire(''))
btnSupprimer = tkinter.Button(fenetre,text="Delete",bg="#85CDC3",cursor="circle",command=lambda: appuiSupprimer())
btnAnnuler = tkinter.Button(fenetre,text="Cancel",bg="#85CDC3",cursor="circle",command=lambda: ecrire(''))

btnConsulter.pack(side="left",padx=5,pady=5)
btnInserer.pack(side="left",padx=5,pady=5)
btnMaj.pack(side="left",padx=5,pady=5)
btnSupprimer.pack(side="left",padx=5,pady=5)
btnAnnuler.pack(side="left",padx=5,pady=5)
messageExplication.pack()

fenetre.mainloop()

# TO BE ERASED
bouton = input('What do you want to do ?')
   

# update the table enregistrement_mp
if bouton=='maj':
    # choose the item to update, confirm the item to update or cancel
    curseur.execute("""SELECT company FROM enregistrement_mp""")
    requete = curseur.fetchall()
    print('Here are the different companies whose information you can update:')
    for value in requete:
        print(decodage(value[0]))
    ins_company = input('Please choose the company you would like to update from the file')
    ins_company = encodage(ins_company)
    curseur.execute("""SELECT id,company,category,identifiant,mp,association,mp_finder FROM enregistrement_mp WHERE company=?""",(ins_company,))
    requete = curseur.fetchall()
    print('You chose to update the following company:')
    print('id / company / category / identifiant / mp / association / mp_finder')
    for value in requete:
        print(value[0],' : ',decodage(value[1]),' , ',decodage(value[2]),' , ',decodage(value[3]),' , ',decodage(value[4]),' , ',decodage(value[5]),' , ',decodage(value[6]))
    confirmation = input('Are you sure you want to update the selected item ? (y/n)')
    
    if confirmation=='y':
        # if the update concerns the company name, make sure the new company name
        # is not already in the table then update, else don't ask for the company name
        # and update
        changeName = input('Do you want to change the company name? (y/n)')
        # input the fields of the item
        # encrypt the fields
        ins_category = input('category')
        ins_category = encodage(ins_category)
        ins_identifiant = input('identifiant')
        ins_identifiant = encodage(ins_identifiant)
        ins_mp = input('mot de passe')
        ins_mp = encodage(ins_mp)
        ins_association = input('association')
        ins_association = encodage(ins_association)
        ins_finder = input('finder')
        ins_finder = encodage(ins_finder)
        
        if(changeName=='y'):
            ins_company = input('company')
            ins_company = encodage(ins_company)
            # test of the new company name, if it is already in the table then cancel
            # else update item in the table
            bool = testExistenceCompany(ins_company)
            if(bool==True):
                print('This company name already exists in the file. Please proceed again choosing another name')
            else:
                maj(ins_company,ins_category,ins_identifiant,ins_mp,ins_association,ins_finder)
        else:
            maj(value[1],ins_category,ins_identifiant,ins_mp,ins_association,ins_finder)
    else:
        print('cancel action')

# BACKEND
def suppr_dev():
    curseur.execute("""DELETE FROM enregistrement_mp""")
    conn.commit()

def cons():
    curseur.execute("""SELECT id,company,category,identifiant,mp,association,mp_finder FROM enregistrement_mp""")
    requete = curseur.fetchall()
    print('id / company / category / identifiant / mp / association / mp_finder')
    for value in requete:
        print(value[0],' : ',value[1],' , ',value[2],' , ',value[3],' , ',value[4],' , ',value[5],' , ',value[6])

    
