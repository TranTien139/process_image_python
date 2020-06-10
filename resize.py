import cv2
import time
from PIL import Image
import os
import json


def resize_image(path, newpath):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    # width = 194
    width = 750
    height = (width / img.shape[1]) * img.shape[0]
    dim = (width, int(height))
    # print(dim, "dim")
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # resized = resized[7: 180, 17:180]
    cv2.imwrite(newpath, resized)
    # print('success: ', id)


# for i in range(1, 262):
#     resize_image(i)
#     time.sleep(2)


def get_star(str):
    if str == 'Kim':
        return 'Metal'
    if str == 'Thổ':
        return 'Earth'
    if str == 'Hỏa':
        return 'Fire'
    if str == 'Mộc':
        return 'Wood'
    if str == 'Thủy':
        return 'Water'
    return ''

def get_star_number(str):
    if str == 'Kim':
        return 1
    if str == 'Thổ':
        return 5
    if str == 'Hỏa':
        return 4
    if str == 'Mộc':
        return 2
    if str == 'Thủy':
        return 3
    return 0

def get_skill(str):
    if str == 'Goku':
        return [100, 100, 100, 100, 100, 80, 100]
    if str == 'Vegeta':
        return [95, 90, 100, 100, 100, 100, 100]
    if str == 'Krillin':
        return [50, 50, 40, 70, 100, 85, 100]
    if str == 'Frieza':
        return [80, 90, 80, 80, 70, 60, 70]
    if str == 'Beerus':
        return [500, 500, 500, 500, 100, 55, 100]
    if str == 'Android 18':
        return [75, 70, 90, 100, 90, 100, 90]
    if str == 'Broly':
        return [90, 90, 150, 100, 100, 80, 100]
    if str == 'Bulma':
        return [5, 5, 5, 5, 100, 80, 100]
    if str == 'Ginyu':
        return [20, 10, 20, 20, 60, 30, 60]
    if str == 'Jiren':
        return [90, 100, 120, 90, 100, 80, 100]
    if str == 'Kid Buu':
        return [75, 75, 90, 100, 80, 60, 80]
    if str == 'Majin Buu':
        return [75, 75, 90, 100, 85, 70, 85]
    if str == 'Master Roshi':
        return [30, 20, 25, 30, 90, 60, 90]
    if str == 'Mercenary Tao':
        return [10, 10, 10, 10, 20, 30, 20]
    if str == 'Piccolo':
        return [70, 70, 80, 80, 100, 80, 100]
    if str == 'Son Gohan':
        return [80, 90, 90, 90, 100, 100, 100]
    if str == 'Son Goten':
        return [60, 70, 70, 80, 100, 80, 100]
    if str == 'Tien Shinhan':
        return [45, 45, 40, 40, 100, 80, 100]
    if str == 'Yamcha':
        return [25, 25, 20, 25, 100, 70, 100]
    if str == 'Zarbon':
        return [30, 20, 30, 30, 80, 70, 80]
    return [0, 0, 0, 0, 0, 0, 0]

def gender_json_image():
    path = './image'
    files = os.listdir(path)
    k = 0
    for name in files:
        pathSub = path + '/' + name
        filesChild = None
        if name != '.gitkeep':
            filesChild = os.listdir(pathSub)
        if filesChild:
            for nameSub in filesChild:
                try:
                    arrName = nameSub.split('.')
                    id = arrName[0].strip()
                    id = int(id)
                    if id > 10:
                        id = id - 2
                    if id < 10:
                        id = '200' + str(id)
                    else:
                        id = '20' + str(id)
                    id = id + str(get_star_number(name))

                    nameCharacter = arrName[1].strip()
                    star = get_star(name)
                    skill = get_skill(nameCharacter)

                    pathSub1 = path + '/' + name + '/' + nameSub
                    filesChild1 = os.listdir(pathSub1)
                    for nameSub1 in filesChild1:
                        level = nameSub1.split('-')
                        if level[1]:
                            level = level[1].replace('.jpg', '').replace('.png', '')
                        idFinal = id + level
                        resize_image(path + '/' + name + '/' + nameSub + '/' + nameSub1, './resize' + '/' + idFinal + '.jpg')
                        metadata = {
                            "skill": 0,
                            "speed": 0,
                            "power": 0,
                            "endurance": 0,
                            "loyalty": skill[4],
                            "charm": skill[5],
                            "love": skill[6],
                            "luck": None,
                            "longevity": None,
                            "health": 100,
                            "age": 0,
                            "sex": None,
                            "star": star,
                            "race": "Dragon Ball",
                            "level": 0,
                            "id": idFinal,
                            "name": nameCharacter + ' ' + level,
                            "description": "DragonSphere Character NFT: " + nameCharacter + ' ' + level,
                            "image": "https://m721.midasprotocol.com/dragonsphere/" + idFinal + ".png",
                        }
                        data = {
                            "id": idFinal,
                            "name": nameCharacter + ' ' + level,
                            "description": "DragonSphere Character NFT: " + nameCharacter + ' ' + level,
                            "image": "https://m721.midasprotocol.com/dragonsphere/" + idFinal + ".png",
                            "metadata": json.dumps(metadata)
                        }
                        # with open('./json/' + idFinal + ".json", 'w+') as f:
                        #     json.dump(data, f)
                        k+=1
                        print(nameSub, idFinal, k)
                except Exception as e:
                    print('error', e)

