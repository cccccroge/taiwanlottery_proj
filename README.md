# Install python and pip

python version: 3.8

for mac,
```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py | python
```

for windows, use installer

# Setup for Mac

install pipenv

```
pip3 install pipenv
```

install packages for the project

```
python3 -m pipenv install # first time
python3 -m pipenv install [package_name] # install dev package
```

activate the virtual env at the project root

```
pipenv shell
```

# Windows trouble shooting
```
python -m pip install kivy.deps.sdl2
python -m pip install kivy.deps.glew
```
