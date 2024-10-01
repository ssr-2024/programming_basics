# Repositories
## Was ist ein Repository?
Enthält:
- Dateien
- Revisionsverlauf (zum Nachvollziehen der Änderungen)
### Neues Repo in command Line erstellen
```cmd
echo "# hello-world" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Jonathan00R/hello-world.git
git push -u origin main
```
### Push von bereits existierendem Repo (im CMD)
```cmd
git remote add origin https://github.com/Jonathan00R/hello-world.git
git branch -M main
git push -u origin main
```
Änderungen auf dem remote Repo speichern:
```cmd
git commit 
git push
```
Wie bekommt jemand anders das auf sein eigenes Repo? Das Problem ist, dass eventuell beide unterschiedliche Versionen haben, diese müssen gemerged werden und es ist nicht genau klar wie das gemacht werden muss (bei Textdateien geht das gut, aber z.B. PowerPoints sind binäre Dateien, da ist es schwieriger)
<br>
Im Terminal:
```cmd
cd zum Ordner
git pull
```
## Eigene Branch erstellen
Unten links kann man auf die aktuelle Branch klicken und dann create new Branch. 

