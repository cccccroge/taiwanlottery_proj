# Setup for Mac

install pip via (for 2.7)

```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py | python
```

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
