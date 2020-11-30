### Doing git on terminal

1. **Initialising a repository:**

		git init

2. **Cloning a repository**

		git clone <https_link_to_repository>
		e.g. git clone https://github.com/vivekhsridhar/GitBasics.git

3. **Moving a file to the staging area:**
   - Stage changes to a single file
		
		git add <relative_filepath/filename>

   - Stage all new changes
		
		git add .

4. **Take a snapshot of currently staged files:**

		git commit -m "a message relavant to this snapshot"

5. **Undo changes made in a previous commit:**
   - Undo changes in specific commit without altering commit history

		    git revert <commit SHA-1>
	identifies changes made in specific commit, inverts it, and includes a second commit to reverse it

   - Undo changes by permanently deleting subsequent changes (alters commit history)

            git reset --hard <commit SHA-1>
	choosing the latest commit will remove all changes since (staged and unstaged)

6. **Send everything to the remote repository:**

		git push -u origin master