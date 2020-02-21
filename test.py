import subprocess

code, ver = subprocess.getstatusoutput("docker --version")

if code == 0:
    print("Docker is installed")
    os = subprocess.getoutput("""echo $(grep -oP '(?<=^NAME=).+' /etc/os-release | tr -d '"')""")
    print(os)
else:
    print("Docker not installed!")
    os = subprocess.getoutput("""echo $(grep -oP '(?<=^NAME=).+' /etc/os-release | tr -d '"')""")
    if 'Ubuntu' in os:
        print(os)
        subprocess.getoutput("sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y")
        print("Adding key")
        subprocess.getoutput("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -")
        print("Adding docker repository")
        subprocess.getoutput("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'")
        subprocess.getoutput("sudo apt remove docker-ce docker-engine docker.io -y")
        print("Installing Docker in ubuntu")
        subprocess.getoutput("sudo apt-get update")
        subprocess.getoutput("sudo apt-get install docker-ce -y")
        print("Running docker service")
        subprocess.getoutput("sudo systemctl start docker && sudo systemctl enable docker")
        print("Installing docker-compose")
        subprocess.getoutput("sudo curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose")
    
    elif 'Red Hat Enterprise Linux' in os:
        print("Installing docker in RHEL")
        subprocess.getoutput("sudo yum install yum-utils device-mapper-persistent-data curl lvm2 -y")
        print("Installed required packages")
        subprocess.getoutput("sudo yum-config-manager --add-repo  https://download.docker.com/linux/centos/docker-ce.repo")
        print("Repo added to repository")
        subprocess.getoutput("sudo yum remove docker-ce docker-engine docker.io -y")
        print("Removed pre-installed docker packages")
        subprocess.getoutput("sudo yum install docker-ce --nobest -y -y")
        print("Installed docker package")
        subprocess.getoutput("sudo  systemctl start docker && sudo systemctl enable docker")
        print("Installing docker-compose")
        subprocess.getoutput("sudo curl -L https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose")
        
    elif 'Fedora' in os:
        print("Installing docker in fedora")
        subprocess.getoutput("sudo dnf -y install dnf-plugins-core")
        subprocess.getoutput("sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo")                                                                                  
        subprocess.getoutput("sudo dnf install docker-ce -y -y --nobest")
        subprocess.getoutput("sudo systemctl start docker && sudo systemctl enable docker")
        print("Installing docker-compose")
        subprocess.getoutput("sudo dnf -y install curl")
        subprocess.getoutput("sudo curl -L 'https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose")

    elif 'Debian' in os:
        print(os)
        subprocess.getoutput("sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y")
        print("Adding key")
        subprocess.getoutput("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -")
        print("Adding docker repository")
        subprocess.getoutput("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'")
        subprocess.getoutput("sudo apt remove docker-ce docker-engine docker.io -y")
        print("Installing Docker in ubuntu")
        subprocess.getoutput("sudo apt-get update")
        subprocess.getoutput("sudo apt-get install docker-ce -y")
        print("Running docker service")
        subprocess.getoutput("sudo systemctl start docker && sudo systemctl enable docker")
        print("Installing docker-compose")
        subprocess.getoutput("sudo curl -L https://github.com/docker/compose/releases/download/1.23.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose")
    

# print("Launching containers...")
# subprocess.getoutput("sudo /usr/local/bin/docker-compose build")
# subprocess.getoutput("sudo /usr/local/bin/docker-compose up -d")