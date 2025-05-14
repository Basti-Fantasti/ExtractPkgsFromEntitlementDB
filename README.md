# Extract all PKG Download Links from your Entitlement.db file

## Preface

For this to work, you need to jailbreak your PS4 and copy the entitlement.db e.g. via FTP into the script directory.

The entitlement db can be found on the PS4 here:

````
    /system_data/priv/license/entitlement.db
````

The script is not perfect and not all errors are caught but it does its job :-)


**The downloaded pkgs can only be run on the same PS4 as the entitlement.db was taken from.**

## Use Release File

The script can be downloaded as a zip file containing the Windows EXE file of the compiled script. 

Just extract the exe file into a directory on your hard drive and place the entitlement.db file in the same directory.

Execute the **ExtractPkgsFromEntitlementDB.exe** file and wait for the process to be finished.


## Setup Python venv for using the script

- Install Python 3.8+ (with virtualenv, virtualenvwrapper-win, pip)
- clone this repo
- Inside cloned repo directory, Setup virtual environment with:
```shell    
python -m venv .venv
```
- Activate venv on Windows (Powershell) with:
```shell
.venv\Scripts\activate
```

- Activate venv on Unix/Mac

```Shell
source .venv/bin/activate
```

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
- all found package files will be written to the **dl_links.csv** file in the script directory

Example Format of CSV File:

|ID|Title|URL|
| --- | ---| ---|
|EP0006-CUSA02532_00-UNRAVELUNRAVEL09 |Unravel | http://gs2.ww.prod.dl.playstation.net/.../EP0006-CUSA02532_00-UNRAVELUNRAVEL09.pkg

the links without any description or ID will be written to **dl_links_only.txt** file in the script directory for importing into e.g. jdownloader2

## Additional

You can then use any program to directly download the package files (e.g. jdownloader2)

and process them further (merge updates, ...)

