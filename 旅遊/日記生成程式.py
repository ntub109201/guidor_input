a1 = ["1天","多天"]
a2 = ["自己","家人","朋友","另一半","同事"]
a3 = ["放鬆身心","拜訪親友","網路推薦","工作出差","挑戰刺激","休閒渡假","節慶"]
a4 = ["國外/亞洲","國外/歐洲","國外/北美洲","國外/南美洲","國外/南極洲","國內/北部","國內/中部","國內/南部","國內/東部","國內/離島"]
a5 = ["文化之旅","生態之旅","藝術之旅","海島之旅","自由行","公司活動","體育活動"]
h1 = ["視覺:震撼","視覺:療癒","視覺:遼闊","視覺:狹隘","視覺:擁擠","視覺:繽紛"]
h2 = ["嗅覺:芬多精","嗅覺:芬芳","嗅覺:清新","嗅覺:污染"]
h3 = ["味覺:美食文化","味覺:風俗","味覺:懷舊","味覺:宗教信仰"]
h4 = ["聽覺:寧靜","聽覺:嘈雜","聽覺:吵雜","聽覺:語言文化","聽覺:宗教信仰"]

f = open('心情5.txt', 'w', encoding='UTF-8')
for a in range(2):
    for b in range(5):
        for c in range(7):
            for d in range(10):
                for e in range(7):
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when who why where what\n")
                    f.write("在"+a1[a]+"中，我與"+a2[b]+"因為"+a3[c]+"，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a2[b]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("who why where what\n")
                    f.write("我與"+a2[b]+"因為"+a3[c]+"，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when why where what\n")
                    f.write("在"+a1[a]+"中，因為"+a3[c]+"，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when who where what\n")
                    f.write("在"+a1[a]+"中，我與"+a2[b]+"，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a3[c]+" "+a5[e]+"\n")
                    f.write("when who why what\n")
                    f.write("在"+a1[a]+"中，我與"+a2[b]+"因為"+a3[c]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("why where what\n")
                    f.write("因為"+a3[c]+"，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when where what\n")
                    f.write("在"+a1[a]+"中，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a5[e]+"\n")
                    f.write("when who what\n")
                    f.write("在"+a1[a]+"中，我與"+a2[b]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a4[d]+" "+a5[e]+"\n")
                    f.write("where what\n")
                    f.write("，到了"+a4[d]+"，體驗一場"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a5[e]+"\n")
                    f.write("when what\n")
                    f.write("在"+a1[a]+"中，體驗一場"+a5[e]+"\n")
                    f.write("\n")
f.close()
