from django.http import HttpResponse
from django.shortcuts import render

def call(request):
    return render(request,"index.html")

def spi(request):
    marks=request.POST.get("mark","empty")
    lastspi=request.POST.get("lastspi","empty")
    point=request.POST.get("point","empty")
    select = request.POST.get("spic", "off")

    if select=="on":

        last_sem =lastspi

        JAVA, SE, TOC, WT, DOS = (marks).split(",")

        JAVAc, SEc, TOCc, WTc, DOSc =(point).split(",")

    ########################################################################
        mark = {}
        cre = {}
    ########################################################################
        AA = 10
        AB = 9
        BB = 8
        BC = 7
        CC = 6
        CD = 5
        DD = 4
        FAIL = 0
    ########################################################################
        mark['java'] = JAVA
        mark['se'] = SE
        mark['toc'] = TOC
        mark['dos'] = DOS
        mark['wt'] = WT
    ############################################################

        cre['javac'] = JAVAc
        cre['sec'] = SEc
        cre['tocc'] = TOCc
        cre['dosc'] = DOSc
        cre['wtc'] = WTc
        n =30
    ###############################################################
        for i, j in mark.items():
            pr = (int(j) * 100) / int(n)
            if pr > 85 and pr <= 100:
                mark[i] = AA
            elif pr <= 84 and pr > 75:
                mark[i] = AB
            elif pr <= 74 and pr > 65:
                mark[i] = BB
            elif pr <= 64 and pr > 55:
                mark[i] = BC
            elif pr <= 54 and pr > 45:
                mark[i] = CC
            elif pr <= 44 and pr > 40:
                mark[i] = CD
            elif pr <= 39 and pr >= 35:
                mark[i] = DD
            elif pr < 34:
                mark[i] = FAIL

        c = []
        b = []
        total = 0
        count = 0
        for i, j in mark.items():
            c.append(j)

        for l, m in cre.items():
            b.append(m)
        for i in c:
            mul = int(i) * int(b[count])
            total = int(total) + int(mul)
            count += 1
        credit = 0
        for i in b:
            credit = int(credit) + int(i)
        internal = total / credit
        external = (float(internal) + float(last_sem)) / 2

        mukesh = {'accepts': marks, 'aws': lastspi,"point":point,"internal":internal,"external":external}
        return render(request, "awnser.html", mukesh)
    else:
        return HttpResponse("ERROR :Plese Select SPI Count .")




