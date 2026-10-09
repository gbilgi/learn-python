# Installation

**Status:** In Progress

### Overview
Python is a programming language and our computer needs a program called **Interpreter** to read and run Python code.

Installing Python means, installing the interpreter plus the **pip**, the tool that downloads extra libraries.




### Installing Python on Windows
#### Step1: Check if Python is already installed
- Open command prompt and type `python --version` and press Enter.
- If you see something like Python 3.3.x, its installed.
- If it errors out then probably it's not installed.

#### Step2: Download the installer
- Go to www.python.org/downloads
- Download the latest version.

#### Step3: Run the Installer
- On the first screen, tick the box **"Add python.exe to PATH"**. This is the most important step. PATH is a list of folders that Windows will search when we type a command.

#### Step4: Verify it worked
- Open command prompt and verify `python --version` and `pip --version`

#### Step5: Run the first program
- Type `python` and press enter. You'll see `>>>` which is the interactive mode.
- Type `print("Hello World!")` and press Enter.
- Type `exit()` to leave. 


### Installing Python on Linux
Most Linux Distributions comes pre-installed with Python as their system tools depend on it.

#### Step1: Check the current version
- Open a terminal and run `python --version`

#### Step2: Installing or upgrading using the package manager
| Distribution | Command |
|:-------------|:---------|
| Ubuntu, Debian, Mint | `sudo apt update` then `sudo apt install python3 python3-pip` `python3-venv`|
| Fedora | `sudo dnf install python3 python3-pip`|
| Arch, Manjaro | `sudo pacman -S python python-pip`|

`sudo` means run as administrator

#### Step3: Verify
- Run `python3 --version` and `pip3 --version`

Don't touch the system Python. Instead, use a version manager `uv` or virtual environment.

#### Step4: Virtual environments
- A virtual environment is a private folder holding Python libraries for one project, so they never conflict.
```python
    python -m venv .venv
    source .venv/bin/activate
```
- When active we will see `(.veve)` at the start of prompt. Now any pip install requests installs only into this folder.
- Type `deactivate` to leave.

### Code editors and IDE




## Related
- 
