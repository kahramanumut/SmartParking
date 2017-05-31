import cv2
import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost', 'root', 'root', 'akilliOtopark');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print "Database version : %s " % ver

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

i =9

while True:
    original = cv2.imread(str(i)+'.jpg')
    cv2.imshow('Original', original)
    gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 100, 100)
    cv2.imshow('Ori>Gray>Blur>Canny', canny)

    #img[y: y + h, x: x + w]
    crop_img1 = canny[65:202, 1:96]
    crop_img2 = canny[65:202, 105:200]
    crop_img3 = canny[65:202, 209:304]
    crop_img4 = canny[65:202, 313:408]

    crop_img5 = canny[212:340,  1:96]
    crop_img6 = canny[212:340, 105:200]
    crop_img7 = canny[212:340, 209:304]
    crop_img8 = canny[212:340, 313:408]

    ''' cv2.imshow('Lot1', crop_img1)
    cv2.imshow('Lot2', crop_img2)
    cv2.imshow('Lot3', crop_img3)
    cv2.imshow('Lot4', crop_img4)
    cv2.imshow('Lot5', crop_img5)
    cv2.imshow('Lot6', crop_img6)
    cv2.imshow('Lot7', crop_img7)
    cv2.imshow('Lot8', crop_img8) '''

    park1 = cv2.countNonZero(crop_img1)
    park2 = cv2.countNonZero(crop_img2)
    park3 = cv2.countNonZero(crop_img3)
    park4 = cv2.countNonZero(crop_img4)
    park5 = cv2.countNonZero(crop_img5)
    park6 = cv2.countNonZero(crop_img6)
    park7 = cv2.countNonZero(crop_img7)
    park8 = cv2.countNonZero(crop_img8)

    print("1:" + str(park1))
    print("2:" + str(park2))
    print("3:" + str(park3))
    print("4:" + str(park4))
    print("5:" + str(park5))
    print("6:" + str(park6))
    print("7:" + str(park7))
    print("8:" + str(park8))

    if park1 > 200:
        park_yeri1 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 1"
    else:
        park_yeri1 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 1"

    if park2 > 200:
        park_yeri2 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 2"
    else:
        park_yeri2 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 2"

    if park3 > 200:
        park_yeri3 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 3"
    else:
        park_yeri3 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 3"

    if park4 > 200:
        park_yeri4 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 4"
    else:
        park_yeri4 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 4"

    if park5 > 200:
        park_yeri5 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 5"
    else:
        park_yeri5 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 5"

    if park6 > 200:
        park_yeri6 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 6"
    else:
        park_yeri6 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 6"

    if park7 > 200:
        park_yeri7 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 7"
    else:
        park_yeri7 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 7"

    if park8 > 200:
        park_yeri8 = "UPDATE `park` SET `Durum` = 'D' WHERE `park`.`ID` = 8"
    else:
        park_yeri8 = "UPDATE `park` SET `Durum` = 'B' WHERE `park`.`ID` = 8"

    with con:
        cur = con.cursor()
        cur.execute(park_yeri1)
        cur.execute(park_yeri2)
        cur.execute(park_yeri3)
        cur.execute(park_yeri4)
        cur.execute(park_yeri5)
        cur.execute(park_yeri6)
        cur.execute(park_yeri7)
        cur.execute(park_yeri8)

    '''if i > 8:
    i = 1
   else:
     i = i + 1'''

    cv2.waitKey(10000)
    cv2.destroyAllWindows()

