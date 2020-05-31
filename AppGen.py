import os
import shutil

def agen(apath, dst):
    files = []

    dware = os.path.join(dst, 'dsiware')
    if os.path.exists(dware):
        shutil.rmtree(dware)
    os.mkdir(dware)

    num = 0

    for app in os.listdir(apath):
        apps = apath + '\\' + app
        try:
            for title in os.listdir(apps + '\\' + 'content'):
                if title.endswith('.app'):
                    if app != '53524c41' and app != '484e474a' and app != '534c524e' :
                        print('{}\content\{}'.format(app, title))
                    shutil.copy(apath + '\{}\content\{}'.format(app, title), dware)
                    os.rename(dware + '\{}'.format(title), dware + '\{}.nds'.format(app))
                    num += 1
        except:
            pass

        try:
            for titleid in os.listdir(apps + '\\' + 'data'):
                if titleid.endswith('.sav'):
                    if titleid.startswith('pri'):
                        if app != '484e474a':
                            print('{}\data\{}'.format(app, titleid))
                        shutil.copy(apath + '\{}\data\{}'.format(app, titleid), dware)
                        os.rename(dware + '\{}'.format(titleid), dware + '\{}.prv'.format(app))
                    if titleid.startswith('pub'):
                        print('{}\data\{}'.format(app, titleid))
                        shutil.copy(apath + '\{}\data\{}'.format(app, titleid), dware)
                        os.rename(dware + '\{}'.format(titleid), dware + '\{}.pub'.format(app))
        except:
            pass

    if os.path.exists(dware + '\\' + '484e474a.prv'):
        files.append(dware + '\\' + '484e474a.prv')
    if os.path.exists(dware + '\\' + '484e474a.nds'):
        files.append(dware + '\\' + '484e474a.nds')
    if os.path.exists(dware + '\\' + '534c524e.nds'):
        files.append(dware + '\\' + '534c524e.nds')
    if os.path.exists(dware + '\\' + '53524c41.nds'):
        files.append(dware + '\\' + '53524c41.nds')

    while len(files) > 0:
        try:
            os.remove(files.pop())
        except:
            pass

    if num == 0:
        shutil.rmtree(dware)

if __name__ == '__main__':
    agen(os.getcwd(), os.getcwd())
