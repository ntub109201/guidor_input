a1 = ["某一天","某兩天","某三天","某四天","某五天"]
a2 = ["自己","家族","朋友","另一半"]
a3 = ["網路推薦","散心","聚會","興趣","拜訪親友"]
a4 = ["國外/亞洲", "國外/歐洲","國外/非洲","國外/北美洲","國外/南美洲","國外/南極洲","國內/北部","國內/中部","國內/南部","國內/東部","國內/離島"]
a5 = ["拍照攝影","夜遊","爬山","海邊","欣賞風景","餐廳"]
h1 = ["視覺/震撼","視覺/療癒","視覺/遼闊","視覺/狹隘","視覺/擁擠"]
h2 = ["嗅覺/芬多精","嗅覺/芬芳","嗅覺/清新","嗅覺/污染"]
h3 = ["味覺/美食文化","味覺/風俗","味覺/懷舊","味覺/宗教信仰"]
h4 = ["聽覺/寧靜","聽覺/嘈雜","聽覺/吵雜","聽覺/語言文化","聽覺/宗教信仰"]

f = open('心情5.txt', 'w', encoding='UTF-8')
for a in range(5):
    for b in range(4):
        for c in range(5):
            for d in range(11):
                for e in range(6):
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when who why where what\n")
                    f.write("在"+a1[a]+"期間，我和"+a2[b]+" 因為"+a3[c]+"，所以去了"+a4[d]+" 來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a2[b]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("who why where what\n")
                    f.write("我和"+a2[b]+"期間，因為"+a3[c]+"，所以去了"+a4[d]+" 來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when why where what\n")
                    f.write("在"+a1[a]+"期間，因為"+a3[c]+"，所以去了"+a4[d]+" 來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when who where what\n")
                    f.write("在"+a1[a]+"期間，我和"+a2[b]+" 去了"+a4[d]+" 來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a3[c]+" "+a5[e]+"\n")
                    f.write("when who why what\n")
                    f.write("在"+a1[a]+"期間，我和"+a2[b]+" 因為"+a3[c]+"，來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("why where what\n")
                    f.write("在"+a3[c]+"期間，所以到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when where what\n")
                    f.write("在"+a1[a]+"期間，去了"+a4[d]+" 來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a2[b]+" "+a5[e]+"\n")
                    f.write("when who what\n")
                    f.write("在"+a1[a]+"期間，我和"+a2[b]+" 來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a4[d]+" "+a5[e]+"\n")
                    f.write("where what\n")
                    f.write("在"+a4[d]+"期間，來"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情5 旅遊\n")
                    f.write(a1[a]+" "+a5[e]+"\n")
                    f.write("when what\n")
                    f.write("在"+a1[a]+"期間，來"+a5[e]+"\n")
                    f.write("\n")
f.close()
