# Mise en place d’une pipeline de CI/CD


### 1.  Création vous un compte Github
 * Compte Github : déja créé [@otmane047](https://github.com/otmane047)

 * generation d’une clé SSH
```bash
ssh-keygen -t ed25519 -C "otmane047@gmail.com"
cat ~/.ssh/id_ed25519.pub
```
* Et apres je l'ai ajouté dans mon compte Github dans les paramètres SSH and GPG keys

### 2. Tester un premier workflow GitHub Actions
    * Compte Github : déja créé [Repo Github](https://github.com/otmane047/tp_cicd)
    * Créer un fichier `.github/workflows/github-actions-demo.yml` dans le repo
 
 ### 3. Créer deux classes python, SimpleMath et TestSimpleMath

    * J'ai créé la classe `SimpleMath` dans le fichier `simple_math.py` avec une méthode `add` qui additionne deux entiers.
    * J'ai créé la classe `TestSimpleMath` dans le fichier `test_simple_math.py` pour tester la méthode `add`.

### 4. Workflow de tests unitaires

    * J'ai ajouté un fichier `requirements.txt` avec les dépendances nécessaires, comme `unittest`.
    
    * J'ai créé le fichier `.github/workflows/test.yml`

###  5: Ajout de la soustraction
    * J'ai ajouté la méthode `subtract` dans la classe `SimpleMath` pour soustraire deux entiers.
    * J'ai modifié le fichier `test_simple_math.py` pour inclure des tests pour la méthode `subtract`.

### 6: Ajout du linting avec pylint
    * J'ai ajouté run step pour installer `pylint`.
    * J'ai ajouter un lint Job dans `test.yml` pour exécuter `pylint` sur le code Python.