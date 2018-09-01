# Dirobium
The virtual CPU (and emulator) built for hobbyists (pronounced die-row-bee-yum)

## Installation
The installation is split into two parts. Setting up the pyzip and setting up the enulation environment

### Creating a pyz
To package all of the emulator together into one small file, we use python's zipfile format.

First, clone this repo.
```
git clone https://github.com/Ewpratten/Dirobium.git && cd Dirobium
```

Then, create the pyz file:
```bash
zip -r dirobium.zip ./src
mv dirobium.zip dirobium
```

You now have a file called dirobium. It contains all of dirobium's source code.

Every time you want to update dirobium, redo this step.

### Creating the emulation environment
Dirobium uses something called an *emulation environment*. This is really just a folder in your home directory that contains the emulator, bootloader, system rom, and devices. To set it up (assuming you are still in the same directory from the step above), run:

```
mkdir ~/dirobium
mkdir ~/dirobium/devices
touch ~/dirobium/bootloader.rom ~/dirobium/main.rom
mv ./dirobium ~/dirobium/
echo "#!/bin/bash" > /usr/local/bin/enter-dirobium
echo "cd ~/dirobium" >> /usr/local/bin/enter-dirobium
chmof 755 /usr/local/bin/enter-dirobium
```

Now, run `enter-dirobium` and you are in the emulation environment (run this command any time you want to go back into the folder)

You can run `python3 dirobium` but it will do nothing, because you have not written any code to be run.

Take a look at [Deuterium](https://github.com/Ewpratten/Deuterium) for some guidance on how to install a bootloader, and install a graphics emulator / driver.

If you would like to learn how to write your own programs, take a look at [DirAS](https://github.com/Ewpratten/DirAS)

## Usage
Once you have installed everything, just run:
```bash
enter-dirobium
python3 dirobium
```