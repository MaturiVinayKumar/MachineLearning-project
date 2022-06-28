# MachineLearning-project

**Start Machine Learning project.** 



## Software and account Requirement

 - [Github Account](https://github.com/)
 - [Heroku Account](https://dashboard.heroku.com/login)
 - [VS Code IDE](https://code.visualstudio.com/download)
  - [GIT cli](https://git-scm.com/downloads)
 - [GIT Documentation](https://git-scm.com/docs/gittutorial)
  
Creating conda environment
```
    conda create -p venv python==3.7 -y

```

```
    conda activate venv/

```
```
pip install -r requirements.txt

```

To Add files to git
```
git add .

```
OR
```
git add <file_name>

```
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status

```
To check all version maintained by git
```
git log

```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v

```
To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = vinaykumar3414.maturi@gmail.com
2. HEROKU_API_KEY = 086779a8-c8f6-40da-9704-d58fe45ea433
3. HEROKU_APP_NAME = ml-ineuron-regression-app1

BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>
python setup.py install
Install ipykernel

pip install ipykernel