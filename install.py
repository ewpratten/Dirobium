from sys import platform, stderr
import os

nix = ['linux', 'linux2']
win = ['win32']
osx = ['darwin']

def clear():
    if platform in nix:
        os.system('clear')
    elif platform in win:
        os.system('cls')
    elif platform in osx:
        # I dont know
        pass

def install_linux():
    inst_dir = "~/dirobium"
    # Asking for Installation Directory
    while True:
        clear()
        print("Current Installation Directory : {}".format(inst_dir))
        _ = str(input("Insert Another Installation Directory (blank to use Current Directory)\n:"))

        if _ not in [" ", ""]:
            if _[0] is not '~':
                _ = os.path.join("~", _)
            if "dirobium" not in _:
                inst_dir = os.path.join(_, "dirobium/")
            else:
                inst_dir = _
        else:
            break

    # Pre Requirements Installation
    ansy = ['y', 'yes', '1', 'yes please', 'fuck yeah!', 'why not?' ]
    clear()
    print("Pre-requirements: git, zip\nDo you want to install Pre-requirements ?")
    print("This May Require Internet Connection and Root Previlages.")
    _ = str(input("[Y/n] >> ")).replace(" ", "").lower()
    if _ in ansy:
        clear()
        print("Installing Pre-requirements:\ngit")
        os.system("sudo apt-get install git > /dev/null && echo git installed successfully")
        os.system("sleep 2")
        clear()
        print("Installing Pre-requirements:\nzip")
        os.system("sudo apt-get install zip > /dev/null && echo zip installed successfully")
        os.system("echo Proceeding to Installing Dirobium Environment Installation... && sleep 2")

    # Dirobium Installation
    clear()
    print("Updating Dirobium...")
    os.system("git clone https://github.com/EWpratten/Dirobium.git")
    os.system("sync && cd Dirobium && sleep 2")

    clear()
    print("Creating pyz...")
    os.system("sync && zip -r dirobium.zip ./src")
    os.system("sync && mv dirobium.zip dirobium && sleep 2")

    clear()
    print("Creating emulation environment...")
    os.system("mkdir -p {}".format(inst_dir))
    os.system("mkdir {}/devices".format(inst_dir))
    os.system("touch {}/bootloader.rom {}/main.rom".format(inst_dir, inst_dir))
    os.system("mv ./dirobium {}".format(inst_dir))
#    os.system('echo "echo Running..." > install.sh')
#    os.system('echo "sudo rm -rf /usr/local/bin/enter-dirobium" >> install.sh')
#    os.system('echo "sudo echo "#\\!/bin/bash" > /usr/local/bin/enter-dirobium" >> install.sh')
#    os.system('echo "echo "cd {}" >> /usr/local/bin/enter-dirobium" >> install.sh'.format(inst_dir))
#    os.system('echo "sudo chmod 755 /usr/local/bin/enter-dirobium && sleep 2" >> install.sh')
#    os.system("sync && chmod 755 install.sh && sleep 2 && sudo bash install.sh")
    os.system('echo "alias enter-dirobium=\'cd {}\'" >> ~/.bashrc'.format(inst_dir))
    print("Cleaning...")
    os.system("sleep 3 && rm -rf Dirobium install.sh")


# Update this function if you know how to install in windows
def install_windows():
    stderr.write("Sorry... For now you cannot use ez-install for this platform (Windows) yet\n")

# Update this function if you know how to install in macOS-X
def install_maxosx():
    stderr.write("Sorry... For now you cannot use ez-install for this platform (OS X) yet\n")

# Update this list if you know how to install in any other OSes


if platform in nix:
    install_linux()
elif platform in win:
    install_windows()
elif platform in osx:
    install_macosx()
