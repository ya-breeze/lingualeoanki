import os
from random import randint
import json
from .six.moves import urllib
import socket
import ssl

from aqt import mw
from anki import notes

from . import styles


fields = ['en', 'transcription',
          'ru', 'picture_name',
          'sound_name', 'context']


def create_templates(collection):
    template_eng = collection.models.newTemplate('en -> ru')
    template_eng['qfmt'] = styles.en_question
    template_eng['afmt'] = styles.en_answer
    template_ru = collection.models.newTemplate('ru -> en')
    template_ru['qfmt'] = styles.ru_question
    template_ru['afmt'] = styles.ru_answer
    return (template_eng, template_ru)


def create_new_model(collection, fields, model_css):
    model = collection.models.new("LinguaLeo_model")
    model['tags'].append("LinguaLeo")
    model['css'] = model_css
    for field in fields:
        collection.models.addField(model, collection.models.newField(field))
    template_eng, template_ru = create_templates(collection)
    collection.models.addTemplate(model, template_eng)
    collection.models.addTemplate(model, template_ru)
    model['id'] = randint(100000, 1000000)  # Essential for upgrade detection
    collection.models.update(model)
    return model


def is_model_exist(collection, fields):
    name_exist = 'LinguaLeo_model' in collection.models.allNames()
    if name_exist:
        fields_ok = collection.models.fieldNames(collection.models.byName(
                                                'LinguaLeo_model')) == fields
    else:
        fields_ok = False
    return name_exist and fields_ok


def prepare_model(collection, fields, model_css):
    """
    Returns a model for our future notes.
    Creates a deck to keep them.
    """
    if is_model_exist(collection, fields):
        model = collection.models.byName('LinguaLeo_model')
    else:
        model = create_new_model(collection, fields, model_css)
    # TODO: Move Deck name to config?
    # Create a deck "LinguaLeo" and write id to deck_id
    model['did'] = collection.decks.id('LinguaLeo')
    collection.models.setCurrent(model)
    collection.models.save(model)
    return model


def get_valid_name(orig_name):
    """
    Unfortunately, from April 30, 2019,
    media filenames can be very long and contain '\n' symbols,
    the function checks if it is the case
    and returns a name without '\n' and only up to 30 characters
    """
    if len(orig_name) > 50 or orig_name.find('\n'):
        new_name = orig_name[-30:]
        new_name = new_name.replace('\n', '')
        return new_name
    else:
        return orig_name


def download_media_file(url):
    DOWNLOAD_TIMEOUT = 20
    destination_folder = mw.col.media.dir()
    name = url.split('/')[-1]
    name = get_valid_name(name)
    abs_path = os.path.join(destination_folder, name)
    # Fix '\n' symbols in the url (they were found in the long sentences)
    url = url.replace('\n', '')
    # TODO: find a better way for unsecure connection
    resp = urllib.request.urlopen(url, timeout=DOWNLOAD_TIMEOUT, context=ssl._create_unverified_context())
    media_file = resp.read()
    with open(abs_path, "wb") as binfile:
        binfile.write(media_file)


def send_to_download(word, thread):
    # TODO: Move to config following settings and DOWNLOAD_TIMEOUT
    NUM_RETRIES = 3
    SLEEP_SECONDS = 5
    # try to download the picture and the sound the specified number of times,
    # if not succeeded, raise the last error happened to be shown as a problem word
    sound_url = word['pron']
    if sound_url:
        exc_happened = None
        for i in list(range(NUM_RETRIES)):
            exc_happened = None
            try:
                download_media_file(sound_url)
                break
            except (urllib.error.URLError, socket.error) as e:
                exc_happened = e
                thread.sleep(SLEEP_SECONDS)
        if exc_happened:
            raise exc_happened
    translations = word['trs']
    if not translations:
        """
        There might be no translation for the word
        """
        # TODO: Find the example of word with no translation
        #  and handle it according to structure
        return
    pictures = translations[0]['pics']
    if pictures:
        exc_happened = None
        pic_url = pictures[0]
        picture_url = pic_url if pic_url.startswith('https:') else 'https:' + pic_url
        for i in list(range(NUM_RETRIES)):
            exc_happened = None
            try:
                download_media_file(picture_url)
                break
            except (urllib.error.URLError, socket.error) as e:
                exc_happened = e
                thread.sleep(SLEEP_SECONDS)
        if exc_happened:
            raise exc_happened


