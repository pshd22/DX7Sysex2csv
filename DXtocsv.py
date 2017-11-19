# -*- coding: latin-1 -*-

"""
    Ceci est un module qui va convertir 
    un fichier sysex DX7 en un fichier csv.
"""

import os
from pathlib import Path
import csv
import array

def count_file(path):
    i=0
    for p in  Path(path).glob('./**/*'):
        if p.is_file():
            i=i+1
    print('nombre de fichier : ',i)

def RC_LC(record):
    RC_LC = []
    print("\n----------------------------------")
    print (record)
    d = int('00011100',2) & record
    rotd = d>>2       
    RC_LC.append(rotd)     
    d = int('00000011',2) & record
    RC_LC.append(d)    #print (valeur)
    return (RC_LC)  

def PD_RS(record):
    PD_RS = []
    print (record)          
    d = int('01111000',2) & record
    rotd = d>>3       
    PD_RS.append(rotd)     
    d = int('00000111',2) & record
    PD_RS.append(d) 
    return (PD_RS)

def KVS_AMS(record):
    KVS_AMS = []
    print (record)          
    d = int('00011100',2) & record
    rotd = d>>2       
    KVS_AMS.append(rotd)     
    d = int('00000011',2) & record
    KVS_AMS.append(d)
    return(KVS_AMS)

def FC_M(record):
    FC_M = []
    d = int('00111110',2) & record
    rotd = d>>1       
    FC_M.append(rotd)     
    d = int('00000001',2) & record
    FC_M.append(d)
    return (FC_M)

def ALS(record):
    ALS = []
    d = int('00011111',2) & record
    ALS.append(d)
    return (ALS)

def OKS_FB(record):
    OKS_FB = []
    d = int('00001000',2) & record
    rotd = d>>3       
    OKS_FB.append(rotd)     
    d = int('00000111',2) & record
    OKS_FB.append(d)
    return (OKS_FB)

def LPMS_LFW_LFKS(record):
    LPMS_LFW_LFKS = []
    d = int('01110000',2) & record
    rotd = d>>4       
    LPMS_LFW_LFKS.append(rotd)
    d = int('00001110',2) & record
    rotd = d>>2       
    LPMS_LFW_LFKS.append(rotd)      
    d = int('00000001',2) & record
    LPMS_LFW_LFKS.append(d)
    return (LPMS_LFW_LFKS)
   
def liste_fichier(path):    
   
    basse=(os.listdir(path))

    s=open('liste_fichier.txt','w')
    for fichier in basse :   
        f= open(path+fichier, "rb")
        record = f.read(7) #lit l'entête du message
        i=0
        while True:
            record = f.read(128)
            if len(record) != 128:
                break;
            # Do stuff with record
            print (record[117:127]) # nom du programme en ASCII
            s.write(record[117:127])
            s.write("\n")
            i=i+1
    f.close()
    s.close

#Début du programme

