# Work with Github

```
pipx uninstall pygitscrum #if necessary 
git clone https://github.com/thib1984/pygitscrum.git
cd pygitscrum 
rm -rf pygitscrum_env #clean env if necessary
python3 -m venv pygitscrum_env
source pygitscrum_env/bin/activate
#work!
pip3 install .
pygitscrum [...] #to retest
deactivate

python3 -m build && python3 -m twine upload dist/* #to publish to pypi
pipx install pygitscrum #if necessary 
``` 