## setup git cli and git lfs

### Install

##### install git
```zsh
sudo apt install git
```

##### install git lfs if you need
```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```

##### login in cli
```bash
git config user.name my-name
git config user.email my-email
git config --global credential.helper store
```

##### now clone or push to a repo where you need to login type user name when asked and Access Token for password.

##### if you want to delete login details shred .git-credentials thsi will delete the file forever!
```bash
shred -v -n 20 -u .git-credentials
```
##### get github release latest link

https://github.com/USER/PROJECT/releases/latest/download/package.zip

Example:

https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64
