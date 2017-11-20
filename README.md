# DX7Sysex2csv
Convert sysex file of 32 sounds from DX/TX7 to a csv files of 32 lines and 155 colomns of parameters for statistics and more... 

3 fichiers de test contenant 32 sons sont dans le répertoire syx.
Chaque fichier correspond à un ensemble de 32*128 octets précédé d'un entête de 7 octets.
La description des 128 octets est dans le document Parametre de son.png sous forme de tableau. La description du message est dans le document format message sysex.png. Ces deux tableaux sont extraits du document TX7F1.pdf page 38 et 46.

Le codage des données midi est un codage "pénible" des données. Il peut être opportun d’avoir une base de référence avec un codage plus facile et lisible (xml, ASCII, …).

Le fichier xylophone.sound est un fichier au format XML qui est un exemple de fichier de sortie, les properties sont à adapter aux paramètres de son d'un DX. 

Dans tous les cas, je souhaite transformer ces messages au format binaire dans un format qui alimentera une base de référence (pas de doublons). A partir de cette base de référence je dois etre en mesure de les importer dans un tableur à des fins de  statistiques et des recherches multicritères dans des outils de type Big Data.   

Je débute en Python et donc je suis preneur de toutes suggestions qui me permettront d'atteindre cet objectif.

Merci à toi qui m'aidera ;)

