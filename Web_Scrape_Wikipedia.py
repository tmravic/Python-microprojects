#!/usr/bin/env python
# coding: utf-8


import requests
import bs4
import lxml
import zipfile
import os
import shutil
import send2trash


dir_list = os.getcwd()
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


lets_go = True
while lets_go:
    try:
        shutil.rmtree(desktop + '/extracted_content')
    except:
        pass
    print('Hello and welcome to the Wikipedia Image Web-Scraping Program!')
    print('Every day the main page of Wikipedia has some new images.')
    print('You can run this program every day and it will put today\'s images on your desktop!')
    input('Type anything to continue: ')
    
    res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    wikimain = soup.select('.image')


    for i in range(len(wikimain)):
        wiki_piki = 'https:' + str(soup.select('img')[i]['src'])
        image_link = requests.get(wiki_piki)
        f = open('wiki{}.jpg'.format(str(i)), 'wb')
        f.write(image_link.content)
        f.close()


    zip_it_up = zipfile.ZipFile('zip_it_up.zip', 'w')
    for i in range(len(wikimain)):
        zip_it_up.write('wiki{}.jpg'.format(str(i)), compress_type = zipfile.ZIP_DEFLATED)
    zip_it_up.close()


    zip_obj = zipfile.ZipFile('zip_it_up.zip', 'r')
    zip_obj.extractall('extracted_content')
    zip_obj.close()
    for i in range(len(wikimain)):
            send2trash.send2trash('wiki{}.jpg'.format(str(i)))
            send2trash.send2trash('zip_it_up.zip')


    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    shutil.move('extracted_content', desktop)


    delete = input('Would you like to delete the web-scraped images now? Y or N: ').upper()
    while delete != 'Y':
        if delete == 'N':
            print("Thanks for using my program! This is the end.")
            lets_go = False
            break
        delete = input('Did you mistype? Please enter Y or N: ').upper()
    else:
        for i in range(len(wikimain)):
            send2trash.send2trash('wiki{}.jpg'.format(str(i)))
            send2trash.send2trash('zip_it_up.zip')
            send2trash.send2trash('extracted_content')
            send2trash.send2trash(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop\\extracted_content'))
        print("Thanks for using my program! This is the end.")
        lets_go = False
        break

