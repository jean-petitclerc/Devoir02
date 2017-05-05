- File - New Project: Devoir02

- File- Settings - Project:Devoir02 - Project Interpreter
    - Create Virtual env

- Installe packages:
    - Flask
    - Flask-Script
    - Flask-SQLAlchemy

-  Github
    - New Repository
    - Devoir02 - Public - Create

- PyCharm
    - VCS - Enable Version control - Git
    - File - Settings - Version Control - github
        - Host: github.com
        - Login/password
    - Devoir02 (right-click) - Git - Repository - Remote
        - Pèse sur le + vert
        - Rentre ton lien github: https://github.com/ton-compte-github/Devoir02.git

- Faire un fichier .gitignore
    - Devoir02 (right-click) - new - .ignore file - gitignore - Generate
    - Change env/ pour venv/
    - Save - Close

- Faire le premier commit
    - Devoir02 - Git - Commit Directory...
    - Commit message: Initial commit
    - Commit and Push
    - Push

- Créer l'arborescence
    - app
        - config
        - data
        - static
        - templates

- Créer un fichier de config.py sour config/
    - New - Python file: config (.py est ajouté automatiquement)
    - Add dans git - Non (parce que ce fichier contient des secrets)
    - Ajouter le contenu

- Créer le fichier devoir02.py sous app/
    - New - Python file: devoir02
    - Add to git - Oui
    - Ajouter le contenu

- Créer le fichier index.html sous templates/
    - New - HTML File: index
    - Add to git - Oui
    - Ajouter le contenu

- Créer la base de données
    - Dans le bas, il y a Version Control, Python Console, Terminal, TODO - Pèse sur terminal
    - Tape python app/devoir02.py shell
        - from devoir02 import db
        - db.create_all()
        - (si pas d'erreur la BD est créée)
        - exit()

- Roule ton application (dans le même terminal):
    - Tape python app/devoir02.py runserver

- Ouvre un browser
    - http://127.0.0.1:5000

