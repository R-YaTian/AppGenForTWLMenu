import os
import shutil

if os.path.exists("dsiware"):
    shutil.rmtree("dsiware")
os.mkdir("dsiware")

num = 0

for app in os.listdir():
    try:
        for titleid in os.listdir(app + "/data/"):
            if titleid.endswith(".sav"):
                if titleid.startswith("pri"):
                    print("/{}/data/{}".format(app, titleid))
                    shutil.copy("{}/data/{}".format(app, titleid), "dsiware")
                    os.rename("dsiware/{}".format(titleid), "dsiware/{}.prv".format(app))
                if titleid.startswith("pub"):
                    print("/{}/data/{}".format(app, titleid))
                    shutil.copy("{}/data/{}".format(app, titleid), "dsiware")
                    os.rename("dsiware/{}".format(titleid), "dsiware/{}.pub".format(app))
        for title in os.listdir(app + "/content/"):
            if title.endswith(".app"):
                print("/{}/content/{}".format(app, title))
                shutil.copy("{}/content/{}".format(app, title), "dsiware")
                os.rename("dsiware/{}".format(title), "dsiware/{}.nds".format(app))
                num += 1
        os.remove("dsiware/484e474a.prv")
        os.remove("dsiware/484e474a.nds")
        os.remove("dsiware/534c524e.nds")
        os.remove("dsiware/53524c41.nds")
    except:
        pass

if num == 0:
    shutil.rmtree("dsiware")
