a1 = ["早上","中午","下午","晚上","深夜"]
a2 = ["朋友","家人","另一半","自己","同事"]
a3 = ["沒為什麼","送禮","想逛街","有需求","衝動性消費","本來沒有要去"]
a4 = ["大賣場","百貨公司","傳統市場","商圈","線上購物"]
a5 = ["生活用品","食物及食品","家電及3C產品","美妝護理品","車用品","服飾鞋包"]

f = open('心情1.txt', 'w', encoding='UTF-8')
for a in range(5):
    for b in range(5):
        for c in range(6):
            for d in range(5):
                for e in range(6):
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a2[b]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when who why where what\n")
                    f.write("今天"+a1[a]+"的時候，我和"+a2[b]+" 因為"+a3[c]+"，所以到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a2[b]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("who why where what\n")
                    f.write("我和"+a2[b]+" 因為"+a3[c]+"，所以到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when why where what\n")
                    f.write("今天"+a1[a]+"的時候，因為"+a3[c]+"，所以到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a2[b]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when who where what\n")
                    f.write("今天"+a1[a]+"的時候，我和"+a2[b]+" 到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a2[b]+" "+a3[c]+" "+a5[e]+"\n")
                    f.write("when who why what\n")
                    f.write("今天"+a1[a]+"的時候，我和"+a2[b]+" 因為"+a3[c]+"，去買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a3[c]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("why where what\n")
                    f.write("今天"+a3[c]+"，所以到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a4[d]+" "+a5[e]+"\n")
                    f.write("when where what\n")
                    f.write("今天"+a1[a]+"的時候，到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a2[b]+" "+a5[e]+"\n")
                    f.write("when who what\n")
                    f.write("今天"+a1[a]+"的時候，我和"+a2[b]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a4[d]+" "+a5[e]+"\n")
                    f.write("where what\n")
                    f.write("今天到"+a4[d]+" 買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a1[a]+" "+a5[e]+"\n")
                    f.write("when what\n")
                    f.write("今天"+a1[a]+"的時候，去買"+a5[e]+"\n")
                    f.write("\n")
                    f.write("心情1 購物\n")
                    f.write(a5[e]+"\n")
                    f.write("what\n")
                    f.write("今天去買"+a5[e]+"\n")
                    f.write("\n")
f.close()
