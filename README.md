Github
username: KaixiangYang6
user email: kaixiang.yang.work@gmail.com

Installing Git
For Mac: https://git-scm.com/download/mac
For Win: https://git-scm.com/download/win
从https://code.visualstudio.com/ 下载Visual Studio Code，并安装。在左边栏extensions安装GitLens插件辅助显示文件目录

名词概念
repository  仓库。用于存储项目文件的地方
branch		分支。项目除主分支外，允许多个分支同时工作，审核通过的内容才会被合并进主分支。
commit 提交
pull
push
request
merge

从本地同步到云端时候，在终端输入账户名和密码时，需要的密码实际是personal access token个人身份牌。令牌在settings--Developer settings--Personal access tokens--Generate new token

在远端新建repository，在绿色按钮Code的下拉选项里，复制HPPTS，将其作为$ git remote add origin https://github.com/KaixiangYang6/For-Self-Learning-Python.git 命令中

Basic Commands in Terminal.app for Git
git命令参考：https://git-scm.com/docs/gittutorial
$ git —version 				Check Current Version
$ git init 						Initialize Local Git Repository.在本地文件夹执行$ git init之后，会出现git隐藏文件夹（打开系统的隐藏模式才能看到）。同时将使用master作为初始分支名称。

$ git config —global user.name “Name”
$ git config —global user.email “Email”
$ git add <filename> 			Add Files To The Staging area
	folder: “name/“			Add Folder
	*.html					Add All HTML files 
$ git add .					Add Everything
$ git add -a					Add Everything
$ git rm —cached filename	Remove File from The Staging area
$ git status 					Check Status of Working Tree
$ git commit					Commit Changes In Index
	提交后可以直接按I去修改命名，然后按Esc，再输入:wq退出修改模式
$ git commit -a		Automatically notice any modified (but not new) files, add them to the index, and commit, all in one step.
$ gut commit -m “本次上传的注释”		提交并跳过整个编辑步骤
$ git reset HEAD^1			重新定向到当前提交的上一个提交上
$ git log						give a history of commits

$ git checkout <commit-hash>	go back to one commit point by commit-hash in the commit history
$ git push					Push To Remote Repository
$ git pull						Pull Lastest From Remote Repository
$ git clone					Clone Repository Into A New Directory
$ git branch					List all existing branches
	experimental
	* master					The asterisk marks the branch you are currently on;
$ git branch <name>			Create a Branch
$ git branch -d <name>		Delate the branch
$ git branch -m h<name>		Rename the branch. 本地仓库分支命名需要与远端仓库分支保持命名一致

$ git switch <experimental>	Switch to the experimental branch
$ git checkout <branch name>	Switch To Another Branch
$ git checkout <file name>	Switch To Original Status of the file
$ git checkout -b <branch name>	以当前分支为基础新建分支
$ git merge <branch name> 	将分支合并进当前master分支
$ git merge —abort			放弃当前合并动作
$ git remote					List The Remote Repository We Have Now
$ git remote add original https://github.com/KaixiangYang6/For-Self-Learning-Python.git 将已创建好的远端仓库添加到本地git中文件夹，成功后输入$ git remote将返回origin（目前存在的库）
$ git push -u origin master	将当前origin master分支推到云端



$ touch XXX.js	create a JS file
$touch .gitignore				创建一个文件名清单，其包含的文件将不会被git同步
	/文件夹名称	
$ clear			清空窗口