def fill_note(word, note):
    note['en'] = word['wd']
    # TODO: Allow user to collect more than one translation
    #  see: https://bitbucket.org/alon_kot/lingualeoanki/commits/8a430865d330b37ec688006e1026a39e05d2cc35#chg-lingualeo/utils.py
    # User's choice translation has index 0, then come translations sorted by votes (higher to lower)
    translations = word['trs']
    if translations:  # apparently, there might be no translation
        translation = translations[0]
        note['ru'] = translation['tr']
        if translation.get('ctx'):
            note['context'] = translation['ctx']
        pictures = translation['pics']
        if pictures:
            picture_name = pictures[0].split('/')[-1]
            picture_name = get_valid_name(picture_name)
            note['picture_name'] = '<img src="%s" />' % picture_name
    if word['scr']:
        note['transcription'] = '[' + word['scr'] + ']'
    sound_url = word['pron']
    if sound_url:
        sound_name = sound_url.split('/')[-1]
        sound_name = get_valid_name(sound_name)
        note['sound_name'] = '[sound:%s]' % sound_name
    # TODO: Add user dictionaries (wordsets) as tags
    return note


def add_word(word, model):
    # TODO: Use picture_name and sound_name to check
    #  if update is needed and don't download media if not
    collection = mw.col
    note = notes.Note(collection, model)
    note = fill_note(word, note)
    # TODO: Rewrite to use is_duplicate()
    dupes = collection.findDupes("en", word['wd'])
    # a hack to support words with apostrophes
    note_dupes1 = collection.findNotes("en:'%s'" % word['wd'])
    note_dupes2 = collection.findNotes('en:"%s"' % word['wd'])
    note_dupes = note_dupes1 + note_dupes2
    if not dupes and not note_dupes:
        collection.addNote(note)
    # TODO: Update notes if translation or tags (user wordsets) changed
    elif (note['picture_name'] or note['sound_name']) and note_dupes:
        # update existing notes with new pictures and sounds in case
        # they have been changed in LinguaLeo's UI
        for nid in note_dupes:
            note_in_db = notes.Note(collection, id=nid)
            # a dirty hack below until a new field in the model is introduced
            # put a space before or after a *sound* field of an existing note if you want it to be updated
            # if a note has no picture or sound, it will be updated anyway
            # TODO: Check if hack is still needed, remove if not
            sound_name = note_in_db['sound_name']
            sound_name = sound_name.replace("&nbsp;", " ")
            note_needs_update = sound_name != sound_name.strip()
            if note['picture_name'] and (note_needs_update or not note_in_db['picture_name'].strip()):
                note_in_db['picture_name'] = note['picture_name']
            if note['sound_name'] and (note_needs_update or not note_in_db['sound_name'].strip()):
                note_in_db['sound_name'] = note['sound_name']
            note_in_db.flush()
    # TODO: Check if it is possible to update Anki's media collection to remove old (unused) media


def is_duplicate(word):
    """
    Check if the word exists in collection
    :param word: dictionary
    :return: bool
    """
    collection = mw.col
    dupes = collection.findDupes("en", word['wd'])
    # a hack to support words with apostrophes
    # TODO: Debug to find out if it is still required
    note_dupes1 = collection.findNotes("en:'%s'" % word['wd'])
    note_dupes2 = collection.findNotes('en:"%s"' % word['wd'])
    note_dupes = note_dupes1 + note_dupes2
    return True if dupes or note_dupes else False


def get_module_name():
    return __name__.split(".")[0]


def get_addon_dir():
    root = mw.pm.addonFolder()
    addon_dir = os.path.join(root, get_module_name())
    return addon_dir


def get_cookies_path():
    """
    Returns a full path to cookies.txt in the user_files folder
    :return:
    """
    # user_files folder in the current addon's dir
    uf_dir = os.path.join(get_addon_dir(), 'user_files')
    # Create a folder if doesn't exist
    if not os.path.exists(uf_dir):
        try:
            os.makedirs(uf_dir)
        except:
            # TODO: Improve error handling
            return None
    return os.path.join(uf_dir, 'cookies.txt')


def clean_cookies():
    # TODO: Better handle file removal (check if exists or if in use)
    try:
        os.remove(get_cookies_path())
    except:
        pass


def get_config():
    # Load config from config.json file
    if getattr(getattr(mw, "addonManager", None), "getConfig", None):
        config = mw.addonManager.getConfig(get_module_name())
    else:
        try:
            config_file = os.path.join(get_addon_dir(), 'config.json')
            with open(config_file, 'r') as f:
                config = json.loads(f.read())
        except IOError:
            config = None
    return config


def update_config(config):
    if getattr(getattr(mw, "addonManager", None), "writeConfig", None):
        mw.addonManager.writeConfig(get_module_name(), config)
    else:
        try:
            config_file = os.path.join(get_addon_dir(), 'config.json')
            with open(config_file, 'w') as f:
                json.dump(config, f, sort_keys=True, indent=2)
        except:
            # TODO: Improve error handling
            pass
