# Work

```
pipx uninstall pygitscrum #if necessary 
git clone https://github.com/thib1984/pygitscrum.git
cd pygitscrum 
rm -rf pygitscrum_env #clean env if necessary
python3 -m venv pygitscrum_env
source pygitscrum_env/bin/activate
#work!
pip install .
pygitscrum [...] #to retest
deactivate
pipx install pygitscrum #if necessary 
``` 

# Publish to pypi

```
#from work directory
python3 -m build && python3 -m twine upload dist/* #to publish to pypi
```