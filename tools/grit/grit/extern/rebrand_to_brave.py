# Before running this script
# In Atom (or other editor) make changes to .grd and .xtb files in folders (chrome/android/java/strings, components/strings, chrome/app/resources, chrome/app):
# Chromiumista -> Brave
# Chromiumist -> Brave
# Chromiumilla -> Brave
# Chromiumille -> Brave
# Chromiumile -> Brave
# Chromiumil -> Brave
# Chromiumiin -> Brave
# Chromiumin -> Brave
# Chromiumia -> Brave
# Chromiumi -> Brave
# Chromiuma -> Brave
# Chromiumu -> Brave
# Chromiumova -> Brave
# Chromiumove -> Brave
# Chromiumov -> Brave
# Chromiumom -> Brave
# Chromiumot -> Brave
# Chromiumnak -> Brave
# Chromiumban -> Brave
# Chromiumba -> Brave
# Chromiumhoz -> Brave
# Chromiumra -> Brave
# Chromiummal -> Brave
# Chromiumos -> Brave
# Chromiumon -> Brave
# Chromiumja -> Brave
# Chromiums -> Brave
# Chromium -> Brave
# Brave <ph name="VERSION_CHROMIUM"> -> Chromium <ph name="VERSION_CHROMIUM">
# Brave Authors -> Chromium Authors
# Brave OS -> Chromium OS
# Google Chrome -> Brave
# Google Chromu -> Brave
# Google Chroma -> Brave
# Google Chromom -> Brave
# Google Chromovimi -> Brave
# Google Chromovim -> Brave
# Google Chromovi -> Brave
# Google Chromove -> Brave
# Google Chromovo -> Brave
# Google Chromova -> Brave
# Google Chromov -> Brave
# Brave OS -> Google Chrome OS
# Chrome -> Brave
# Chromuim -> Brave
# Chromu -> Brave
# Chroma -> Brave
# Chromom -> Brave
# Chromovimi -> Brave
# Chromovim -> Brave
# Chromovi -> Brave
# Chromovem -> Brave
# Chromovega -> Brave
# Chromove -> Brave
# Chromovo -> Brave
# Chromova -> Brave
# Chromov -> Brave
# Brave OS -> Chrome OS
# Google LLC -> Brave Software Inc

# In `android_chrome_strings.grd` make sure that these are changed:
# IDS_CHROME_PRIVACY_NOTICE_URL -> https://brave.com/privacy_android
# IDS_CHROME_TERMS_OF_SERVICE_URL -> https://brave.com/terms_of_use
import sys
import os.path
import xml.etree.ElementTree
import FP
from os import walk

# These are hard coded values
chrome_strings_file='../../../../chrome/android/java/strings/android_chrome_strings.grd'
chromium_strings_file='../../../../chrome/app/chromium_strings.grd'
translations_folder='../../../../chrome/android/java/strings/translations'
components_folder='../../../../components/strings'
chromium_strings_folder='../../../../chrome/app/resources'
brave_brand_string='Brave'
brave_company='Brave Software'
google_company='Google'
chrome_brand_strings={'Chrome', 'Google Chrome', 'Chromium'}
brave_ids={}

# Go through .xtb files and replace ids
def ReplaceIds(folder):
    for (dirpath, dirnames, filenames) in walk(folder):
        for filename in filenames:
            if filename.endswith('.xtb') and 'locale_settings' not in filename:
                translations_tree = xml.etree.ElementTree.parse(folder + '/' + filename)
                translations = translations_tree.getroot()
                print('Processing file "' + filename + '"...')
                found_id = False
                for translation_tag in translations.findall('translation'):
                    translation_id = long(translation_tag.get('id'))
                    if translation_id in brave_ids:
                        print('Replacing "' + str(translation_id) + '" with "' + str(brave_ids[translation_id]) + '"')
                        translation_tag.set('id', str(brave_ids[translation_id]))
                        found_id = True
                if found_id:
                    new_file_name = folder + '/' + filename
                    translations_tree.write(new_file_name, encoding="utf-8", xml_declaration=False)
                    # We need to add prepend headers
                    f = open(new_file_name, 'r+')
                    # Load all content to the memory to make it faster (size is less than 1Mb, so should not be a problem)
                    content = f.read()
                    f.seek(0, 0)
                    f.write(('<?xml version="1.0" ?>\n<!DOCTYPE translationbundle>\n') + content)
                    f.close()
    print('Brave ids successfully updated in ' + folder)

# Generate message id from message text and meaning string (optional),
# both in utf-8 encoding
#
def GenerateMessageId(message, meaning=''):
    fp = FP.FingerPrint(message)
    if meaning:
        # combine the fingerprints of message and meaning
        fp2 = FP.FingerPrint(meaning)
        if fp < 0:
            fp = fp2 + (fp << 1) + 1
        else:
            fp = fp2 + (fp << 1)
    # To avoid negative ids we strip the high-order bit
    return fp & 0x7fffffffffffffffL

# Check for Brave branded strings in grd file, calculate their ids and update them in xtb files (instead of Chrome, Google Chrome and Chromium)
def UpdateBraveIds(grd_file):
    messages = xml.etree.ElementTree.parse(grd_file).getroot().find('release').find('messages')
    for message_tag in messages.findall('message'):
        brave_string = message_tag.text
        brave_string_phs = message_tag.findall('ph')
        meaning = (message_tag.get('meaning') if 'meaning' in message_tag.attrib else None)
        for brave_string_ph in brave_string_phs:
            brave_string = (brave_string if brave_string is not None else '') + brave_string_ph.get('name').upper() + (brave_string_ph.tail if brave_string_ph.tail is not None else '')
        if brave_string is None:
            continue
        brave_string = brave_string.strip().encode('utf-8')
        if brave_company in brave_string:
            # Calculate Brave string id
            brave_string_fp = GenerateMessageId(brave_string, meaning)
            print(str(brave_string_fp) + ' - ' + brave_string)
            chrome_string = brave_string.replace(brave_company, google_company)
            # Calculate Chrome string id
            chrome_string_fp = GenerateMessageId(chrome_string, meaning)
            print(str(chrome_string_fp) + ' - ' + chrome_string)
            if not chrome_string_fp in brave_ids:
                brave_ids[chrome_string_fp] = brave_string_fp
            print('\n')
        elif brave_brand_string in brave_string:
            # Calculate Brave string id
            brave_string_fp = GenerateMessageId(brave_string, meaning)
            print(str(brave_string_fp) + ' - ' + brave_string)
            for chrome_brand_string in chrome_brand_strings:
                chrome_string = brave_string.replace(brave_brand_string, chrome_brand_string)
                # Calculate Chrome string id
                chrome_string_fp = GenerateMessageId(chrome_string, meaning)
                print(str(chrome_string_fp) + ' - ' + chrome_string)
                if not chrome_string_fp in brave_ids:
                    brave_ids[chrome_string_fp] = brave_string_fp
            print('\n')

UpdateBraveIds(chrome_strings_file)
UpdateBraveIds(chromium_strings_file)
ReplaceIds(translations_folder)
ReplaceIds(components_folder)
ReplaceIds(chromium_strings_folder)
