# <p style="text-align: center;">📚 Secret Diary</p>
<div align="center">

![GitHub](https://img.shields.io/github/license/ext8/secret_diary?style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/ext8/secret_diary?style=flat-square)
[![Maintainability](https://api.codeclimate.com/v1/badges/3d026bbe4c4c81823fac/maintainability)](https://codeclimate.com/github/ext8/secret_diary/maintainability)
![GitHub top language](https://img.shields.io/github/languages/top/ext8/secret_diary?style=flat-square)
![version](https://img.shields.io/badge/version-0.2.0-green?style=flat-square)
</div>
<br>

```
Your private diary is now protected with encryption.
```
> ⚠️ Secret Diary is a work-in-progress and far from complete.

### help page

```bash
$ secd --help
```
## Features
| No. 	| Features               	|
|-----	|------------------------	|
| 1.  	| password-protected     	|
| 2.  	| logs,stats & meta-data 	|
| 3.  	| foss & 100% private    	|
| 4.  	| portability            	|



## installation

### clone

```bash
$ git clone https://github.com/ext8/secret_diary.git
```

### build

> `conda`

```bash
$ conda env create -f environment.yml
>> [100% complete]
$ pip install --editable .
>> [100% complete]
$ secd --help
```

> `venv `

 ```bash
 $ python -m venv .
 >> [ 100% complete]
 $ pip install -r requirements.txt
 >> [100% complete]
 $ pip install --editable .
 >> [100% complete]
 $ secd --help
```

### License

[`MIT`](https://choosealicense.com/licenses/mit/)

### dependencies


| `function`| `libraries used`   |
|-----------|--------------------|
| `*.7z` 	| `py7zr` 	         |
| `cli`     | `click, rich`      |



### file structure

```
.
├── .github
│   └── workflows
│       └── actions.yml
├── .gitignore
├── .pre-commit-config.yaml
├── app
│   ├── commands
│   │   ├── __init__.py
│   │   └── init.py
│   └── main.py
├── docs
│   └── TODO.md
├── environment.yml
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── utils
    ├── __init__.py
    ├── core
    │   └── main.py
    ├── initial
    │   └── new_diary.py
    └── logging
        └── sql_context_manager.py

```
