import numpy as np
import cv2
import os
import MySQLdb as mdb
import sys

cap = cv2.VideoCapture(0)
try:
    con = mdb.connect('localhost', 'root', 'root', 'akilliOtopark');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print "Database version : %s " % ver

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    # Kamera frame algılama
    ret, frame = cap.read()

    #Filtreler uygulandı
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #Görüntü düzleştirme
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #kenar belirleme
    canny = cv2.Canny(blurred, 100, 100)
    cv2.imshow('Ori>Gray>Blur>Canny', canny)

    #Alanların belirlenmesi
    # img[y: y + h, x: x + w]
    crop_img8 = canny[40:130, 90:170]
    crop_img7 = canny[40:130, 205:305]
    crop_img6 = canny[40:130, 330:440]
    crop_img5 = canny[40:130, 470:555]

    crop_img4 = canny[150:290, 55:145]
    crop_img3 = canny[150:290, 185:300]
    crop_img2 = canny[150:290, 329:453]
    crop_img1 = canny[150:290, 488:575]


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

    
    duzCizgiFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.line(duzCizgiFrame, (83, 32), (18, 315), (255, 0, 0), 5)
    cv2.line(duzCizgiFrame, (196, 32), (160, 315), (255, 0, 0), 5)
    cv2.line(duzCizgiFrame, (321, 32), (320, 315), (255, 0, 0), 5)
    cv2.line(duzCizgiFrame, (442, 32), (482, 315), (255, 0, 0), 5)
    cv2.line(duzCizgiFrame, (551, 32), (618, 315), (255, 0, 0), 5)
    cv2.line(duzCizgiFrame, (45, 145), (585, 145), (255, 0, 0), 5) #OrtaÇizgi
    cv2.putText(duzCizgiFrame, "8", (106, 71), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "7", (220, 71), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "6", (341, 71), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "5", (468, 71), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "4", (60, 340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "3", (212, 340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "2", (365, 340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))
    cv2.putText(duzCizgiFrame, "1", (512, 340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (225, 0, 0))

    # Görüntüleme ekranı
    sonEkran = cv2.resize(duzCizgiFrame, (480, 320))
    cv2.resizeWindow('Akıllı otopark', 480, 320)
    cv2.imshow('Akıllı otopark',sonEkran)
    cv2.waitKey(250)

cap.release()
cv2.destroyAllWindows()


