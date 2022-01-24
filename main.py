import sqlite3
import json
import requests
import csv
import xml.etree.ElementTree as ET


# Parse XML Files found in the database
def ParseXML(XmlIn):
    root = ET.fromstring(XmlIn)
    url = ''
    for child in root:
        print(child.tag, child.attrib)
        grandchild = child.getchildren()
        data = grandchild[0].attrib
        url = data['manifest_url']
    return url

# Retrieve the download links as a list from the found json files
# when a XML file is passed in, the function is called recursive to
# first parse the XML file for the main json file and then 
# fetch the embedded pkg files as well
def RetrieveDownloadLinks(ConfigFileIn):
    pkgurls = []
    if '.json' in ConfigFileIn:
        #get target json file from URL
        r = requests.get(ConfigFileIn, verify=False)
        if r.ok:
            data = r.json()
            pieces = data['pieces']
            for p in pieces:
                pkgurls.append(p['url'])
        #print('skip')
    if '.xml' in ConfigFileIn:
        r = requests.get(ConfigFileIn, verify=False)
        if r.ok:
            # get manifest url
            url = ParseXML(r.text)
            pkgurls = RetrieveDownloadLinks(url)             
    return pkgurls


dbpath = '.\entitlement.db'
outfile = '.\dl_links.csv'
csvheader = ['id', 'title', 'url']

con = sqlite3.connect(dbpath)
c = con.cursor()

# get entitlement table name

c.execute("SELECT name FROM sqlite_master WHERE type='table';")

target_table = ''
tables = c.fetchall()
for tabname in tables:
    itm = tabname[0]
    if "entitlement" in itm:
        target_table = itm
        break

if target_table != '':
    # build query
    q = f'select json from {target_table}'
    c.execute(q)
    # fetch all results
    res = c.fetchall()
    # open csv file for results
    with open(outfile, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write header to file
        writer.writerow(csvheader)
        # parse results
        for dataset in res:
            data_raw = dataset[0]
            data = json.loads(data_raw)
            
            game_id = data['id']
            # get json download url
            try:
                json_dl_url = data['entitlement_attributes'][0]['reference_package_url']
                game_title = data['game_meta']['name']
                print(game_title)
                # get dl links:
                lnks = RetrieveDownloadLinks(json_dl_url)
                for l in lnks:
                    outset = [game_id, game_title, l]
                    writer.writerow(outset)
                    print(f'title: {game_title} URL: {l}')
            except KeyError:
                print('No json file found - skip')