def gender_json_level0():
    path = './level0'
    files = os.listdir(path)
    k = 0
    for name in files:
        pathSub = path + '/' + name
        filesChild = os.listdir(pathSub)
        if filesChild:
            for nameSub in filesChild:
                try:
                    nameSub = nameSub.replace('.jpg','')
                    arrName = nameSub.split('.')
                    id = arrName[0].strip()
                    id = int(id)
                    if id > 10:
                        id = id - 2
                    if id < 10:
                        id = '200' + str(id)
                    else:
                        id = '20' + str(id)
                    id = id + str(get_star_number(name))

                    nameCharacter = arrName[1].strip()
                    star = get_star(name)
                    skill = get_skill(nameCharacter)

                    idFinal = id + '00'
                    # resize_image(path + '/' + name + '/' + nameSub + '.jpg', './resize' + '/' + idFinal + '.jpg')
                    metadata = {
                        "skill": 0,
                        "speed": 0,
                        "power": 0,
                        "endurance": 0,
                        "loyalty": skill[4],
                        "charm": skill[5],
                        "love": skill[6],
                        "luck": None,
                        "longevity": None,
                        "health": 100,
                        "age": 0,
                        "sex": None,
                        "star": star,
                        "race": "Dragon Ball",
                        "level": 0,
                        "id": idFinal,
                        "name": nameCharacter,
                        "description": "DragonSphere Character NFT: " + nameCharacter,
                        "image": "https://m721.midasprotocol.com/dragonsphere/" + idFinal + ".png",
                    }
                    data = {
                        "id": idFinal,
                        "name": nameCharacter,
                        "description": "DragonSphere Character NFT: " + nameCharacter,
                        "image": "https://m721.midasprotocol.com/dragonsphere/" + idFinal + ".png",
                        "metadata": json.dumps(metadata)
                    }
                    with open('./json/' + idFinal + ".json", 'w+') as f:
                        json.dump(data, f)
                    k+=1
                    print(nameSub, idFinal, k)
                except Exception as e:
                    print('error', e)

def getNumberId(str):
    if str == '01-01':
        return '01'
    if str == '01-02':
        return '02'
    if str == '01-03':
        return '03'
    if str == '01-04':
        return '04'
    if str == '01-05':
        return '05'
    if str == '01-06':
        return '06'
    if str == '01-07':
        return '07'
    if str == '01-08':
        return '08'
    if str == '01-09':
        return '09'
    if str == '01-10':
        return '10'
    if str == '11-01':
        return '11'
    if str == '11-02':
        return '12'
    if str == '11-03':
        return '13'
    if str == '11-04':
        return '14'
    if str == '11-05':
        return '15'
    if str == '11-06':
        return '16'
    if str == '11-07':
        return '17'
    if str == '11-08':
        return '18'
    if str == '11-09':
        return '19'
    if str == '11-10':
        return '20'
    return ''

def gender_json_image_level01():
    path = './level01'
    files = os.listdir(path)
    k = 0
    for name in files:
        pathSub = path + '/' + name
        filesChild = os.listdir(pathSub)
        if filesChild:
            for nameSub in filesChild:
                try:
                    nameSub = nameSub.replace('.jpg','').strip()
                    id = getNumberId(nameSub)
                    idFinal = '20' + id + str(get_star_number(name)) + '00'
                    resize_image(path + '/' + name + '/' + nameSub + '.jpg', './resize' + '/' + idFinal + '.jpg')
                    k+=1
                    print(nameSub, idFinal, k)
                except Exception as e:
                    print('error', e)
        else:
            print('no chil file')

def get_number_by_name(str):
    str = str.strip()
    str = str.lower()
    if 'goku' in str:
        return 1
    if 'vegeta' in str:
        return 2
    if 'krillin' in str:
        return 3
    if 'frieza' in str:
        return 4
    if 'beerus' in str:
        return 5
    if 'android' in str:
        return 6
    if 'broly' in str:
        return 7
    if 'bulma' in str:
        return 8
    if 'ginyu' in str:
        return 9
    if 'jiren' in str:
        return 10
    if 'kid' in str:
        return 11
    if 'majin' in str:
        return 12
    if 'master' in str:
        return 13
    if 'mercenary' in str:
        return 14
    if 'piccolo' in str:
        return 15
    if 'gohan' in str:
        return 16
    if 'goten' in str:
        return 17
    if 'shinhan' in str:
        return 18
    if 'yamcha' in str:
        return 19
    if 'zarbon' in str:
        return 20
    return 0

def gender_json_image_circle():
    path = './circle'
    files = os.listdir(path)
    k = 0
    for name in files:
        pathSub = path + '/' + name
        filesChild = None
        if name != '.gitkeep' and name != '.DS_Store':
            filesChild = os.listdir(pathSub)
        star = str(get_star_number(name))
        if filesChild:
            for nameSub in filesChild:
                try:
                    pathSub1 = path + '/' + name + '/' + nameSub
                    filesChild1 = os.listdir(pathSub1)
                    for nameSub1 in filesChild1:
                        nameCharacter = nameSub1.split('-')
                        level = nameCharacter[1]
                        level = level.replace('.png','').replace('.jpg', '')

                        id = get_number_by_name(nameSub1)
                        if id != 0:
                            if id < 10:
                                id = '200' + str(id)
                            else:
                                id = '20' + str(id)
                            if level == '01':
                                idFinal = id + star + '00'
                                resize_image(path + '/' + name + '/' + nameSub + '/' + nameSub1, './resize' + '/' + idFinal + '.png')
                                print(level, idFinal, k)
                                k+=1
                        else:
                            print(name, nameSub1)
                except Exception as e:
                    print('error', e)

gender_json_image()
# gender_json_image_circle()
# gender_json_image_level01()
# gender_json_level0()