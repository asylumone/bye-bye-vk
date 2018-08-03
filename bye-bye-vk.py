#!/usr/bin/env python3
#Bye-Bye, VK!
#With love, by t.me/undefined_value
import base64
import gzip
import getpass
import time
VKAPI_LIB = bytes("""
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
""".replace('\n', ''), 'utf-8')
LOGO = bytes("""H4sIADCaZFsAA22QUQrAIAxD/z1F/qYw1tvsS+hFevgl1TGYtlDktWlUOANr7PAk2VEpIdQgPFHGFncmYMzIQjG7PZBpOsvTV/yq
KQscKhKHN0245uhhU7zgob5liYuLnWKNmvxORB+euvYfVz5CakJt7F69lfkXkbNLfDg23fIARqEx1W4BAAA=""".replace('\n', ''), 'utf-8')
exec(gzip.decompress(base64.decodestring(VKAPI_LIB)).decode('utf-8')) # vkapi.py library
print(gzip.decompress(base64.decodestring(LOGO)).decode('utf-8')) # Bye-Bye, VK!
def select(variants, prompt):
    while True:
        print(prompt)
        for i, v in enumerate(variants):
            print('%2s> %s'%(i + 1, v))
        try:
            var = int(input('>>> ')) - 1
            if var < 0: raise IndexError
            return variants[var]
        except:
            print('[!] Invalid choice!')
authtype = select(['Token', 'Login+Password'], 'Select auth type:')
if authtype == 'Token':
    while True:
        print('Enter your access token (or type q to quit):')
        access_token = input('>>> ')
        if access_token == 'q':
            print('Bye-Bye')
            quit()
        vk = VK(access_token)
        succ, resp = vk.check_auth()
        if not succ:
            print('Error')
        else:
            print('Logged in as {first_name} {last_name} (@{domain})'.format(**resp))
            MY_ID = resp['id']
            break
else:
    while True:
        print('Enter your credentials (or type q on any field to quit):')
        username = input('Username: ')
        password = getpass.getpass()
        if 'q' in [username, password]:
            print('Bye-Bye')
            quit()
        vk = VK()
        vk.auth(username, password)
        succ, resp = vk.check_auth()
        if not succ:
            print('Error')
        else:
            print('Logged in as {first_name} {last_name} (@{domain})'.format(**resp))
            MY_ID = resp['id']
            break
print('[I] Ok, we have access to VK API, let\'s clean there...')
def _pb(prcnt):
    outs = ''
    pbwidth = 20
    pbcwidth = int(pbwidth * prcnt)
    outs += '=' * pbcwidth
    if pbcwidth < pbwidth:
        outs += '>'
    spaces_cnt = pbwidth - len(outs)
    return outs + ' ' * spaces_cnt
def progressbar(title, now, count):
    print('%20s: %3s/%3s [%3s%%|%s]'%(
        title,
        now,
        count,
        int(100 * now / count),
        _pb(now / count)), end='\r', flush=True)
def clean_wall():
    succ, resp = vk.call('wall.get')
    if not succ:
        return print('Error: {error_code}: {error_msg}'.format(**resp))
    posts = resp['items']
    errors = 0
    for i, post in enumerate(posts):
        progressbar('Cleaning wall...', i + 1, len(posts))
        succ, resp = vk.call('wall.delete', post_id=post['id'])
        if not succ:
            errors += 1
        time.sleep(3)
    print('\nOK%s'%(' (%s errors)'%errors if errors else ''))
def clean_groups():
    succ, resp = vk.call('groups.get')
    if not succ:
        return print('Error: {error_code}: {error_msg}'.format(**resp))
    groups = resp['items']
    errors = 0
    for i, group in enumerate(groups):
        progressbar('Cleaning groups...', i + 1, len(groups))
        succ, resp = vk.call('groups.leave', group_id=group)
        if not succ:
            errors += 1
        time.sleep(3)
    print('\nOK%s'%(' (%s errors)'%errors if errors else ''))
def clean_docs():
    succ, resp = vk.call('docs.get')
    if not succ:
        return print('Error: {error_code}: {error_msg}'.format(**resp))
    docs = resp['items']
    errors = 0
    for i, doc in enumerate(docs):
        progressbar('Cleaning docs...', i + 1, len(docs))
        succ, resp = vk.call('docs.delete', doc_id=doc['id'], owner_id=MY_ID)
        if not succ:
            errors += 1
        time.sleep(3)
    print('\nOK%s'%(' (%s errors)'%errors if errors else ''))
def clean_photos():
    succ, resp = vk.call('photos.getAlbums', need_system=1)
    if not succ:
        return print('Error: {error_code}: {error_msg}'.format(**resp))
    albums = resp['items']
    photos = []
    for album in albums:
        print('[I] Getting album %s...'%album['id'])
        succ, resp = vk.call('photos.get', album_id=album['id'], owner_id=MY_ID)
        if not succ:
            return print('Error: {error_code}: {error_msg}'.format(**resp))
        photos += resp['items']
    print('[I] Total photos: %s'%len(photos))
    errors = 0
    for i, photo in enumerate(photos):
        progressbar('Cleaning photos...', i + 1, len(photos))
        succ, resp = vk.call('photos.delete', photo_id=photo['id'], owner_id=MY_ID)
        if not succ:
            errors += 1
        time.sleep(3)
    print('\nOK%s'%(' (%s errors)'%errors if errors else ''))
