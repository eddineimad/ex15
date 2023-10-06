Algorithme moyenne
Variables
        m , n1 , n2 , n3 : reel
        mention : chaine de caracteres
Debut
    ecrire(¨taper la 1ere note , 2eme note , 3eme note : ¨)
    lire(n1 , n2 , n3)    
    m <-- (n1 + n2 + n3)/3
    tantque n1>20 ou n1<0 faire
    ecrire("taper dans la 1ere note un nombre entre 0 et 20 : ")
    lire(n1)
    fin tantque
    tantque n2>20 ou n2<0 faire 
    ecrire(¨tapez dans la 2eme note un nombre entre 0 et 20 : ¨)
    fin tantque
    tantque n3>20 ou n3<0 faire 
    ecrire(¨taper dans la 3eme note un nombre entre 0 et 20 : ¨)    
    fin tantque
    si m>=16 alors
    mention <-- ¨tres bien¨
    sinon 
    si m>=14 et m<16 alors
    mention <-- ¨bien¨
    sinon
    si m>=12 et m<14 alors
    mention <-- ¨assez bien¨
    sinon 
    si m>=10 et m<12 alors
    mention <-- ¨passable¨
    sinon 
    mention <-- ¨insuffisant¨
    fin si 
    fin si 
    fin si 
    fin si 
    ecrire(¨la moyenne detudiant est : ",m," est : ",f)