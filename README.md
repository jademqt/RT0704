# SALUT
### setup
1. environnement virtuel python
2. ajouter "venv/\*" et "save/\*" dans .git/info/exclude
3. installer les librairies python

### dossiers
src : fichiers sources
www : fichiers pour la page web
save : fichiers json des videotheques

### docker
	1- aller dans le dossier docker
	2- "docker build -t *nom_du_conteneur* ./"
	3- attendre
	4- pour lancer: "docker run -itp 80:8001 *nom_du_conteneur*" 
