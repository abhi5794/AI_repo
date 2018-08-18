Git

1. version
    git --version

2. Initialize local repository
    git init

3. Add files to index
    git add <file>
	git add *.html
	git add . \\adds every file
		to ignore a set of files add them into the file .gitignore
			example of files in .gitignore
			log.txt
			/dir1 

4. Check status of working tree
    git status

5. Commit changes to index
    git commit -m 'comment'

6. Push to remote repository 
    `git push`
to add the first file 
	git remote
	git remote add origin https://github.com/abhi5794/gittut.git
	git remote
	git push -u origin master
This will add push the local to remote even when they are not in sync.
	git push origin +master 

	

7. Pull from remote repository
    git pull

8. Clone repository into a new directory
    git clone

9. adding name and email
git config --global user.name 'ABHIJITH KUMAR'
git config --global user.email 'mail4abhijithkumar@gmail.com'

10 .Removing files from a staging area
git rm --cache <file>

11. adding a branch
git branch <file>

12. switching to the branch
git checkout <branch_name>

13. merge to master
git merge <branch_name>

11. create file
touch file_name.format