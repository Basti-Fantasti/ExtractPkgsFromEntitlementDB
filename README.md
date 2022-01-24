# Extract all PKG Download Links from your Entitlement.db file

## Preface

For this to work, you need to jailbreak your PS4 and copy the entitlement.db e.g. via FTP into the script directory.

The entitlement db can be found on the PS4 here:

````
    /system_data/priv/license/entitlement.db
````

The script is not perfect and not all errors are caught but it does its job :-)


**The downloaded pkgs can only be run on the same PS4 as the entitlement.db was taken from.**

## Setup

- Install Python 3.8+ (with virtualenv, virtualenvwrapper-win, pip)
- clone this repo
- Inside cloned repo directrory, Setup virtual environment with:
````shell    
python -m venv venv
````
- Activate venv with:
````shell
venv\Scripts\activate
````
- Install dependencies:
````shell
pip install -r requirements.txt
````
- Copy your entitlement.db file to repo directory next to main.py

## Run the script

- run main.py to start the program:

````shell
python main.py
````
- all found package files will be written to the **dl_links.csv** file in the same directory

Example Format of CSV File:

|ID|Title|URL|
| --- | ---| ---|
|EP0006-CUSA02532_00-UNRAVELUNRAVEL09 |Unravel | http://gs2.ww.prod.dl.playstation.net/.../EP0006-CUSA02532_00-UNRAVELUNRAVEL09.pkg

the links without any description or ID will be written to **dl_links_only.txt** file in the same directory
## Additional

You can then use any program to directly download the package files (e.g. jdownloader2)

and process them further (merge updates, ...)

