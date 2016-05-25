# Demo: CLI

```bash
~ $ ls
Desktop     Documents   Downloads   Library     Movies      Music      Pictures
~ $ mkdir testfolder
~ $ ls
Desktop     Documents   Downloads   Library     Movies      Music      Pictures    testfolder
~ $ cd testfolder
~/testfolder $ ls
~/testfolder $ mkdir innerfolder
~/testfolder $ ls
innerfolder
~/testfolder $ cd innerfolder
~/testfolder/innerfolder $ ls
~/testfolder/innerfolder $ atom file.txt
~/testfolder/innerfolder $ ls
file.txt
~/testfolder/innerfolder $ cd ..
~/testfolder $ ls
innerfolder
~/testfolder $ cd ..
~ $ ls
Desktop     Documents   Downloads   Library     Movies      Music      Pictures    testfolder
~ $ cd testfolder/innerfolder
~/testfolder/innerfolder $ cd ..
~/testfolder $
~/testfolder $ atom program.py
~/testfolder $ ls
innerfolder	program.py
~/testfolder $ python program.py
Hello! This program ran!
~/testfolder $ cd ..
~ $ python testfolder/program.py
Hello! This program ran!
~ $ python testfolder/./program.py
Hello! This program ran!
~ $ cd testfolder/innerfolder
~/testfolder/innerfolder $ python ../program.py
Hello! This program ran!
~/testfolder/innerfolder $
```
