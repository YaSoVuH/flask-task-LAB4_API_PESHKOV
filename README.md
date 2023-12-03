# flask-task
demo project for simple REST-API by python

## req python 3.10! and higher 

## Step 0. Init virtuel env
    python3 -m venv .venv


## Step 1. To activate venv windows/linux
    .\.venv\Scripts\activate
    source .venv/bin/activate

use PowerShell by admin and  execute: Set-ExecutionPolicy RemoteSigned (comfirm for ALL)

## Step 2. To save packages
    pip freeze >package.txt

## Step 3. To deactivate a virtual environment:
    deactivate

## Step 4. To init from req    
    virtualenv .venv
    Step 1 (windows/linux)
    pip install -r package.txt

## to install new packages
    pip install <package-name>

## Запуск проекта

# by python
    python main.py
    py .\main.py

# by flask (venv/windows)
    $env:FLASK_APP = "main.py"
    flask run --port=2001

# by process manager (not venv)
    sudo pm2 start ".venv/bin/python3 main.py" --name FLASK


## Body JSON:

# 1:
    {
    "method": "ConvertFrom6to10",
    "data": {
    "value": ""
    }
    }

# 2:
    {
    "method": "multiplyMatrixAlgByStrasen",
    "data": {
    "value": 0,
    "matrix1": "",
    "matrix2": ""
    }
    }

P.S. Матрицу вводить i1j1 i1j2; i2j1 i2j2 (Доступна только 2 на 2)

# 3:
    {
    "method": "HowMuchBuckvVTexte",
    "data": {
    "value": "",
    "letter": ""
    }
    }

# 4:
    {
    "method": "DeleteGlasBukv",
    "data": {
    "value": ""
    }
    }
