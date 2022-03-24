# Github

> user name: KaixiangYang6<br/>
> user email: kaixiang.yang.work@gmail.com

### Installing Git
> For Mac: https://git-scm.com/download/mac  
> For Win: https://git-scm.com/download/win  
> 从https://code.visualstudio.com/ 下载Visual Studio Code，并安装。在VS左边栏extensions安装GitLens插件辅助显示文件目录
<br/>

### 名词概念
repository  仓库。用于存储项目文件的地方  
branch		分支。项目除主分支外，允许多个分支同时工作，审核通过的内容才会被合并进主分支。  
commit 提交  
pull 将远端库内容更新到本地库  
push 将本地库内容推送到远端库  
request  
merge 将分支融合到主干  
> 从本地同步到云端时候，在终端输入账户名和密码时，需要的密码实际是personal access token个人身份牌。令牌在settings--Developer settings--Personal access tokens--Generate new token  

> 在远端新建repository，在绿色按钮Code的下拉选项里，复制HPPTS，将其作为$ git remote add origin https://github.com/KaixiangYang6/For-Self-Learning-Python.git 命令中的远端地址
<br/>

### Basic Commands For Git in Terminal.app 
git命令参考：https://git-scm.com/docs/gittutorial

`$ git —version` 				检查当前python版本  
`$ git init` 						初始化本地git仓库。在本地文件夹执行$ git init之后，会出现git隐藏文件夹（打开系统的隐藏模式才能看到）。同时将使用master作为初始分支名称。  
`$ git config —global user.name “Name”`登记账号  
`$ git config —global user.email “Email”`登记email。在log里可以看到是谁提交的  
`$ git add <file name>` 添加文件到暂存区  
`$ git add <folder name/>`添加文件夹到暂存区  
`$ git *.html`添加所有HTML文件到暂存区  
`$ git add .`**添加所有文件到暂存区**  
`$ git add -a`添加所有到暂存区  
`$ git rm —cached filename`从暂存区删除文件  
`$ git status`**查看工作区，暂存区文件状态**  
`$ git commit`提交修改。提交后可以直接按I去修改命名，然后按Esc，再输入:wq退出修改模式  
`$ git commit -a`自动检查任何改动的文件，添加到暂存区并提交，一键完成这几步工作。  
`$ gut commit -m “本次上传的注释”`**一键提交并注释**  
`$ git reset HEAD^1`重新定向到当前提交的上一个提交上  
`$ git log`**查看提交历史**  
`$ git checkout <commit-hash>`根据hash序列号返回到对应的提交时间点。  
`$ git push`**推送到远端仓库。本地没有远端新时，先pull再push**  
`$ git pull`**从远端仓库拉取最新版本**  
`$ git clone`克隆远端仓库到本地新仓库里  
`$ git branch`列出所有存在的分支。将返回：
```python
  experimental  
* master 井号指当前所在分支  
```

`$ git branch <name>`创建分支  
`$ git branch -d <name>`删除分支  
`$ git branch -m h<name>`重命名分支。**本地仓库分支命名需要与远端仓库分支保持命名一致**  
`$ git switch <branch name>` 转到另一个分支  
`$ git checkout <branch name>`载入另一个分支  
`$ git checkout <file name>`载入文件初始状态  
`$ git checkout -b <branch name>`以当前分支为基础新建分支  
`$ git merge <branch name>` 将分支合并进当前master分支  
`$ git merge —abort`放弃当前合并动作  
`$ git remote`列出已有的远端分支  
`$ git remote add original https://github.com/KaixiangYang6/For-Self-Learning-Python.git` **将已创建好的远端仓库添加到本地git中文件夹，成功后输入$ git remote将返回origin（目前存在的库）**  
`$ git push -u origin master`将当前origin master分支推到云端  
`$touch .gitignore`**创建一个文件名清单，其包含的文件将不会被git同步**  
  
  
`$ touch <name.js>`在本地创建一个js文件  
`$ touch </name>`在本地创建一个文件夹  
`$ clear`清空窗口内容  


