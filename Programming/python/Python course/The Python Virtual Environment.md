
First install `pypy3-venv`:
`sudo apt update`
`sudo apt install pypy3-venv`

Create a virtual environment in the directory:
`python3 -m venv .`

Start using the environment by runnig:
`source bin/activate`

To run scripts
The venv will be used automatically for the user but to run a script with sudo you need to give the local python path: `./bin/python`

Exit the virtual environment by running:
`deactivate`

Use pip3 for installing libraries, it's aware of virtual environments:
`pip3 install pwntools`

# For python2

`sudo apt install virtualenv`
`virtualenv -p python2 py2env`
`source py2env/bin/activate`