def convertir1(path,fichier):    
    # alimenter une dictionnaire de 32 listes de 155 paramètres et la retourner à la fonction appelante
    #utilisant les tableaux Array https://pymotw.com/3/array/
    
    patch = {
        'son 1':[],
        'son 2':[],
        'son 3':[],
        'son 4':[],
        'son 5':[],
        'son 6':[],
        'son 7':[],
        'son 8':[],
        'son 9':[],
        'son 10':[],
        'son 11':[],
        'son 12':[],
        'son 13':[],
        'son 14':[],
        'son 15':[],
        'son 16':[],
        'son 17':[],
        'son 18':[],
        'son 19':[],
        'son 20':[],
        'son 21':[],
        'son 22':[],
        'son 23':[],
        'son 24':[],
        'son 25':[],
        'son 26':[],
        'son 27':[],
        'son 29':[] ,       
        'son 30':[],
        'son 31':[],
        'son 32':[]
        }

 

    f= open(path+fichier, "rb")
    record = f.read(7)
    print ("les 7 octets de l'entête sont :",record[:7])
    i=0
    num_patch = 0
    # boucle alimentant chaque entree du dictionnaire avec des arrays, des 
    #listes ou des int correspondant au décodage des 128 octets du fichier en 
    # 155 valeurs
    while True:
        record = f.read(128)
        if len(record) != 128:
            break;
        # Do stuff with record
        record = array.array('b', record)
        print('As array      :', record)
        #print('As hex        :', binascii.hexlify(a))
        
        son=[]
        # operateur 6
        # 11 (RC, LC), 12 (PD, RS), 13 (KVS, AMS), 15 (FC, M) pour l'opérateur 6  
        son.append(record[0:11])
        son.append(RC_LC(record[11]))
        son.append(PD_RS(record[12]))
        son.append(KVS_AMS(record[13]))
        son.append(record[14])
        son.append(FC_M(record[15]))
        son.append(record[16])
        # operateur 5
        # 11+17 (RC, LC), 12+17 (PD, RS), 13 (KVS, AMS), 15 (FC, M) pour l'opérateur 5
        son.append(record[17:28])
        son.append(RC_LC(record[28]))
        son.append(PD_RS(record[29]))
        son.append(KVS_AMS(record[30]))
        son.append(record[31])
        son.append(FC_M(record[32]))
        son.append(record[33])       
        # operateur 4 
        # 11+34 (RC, LC), 12+34 (PD, RS), 13 (KVS, AMS), 15 (FC, M) pour l'opérateur 4
        son.append(record[34:45])
        son.append(RC_LC(record[45]))
        son.append(PD_RS(record[46]))
        son.append(KVS_AMS(record[47]))
        son.append(record[48])
        son.append(FC_M(record[49]))
        son.append(record[50])
        # operateur 3
        # 11+51 (RC, LC), 12+51 (PD, RS), 13 (KVS, AMS), 15 (FC, M) pour l'opérateur 3
        son.append(record[51:62])
        son.append(RC_LC(record[62]))
        son.append(PD_RS(record[63]))
        son.append(KVS_AMS(record[64]))
        son.append(record[65])
        son.append(FC_M(record[66]))
        son.append(record[67])
        # operateur 2
        # 11+68 (RC, LC), 12+68 (PD, RS), 13 (KVS, AMS), 15 (FC, M) pour l'opérateur 2
        son.append(record[68:79])
        son.append(RC_LC(record[79]))
        son.append(PD_RS(record[80]))
        son.append(KVS_AMS(record[81]))
        son.append(record[82])
        son.append(FC_M(record[83]))
        son.append(record[84])
        # operateur 1
        # 11+85 (RC, LC), 12+85 (PD, RS), 13 (KVS, AMS), 15 (FC, M) pour l'opérateur 1
        son.append(record[85:96])
        son.append(RC_LC(record[96]))
        son.append(PD_RS(record[97]))
        son.append(KVS_AMS(record[98]))
        son.append(record[99])
        son.append(FC_M(record[100]))
        son.append(record[101]) 

        son.append(record[102:110])
        # 110 (ALS)
        son.append(ALS(record[110]))
        # 111 (OKS, FB)
        son.append(OKS_FB(record[111]))
        son.append(record[112:116])
        # 116 (LPMS, LFW,LKFS)
        son.append(LPMS_LFW_LFKS(record[116]))
        son.append(record[117])
        son.append(record[118:127])

        # nom du programme en ASCII
        print('As byte string:', record[117:127])
        i=i+1
        #copy le son dans l'emplacement ad hoc du dictionnaire
        patch['son '+str(i)]=son[:]
        print (patch['son '+str(i)])
        num_patch= num_patch +1
 
    #A partir de ce point j'ai normalement les 32 sons dans les 32 listes du 
    #dictionnaire mais je galère pour écrire ces paramètres et le nom du son dans une ligne
    #importable dans un fichier csv :(
    j=len(patch['son 3'])
    k=0
    print ("transforme en liste")
    while k < j :
        print (type(patch['son 3'][k]))       
        k+=1
    #output.flush()
    for valeur in enumerate (patch['son 3']):
        print (valeur)

    f.close() 

if __name__ == '__main__':
      
    #mon environnement de développement est python 3.5 avec sublimetext sous Ubuntu
    #ou anaconda sous windows10, ce qui explique que les paths sont différents selon 
    #le PC sur lequel est pluggé la clé USB...
    
    path='/media/pascal/D8D2-CFD7/DX7/testpy/syx/'
    #path='F:\\DX7\\testpy\\syx\\'
    #path='F:\\DX7\\SynLib DX_TX (Marc Bareille)\\SynLib DX_TX (Marc Bareille)\\'
    #path='C:\\Users\\pascal\\Desktop\\DX7 TX7\\DX7_AllTheWeb\\'
    count_file(path) # calcul du nombre de fichier à convertir
    #liste_fichier(path)
    basse=(os.listdir(path))
    for fichier in basse :
        convertir1(path,fichier)
    print ("Conversion terminée")