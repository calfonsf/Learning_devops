# Intro

Version Control

Cuando se trabaja en equipo es conveniente tener el codigo en repositorios online para que se pueda acceder remotamente por todos los miembros del equipo.

Git guarda versiones por cada cambio, de manera que si exiten errores, es posible volver a una version anterior, de ahi version control

# Permite

- Mantener registro de los cambios en el codigo
- Sincronizar codigo entre varias personas
- Probar cambios entre varias personas sin perder el original
- Revertir a una version anterior

# Git Repos:

- GitHub: better for devs.
- Gitlab: better for admins.
- Existen tambien repos locales Ej: local Gitlab, Bitbucker, ...

# Git clone

git clone permite descargar una copia local de un repositorio 

>git clone https://github.com/calfonsf/CS50w.git


Usualmente hay dos metodos: 

- https + user + password
- ssh + ssh-key

# Git add & rm

anade archivos que seran salvados en el proximo comit

>git add .\git-test.html

retira archivos que seran salvados en el proximo comit

>git rm .\git-test.html

# Git commit

Permite salvar los archivos a git

Vscode pide: git config --global user.email "calfonsf@gmail.com", si no te gusta usa ssh

>git commit -m "mi mensaje"

# Git status

Reporta el estado actual

>git status

# Git push

Permite subir al repo los commits

>git push

# Git pull

Actualiza el repo local a la ultima version online

>git pull

# Git init

Permite especificar a git que el directorio actual es un repositorio de git (creando )

>git init

# Merge Conflicts 

Problemas que surgen cuando varias persona hacen modificaciones que se contradicen

# Git log 

Permite seguir todos tus commits

>git log

# Gt reset

>git reset --hard `<comit>`

>git reset --hard origin/master

# Create new repository

> git init

# Add Git remote repository

>git remoite add origin { repo name http or ssh}

>git push -u origin main 

# Branches

## Problem to solve

Si seguimos un camino lineal y existe algun bug se crearia una situacion en la que para arreglar el bug seria necesario perjudicar el desarrollo de las nuevas "features" que vallan surgiendo

![[Pasted image 20230818231708.png]]

## Solution 

![[Pasted image 20230818231804.png]]

## Git branch

Permite conocer en que branch estas

>git branch

renombrar branch actual a otro nombre

>git branch -N main

## Git Checkout

Permite cambiar de branch

-b -> nueva rama

>git checkout -b style

cambiar a rama master

>git checkout master

# Git merge 

Hace merge a excepcion de que exista un merge conflict

# Forking

Clonar un repositorio de algun proyecto de codigo abierto, en caso que se quiera contribuir puedes hacer un pull request

# Github pages

This is hosting Github offers for static content

# .gitignore

Archivo que permite expecificar archivos en un repositorio

Ex 

> code .gitignore

```gitignore
mycontrasena.txt
secretfile.md
randomshit.py
```

