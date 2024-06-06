# MMShyd
MMShyd

exemplo funcionando: https://colab.research.google.com/drive/1ZTXIAc9yBeNBoe4YbQT91YcIkJKzb6Vo

## installation:

> quick (with git):

pip install git+https://github.com/m4rvinm4rtins/MMShyd
#pip list
#MMShyd                               0.0.2               
#pip uninstall MMShyd

> quick (without git)

pip install https://github.com/m4rvinm4rtins/MMShyd/archive/main.zip
#pip list
#MMShyd                               0.0.2               
#pip uninstall MMShyd

> dev mode (git required):

git clone https://github.com/m4rvinm4rtins/MMShyd/ MMShyd-main

pip install -e ./MMShyd-main #!!!

#pip list
#>>> MMShyd                               0.0.2               /home/marvin/Desktop/MMShyd-main
#pip uninstall MMShyd

> or

#@/path/to/projct_xyz
pip install -e git+https://github.com/m4rvinm4rtins/MMShyd#egg=MMShyd
#pip list
#MMShyd                               0.0.2               /home/marvin/Desktop/project_xyz/src/MMShyd
#pip uninstall MMShyd

> from pypi test

pip install -i https://test.pypi.org/simple/MMShyd
#pip list
#MMShyd                               0.0.3               

## usage

> as a standalone program
python -m MMShyd
#this is the name of the directory neighbor to setup.py, cointaining __init__.py and __main__.py;

```
(base) marvin$ python -m MMShyd
    __init__.py running
    it' s not very effective
    __main__.py running
    nada acontece feijoada
```

> import package

import MMShyd

```
(base) $ python
    >>> import MMShyd
    __init__.py running
    it' s not very effective
```

> import modules

from MMShyd import mod1


'''

>>> from MMShyd import mod1

loading mod1

run "dir(mod1)" to see contents

'''

from MMShyd.mod1 import clas1

obj1=clas1()

'''here is your new object of the class clas1'''

obj2=clas1()

'''here is your new object of the class clas1'''

obj3=clas1()

'''here is your new object of the class clas1'''

from MMShyd.aux.mod2 import clas2 [ok]

python -m MMShyd.aux [ok]

from MMShyd import test_aux [ok]

```

## pip upload (https://packaging.python.org/en/latest/tutorials/packaging-projects/)

> build
	
`$MMShyd-main: python setup.py sdist bdist_wheel`

> upload
	
prerequesite:

`pip install twine`
	
`$MMShyd-main: python -m twine upload --verbose  --repository-url https://test.pypi.org/legacy/ dist/*`

note: cannot reupload the same version "error: File already exists."

> clean

`rm -rf MMShyd.egg-info`

`rm -rf dist`

`rm -rf build`