def clean_dialogs(keep=[]):
    dialogs = []
    succ, resp = vk.call('messages.getDialogs', count=1)
    if not succ:
        return print('Error: {error_code}: {error_msg}'.format(**resp))
    count = resp['count']
    calls200 = int(count / 200)
    callsext = count % 200
    errors = 0
    for i in range(calls200):
        succ, resp = vk.call('messages.getDialogs',
            count=200,
            offset=200 * i)
        dialogs += resp['items']
        time.sleep(1)
    if callsext:
        succ, resp = vk.call('messages.getDialogs',
            count=callsext,
            offset=200 * calls200)
        dialogs += resp['items']
    dialogs = [get_peer_id(m['message']) for m in dialogs]
    for i, dialog in enumerate(dialogs):
        if int(dialog) in [int(v) for v in keep]:
            continue
        succ, resp = vk.call('messages.deleteConversation', peer_id=dialog)
        if not succ:
            errors += 1
        progressbar('Cleaning dialogs...', i + 1, len(dialogs))
        time.sleep(2)
    print('\nOK%s'%(' (%s errors)'%errors if errors else ''))
def clean_friends(blacklist=False):
    succ, resp = vk.call('friends.get')
    if not succ:
        return print('Error: {error_code}: {error_msg}'.format(**resp))
    friends = resp['items']
    with open('friends.txt', 'w') as f: f.write('\n'.join('vk.com/id%s'%i for i in friends))
    errors = 0
    for i, friend in enumerate(friends):
        progressbar('Cleaning friends...', i + 1, len(friends))
        succ, resp = vk.call('friends.delete', user_id=friend)
        if blacklist:
            succ2, resp2 = vk.call('account.ban', owner_id=friend)
        else:
            succ2, resp2 = True, 1
        if not succ or not succ2:
            errors += 1
        time.sleep(1)
    print('\nOK%s'%(' (%s errors)'%errors if errors else ''))

DIALOGS_CACHE = {}
get_peer_id = lambda m: m['chat_id'] + 2000000000 if 'chat_id' in m else m['user_id']
def get_name(peerid):
    if peerid < 2000000000:
        succ, user = vk.call('users.get', user_id=peerid % 2000000000)
        if not succ:
            print('Error: {error_code}: {error_msg}'.format(**user), '(User ID: %s)'%(peerid % 2000000000))
            return 'id%s'%(peerid % 2000000000)
        return '{first_name} {last_name}'.format(**user[0])
    else:
        succ, resp = vk.call('messages.getChat', chat_id=peerid%2000000000)
        if not succ:
            print('Error: {error_code}: {error_msg}'.format(**resp), '(Chat ID: %s)'%(peerid % 2000000000))
            return 'chat %s'%(peerid % 2000000000)
        return resp['title']

def get_dialogs():
    global DIALOGS_CACHE
    succ, resp = vk.call('messages.getDialogs')
    if not succ:
        print('Error: {error_code}: {error_msg}'.format(**resp))
        return []
    else:
        for dialog in resp['items']:
            pid = str(get_peer_id(dialog['message']))
            name = DIALOGS_CACHE.get(pid, None) 
            if not name:
                name = get_name(int(pid))
                DIALOGS_CACHE[pid] = name
            print('%10s: %s'%(pid, name))
    return list(DIALOGS_CACHE.keys())

while True:
    action = select([
        'Clean wall',
        'Clean photos',
        'Clean documents',
        'Clean dialogs',
        'Clean friends',
        'Unsubsribe from communities',
        'Quit',
        'Clean ALL'], 'Select action:')
    if action == 'Quit':
        print('Bye-Bye')
        quit()
    elif action == 'Clean wall':
        clean_wall()
    elif action == 'Clean photos':
        clean_photos()
    elif action == 'Clean documents':
        clean_docs()
    elif action == 'Clean friends':
        clean_friends(select(['Blacklist', 'No'], 'Do you want to blacklist old friends?') == 'Blacklist')
    elif action == 'Clean dialogs':
        if select(['All', 'Not all'], 'Clear all dialogs or keep some?') == 'All':
            get_dialogs()
            clean_dialogs()
        else:
            keep_list = []
            while True:
                print('Selected: %s'%', '.join(str(v) for v in keep_list))
                act = select(get_dialogs() + ['OK', 'Cancel'], 'Select dialog to add')
                if act == 'OK':
                    clean_dialogs(keep_list)
                    break
                elif act == 'Cancel':
                    break
                else:
                    keep_list.append(int(act))
    elif action == 'Unsubsribe from communities':
        clean_groups()
    elif action == 'Clean ALL':
        if select(['Yes', 'NO!', 'Goddamit, NO!!!'], 'Are you sure wants to clean ALL on this page?') == 'Yes':
            if select(['NO, I DON\'T WANTS!', 'Yes, clean', 'FUCK, NO!!'], 'Are you TOTALLY sure?') == 'Yes, clean':
                print('Starting cleaning ALL...')
                clean_docs()
                clean_photos()
                clean_groups()
                clean_friends()
                clean_wall()
                if select(['Clean', 'Stop'], 'Here you can stop cleaning or clean dialogs.') == 'Stop':
                    print('Dialogs not cleaned')
                    break
                clean_dialogs()
                print('Job finished.')
                break
        print('Cleaning cancelled.')