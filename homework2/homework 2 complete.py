# 1) Suppose your current working directory is ~/Desktop/classes/python_decal/. What command would allow you to navigate directly to ~/Desktop?
# - running "cd ../.." would go back two directories, leading to ~/Desktop 
#
# 2) What does ~/ mean?
# - ~/ implies you are in your home directory. 
#
# 3) What's the difference between and abolute and a relative path in your terminal?
# - Absolute is relative to the root directory, whereas relative is relative to the current working directory
#
# 4) What command would bring you back to your home directory?
# - Running "cd ~/" would bring you back to your home (root) directory 
#
# 5) If you called rm ./ in your current working directory, what would it do?
# - "rm ./" would remove all files in the current working directory, the "." denoting the current directory, and the "/" denoting all files within the directory 
#
# 6) In your current working directory, what does calling "git add" do? What about "git commit"? What about "git push"?
# - calling "git add <file>" adds a file from the current working directory into the staging area, "git commit" commits the files from "git add" into a separate staging area, where "git push" can then insert files from the second staging area to GitHub. 
#
# 7) Let's say you call "git add" in your current working directory and then "git status". What message would appear? What is it telling you? 
# - "git status" would tell you that the file you added is added to a staging area and ready to be committed.
#
# 8) What has been the most frustrating error or bug you've encountered in this class so far? How did you troubleshoot and resolve it?
# - When first learning how to use "git add", "git commit" and "git push", I used git commit without the "-m" flag, which pulled up a text editor, which i exited out of without saving. Afterwards, I couldn't use any of the 3 git commands. It was resolved in office hours by (I believe) directly terminating the git text editor process running in the background
#
# 9) How does cloning a repository differ from pulling from a repository?
# - With Minecraft as an analog, cloning a repository is like downloading Minecraft, while pulling from a repository is like updating Minecraft.
#
# 10) Tell me a fun fact!
# - Running "rm ./" deletes all files in the current working directory, meaning that if you run it in your root directory, you will delete everything on your computer without warning!
