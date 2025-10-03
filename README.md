# Techzara Backend

Projet **Django + Django REST Framework + PostgreSQL** minimal pour démarrer rapidement.  
Ce backend expose une API sécurisée et extensible pour être consommée par le frontend et l’administration.

---

## Technologies
- Python 3.10+
- Django & Django REST Framework
- PostgreSQL
- psycopg (driver PostgreSQL)

---

## Prérequis
Vérifiez que vous avez installé :
```bash
python --version
psql --version
```

Si nécessaire :  
👉 [Télécharger Python](https://www.python.org/downloads/)  
👉 [Télécharger PostgreSQL](https://www.postgresql.org/download/)  

---

## Installation rapide

### 1. Cloner le projet
```bash
git clone https://github.com/Techzara-Team/techzara-backend.git
cd techzara-backend
```

### 2. Créer et activer un environnement virtuel
```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations initiales (Assurer vous d'avour configurer la base de données avant de faire ca)
```bash
python manage.py migrate
```

### 5. Lancer le serveur de développement
```bash
python manage.py runserver
```

---

## Configuration PostgreSQL

### 1. Installer le driver PostgreSQL
```bash
pip install psycopg[binary]
```

### 2. Se connecter à PostgreSQL
```bash
sudo -u postgres psql
```

### 3. Créer un utilisateur
```sql
CREATE USER techzara WITH PASSWORD 'mon_mot_de_passe';
```

### 4. Créer une base de données
```sql
CREATE DATABASE techzara_db OWNER techzara;
```

### 5. Donner les droits à l’utilisateur
```sql
GRANT ALL PRIVILEGES ON DATABASE techzara_db TO techzara;
```

### 6. Quitter PostgreSQL
```bash
\q
```

---

## Migrations spécifiques

### Générer les migrations de l’app `accounts`
```bash
python manage.py makemigrations accounts
```

### Appliquer toutes les migrations
```bash
python manage.py migrate
```

---

✅ À ce stade, votre backend Django est installé, connecté à PostgreSQL et prêt à être utilisé.

### Vérifier si Snap est installé:
```bash
snap --version

```
### Sinon, installe Snap :
```bash
sudo apt update
sudo apt install snapd
```

### Installer Postman via Snap :
```bash
  sudo snap install postman

```

✅ N.B: N'oublier pas de pull le dépot avant de modifier ou ajouter d'autre fonctionnalités.






models\
  init.py
  model.py
      class User(AbstractUser):

      class reseauSociau(Model)


tache et à faire 

models et serializers

models -> relation membre (foreign key) done

à faire -> models autre table
views autre table

### Installer Pillow pour gérer le champ image :
```bash
  sudo snap install postman

```

```