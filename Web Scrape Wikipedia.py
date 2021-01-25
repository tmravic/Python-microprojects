#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4
import zipfile
import os
import shutil
import send2trash

dir_list = os.getcwd()
dir_list


# In[6]:


desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
desktop


# In[ ]:


# Web scrape the first page of Wikipedia, https://en.wikipedia.org/wiki/Main_Page

# Get the user's directory
lets_go = True
while lets_go:
    
    # James's idea
# if os.path.exists(image_path):
#  print('Path already exists')
# else:
#   os.mkdir(image_path)

# try:
#   os.mkdir(image_path)
# except FileExistsError:
#   print('Path exists')

#shutil.move('downloaded path', image_path)
    print('Hello and welcome to the Wikipedia Image Web-Scraping Program!')
    input('Type anything to continue')
    print('Every day the main page of Wikipedia has some new images.')
    print('You can run this program every day and it will put today\'s images on your desktop!')
    # Web scrape wikipedia
    res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    wikimain = soup.select('.image')

    #Create the images from binary data
    for i in range(len(wikimain)):
        wiki_piki = 'https:' + str(soup.select('img')[i]['src'])
        print(wiki_piki)
        image_link = requests.get(wiki_piki)
        f = open('wiki{}.jpg'.format(str(i)), 'wb')
        f.write(image_link.content)
        f.close()


    # Create the zip file
    zip_it_up = zipfile.ZipFile('zip_it_up.zip', 'w')
    for i in range(len(wikimain)):
        zip_it_up.write('wiki{}.jpg'.format(str(i)), compress_type = zipfile.ZIP_DEFLATED)
    zip_it_up.close()


    # extract the zipfile 
    zip_obj = zipfile.ZipFile('zip_it_up.zip', 'r')
    zip_obj.extractall('extracted_content')
    zip_obj.close()

    # move the extracted content to the desktop
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    shutil.move('extracted_content', desktop)

    # delete everything
    delete = input('Would you like to delete the web-scraped images now? Y or N: ')
    while delete != 'Y':
        print("Thanks for using my program! This is the end.")
        lets_go = False
        break
    if delete == 'Y':
        for i in range(len(wikimain)):
            send2trash.send2trash('wiki{}.jpg'.format(str(i)))
        send2trash.send2trash('zip_it_up.zip')
        send2trash.send2trash('extracted_content')
        send2trash.send2trash(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop\\extracted_content'))
        print("Thanks for using my program! This is the end.")
        lets_go = False
        break

