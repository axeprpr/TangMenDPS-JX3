import random
import os
import math
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')

def DPS(request):
    ATK=float(request.GET['ATK'])
    CR=float(request.GET['CR'])
    CD=float(request.GET['CD'])
    UTR=float(request.GET['UTR'])
    UHR=float(request.GET['UHR'])
    DD=float(request.GET['DD'])
    WD_max=float(request.GET['WD_max'])
    WD_min=float(request.GET['WD_min'])
    ggcd=float(request.GET['ggcd'])
    DDP=float(request.GET['DDP'])
    mzfy=float(request.GET['mzfy'])
    dafumo=float(request.GET['dafumo'])
    ZM_CD=float(request.GET['ZM_CD'])
    dp_ex_dmg=float(request.GET['dp_ex_dmg'])
    zm_ex_dmg=float(request.GET['zm_ex_dmg'])
    zx_ex_dmg=float(request.GET['zx_ex_dmg'])
    by_ex_dmg=float(request.GET['by_ex_dmg'])
    hx_ex_dmg=float(request.GET['hx_ex_dmg'])
    cx_ex_dmg=float(request.GET['cx_ex_dmg'])
    zm_ex_CR=float(request.GET['zm_ex_CR'])
    zm_ex_CD=float(request.GET['zm_ex_CD'])
    dp_ex_CR=float(request.GET['dp_ex_CR'])
    dp_ex_CD=float(request.GET['dp_ex_CD'])
    by_ex_CR=float(request.GET['by_ex_CR'])
    by_ex_CD=float(request.GET['by_ex_CD'])
    zx_ex_CR=float(request.GET['zx_ex_CR'])
    zx_ex_CD=float(request.GET['zx_ex_CD'])
    zx_t3=int(request.GET['zx_t3'])
    dot_cd=float(request.GET['dot_cd'])    
    by_qp=request.GET['by_qp']    

    xw_ggcd=1.19
    sum =0
    timeall = ggcd*2
    zm_count,zx_count,dp_count,xw_count,by_count,gf_count= 0,0,0,0,0,0
    zm_cd,zx_cd,by_cd,xw_cd = 0,0,0,0
    wusheng = 0

    for count in range(0,100000):
        if (xw_cd<=0):
            xw_cx = 0
            xw_cd = 90
            xw_count += 1
	    while (xw_cx <=15):
                if (zm_cd<=0 and wusheng>=3):
                    sum += yuanzhuo(UHR,UTR,CR+0.2+zm_ex_CR,CD+zm_ex_CD,zhuiming_1(WD_min,WD_max,ATK,zm_ex_dmg))
                    sum += yuanzhuo(UHR,UTR,CR+0.2+zm_ex_CR,CD+zm_ex_CD,zhuiming_2(WD_min,WD_max,ATK,zm_ex_dmg))
                    timeall += xw_ggcd
                    xw_cx += xw_ggcd
                    zm_count += 1
                    gf_count += 2
                    wusheng = 0
                    zm_cd = ZM_CD-xw_ggcd
                    if (zx_cd >0):zx_cd -= xw_ggcd
                    if (by_cd >0):by_cd -= xw_ggcd
                    if (xw_cd >0):xw_cd -= xw_ggcd
                    if (random.randint(0,10)<4):
                        sum += yuanzhuo(UHR,UTR,CR+0.2+zm_ex_CR,CD+zm_ex_CD,zhuiming_1(WD_min,WD_max,ATK,zm_ex_dmg))
                        sum += yuanzhuo(UHR,UTR,CR+0.2+zm_ex_CR,CD+zm_ex_CD,zhuiming_2(WD_min,WD_max,ATK,zm_ex_dmg))
                        timeall += xw_ggcd
                        xw_cx += xw_ggcd
                        zm_count += 1
                        gf_count += 1
                        zm_cd = ZM_CD-xw_ggcd
                        if(zx_cd>0):zx_cd -= xw_ggcd
                        if(by_cd>0):by_cd -= xw_ggcd
                        if(xw_cd>0):xw_cd -= xw_ggcd
                        if (random.randint(0,10)<4):
                            zm_cd =0
                if (zx_cd<=0):
                    sum += yuanzhuo(UHR,UTR,CR+0.2+zx_ex_CR,CD+zx_ex_CD,zhuxing_1(WD_min,WD_max,ATK,zx_ex_dmg))
                    for zhuxingDOT in range(0,4+zx_t3):
                        sum += yuanzhuo(UHR,UTR,CR+0.2+zx_ex_CR,CD+zx_ex_CD,zhuxing_2(ATK))
                    timeall += xw_ggcd
                    xw_cx += xw_ggcd
                    zx_count += 1
                    gf_count += 2
                    zx_cd = 10-xw_ggcd
                    if(zm_cd>0):zm_cd -= xw_ggcd
                    if(by_cd>0):by_cd -= xw_ggcd
                    if(xw_cd>0):xw_cd -= xw_ggcd
                sum += yuanzhuo(UHR,UTR,CR+0.2+dp_ex_CR,CD+0.2+dp_ex_CD,duopo(WD_min,WD_max,ATK,dp_ex_dmg))
                timeall += xw_ggcd
                xw_cx += xw_ggcd
                wusheng += 1
                dp_count += 1
                gf_count += 1
                if(zm_cd>0):zm_cd -= xw_ggcd
                if(zx_cd>0):zx_cd -= xw_ggcd
                if(by_cd>0):by_cd -= xw_ggcd
                if(xw_cd>0):xw_cd -= xw_ggcd
                if(dafumo==1):zm_cd -= 1
 
        if (zm_cd<=0 and wusheng>=3):
            sum += yuanzhuo(UHR,UTR,CR+zm_ex_CR,CD+zm_ex_CD,zhuiming_1(WD_min,WD_max,ATK,zm_ex_dmg))
            sum += yuanzhuo(UHR,UTR,CR+zm_ex_CR,CD+zm_ex_CD,zhuiming_2(WD_min,WD_max,ATK,zm_ex_dmg))
            timeall += ggcd
            zm_count += 1
            gf_count += 2
            wusheng = 0
            zm_cd = ZM_CD-ggcd
            if (zx_cd >0):zx_cd -= ggcd
            if (by_cd >0):by_cd -= ggcd
            if (xw_cd >0):xw_cd -= ggcd
            if (random.randint(0,10)<4):
                sum += yuanzhuo(UHR,UTR,CR+zm_ex_CR,CD+zm_ex_CD,zhuiming_1(WD_min,WD_max,ATK,zm_ex_dmg))
                sum += yuanzhuo(UHR,UTR,CR+zm_ex_CR,CD+zm_ex_CD,zhuiming_2(WD_min,WD_max,ATK,zm_ex_dmg))
                timeall += ggcd
                zm_count += 1
                gf_count += 1
                zm_cd = ZM_CD-ggcd
                if(zx_cd >0):zx_cd -= ggcd
                if(by_cd >0):by_cd -= ggcd
                if(xw_cd >0):xw_cd -= ggcd
                if (random.randint(0,10)<4):
                    zm_cd = 0
            
        if (zx_cd<=0):
            sum += yuanzhuo(UHR,UTR,CR+zx_ex_CR,CD+zx_ex_CD,zhuxing_1(WD_min,WD_max,ATK,zx_ex_dmg))
            for zhuxingDOT in range(0,4+zx_t3):
                sum += yuanzhuo(UHR,UTR,CR+zx_ex_CR,CD+zx_ex_CD,zhuxing_2(ATK))
            timeall += ggcd
            zx_count += 1
            gf_count += 2
            zx_cd = 10-ggcd
            if(zm_cd>0):zm_cd -= ggcd
            if(by_cd>0):by_cd -= ggcd
            if(xw_cd>0):xw_cd -= ggcd
            
        if (by_cd<=0 and by_qp=="On"):
            for baoyuDOT in range(0,3):
                sum += yuanzhuo(UHR,UTR,CR+by_ex_CR,CD+by_ex_CD,baoyu(ATK,by_ex_dmg))
            timeall += ggcd
            by_cd = 60-ggcd
            by_count += 1
            gf_count += 1 
            if(zm_cd>0):zm_cd -= ggcd
            if(zx_cd>0):zx_cd -= ggcd
            if(xw_cd>0):xw_cd -= ggcd
            
        sum += yuanzhuo(UHR,UTR,CR+dp_ex_CR,CD+dp_ex_CD,duopo(WD_min,WD_max,ATK,dp_ex_dmg))
        timeall += ggcd
        wusheng += 1
        dp_count += 1
        gf_count += 1
        if(zm_cd>0):zm_cd -= ggcd
        if(zx_cd>0):zx_cd -= ggcd
        if(by_cd>0):by_cd -= ggcd
        if(xw_cd>0):xw_cd -= ggcd
        if(dafumo==1):zm_cd -= 1

    for dot in range(0,int(timeall/dot_cd)):
        sum += yuanzhuo(UHR,UTR,CR,CD,huaxue(ATK,hx_ex_dmg))
        sum += yuanzhuo(UHR,UTR,CR,CD,huaxue(ATK,cx_ex_dmg))
    for gf in range(0,gf_count):
        sum += yuanzhuo(UHR,UTR,CR,CD,gangfeng(WD_min,WD_max,ATK))
#   return HttpResponse(sum/timeall*(1+DD)*mzfy*DDP)
    dps_dict = {'sum':sum,'timeall':timeall,'dps':sum/timeall*(1+DD)*mzfy*DDP,'xw_count':xw_count,'zm_count':zm_count,'dp_count':dp_count,'zx_count':zx_count,'by_count':by_count,'gf_count':gf_count}    
    return HttpResponse(json.dumps(dps_dict), content_type='application/json')
def yuanzhuo(UHR,UTR,CR,CD,Per_Ability_DPS):
    if((1-UHR-UTR)>=CR):
        yuanzhuo_CR = CR
    else:
        yuanzhuo_CR = 1-UHR-UTR
 
    roll = random.uniform(0,1)
 
    if(roll<UHR):
        Per_Ability_DPS = 0
        Sign = "Unhit"
    elif(roll<(UTR+UHR)):
        Per_Ability_DPS /= 4.0
        Sign = "Through"
    elif(roll<(yuanzhuo_CR+UTR+UHR)):
        Per_Ability_DPS *= CD
        Sign = "Crit"
    else:
        Per_Ability_DPS = Per_Ability_DPS 
        Sign = "Attack"
    return Per_Ability_DPS
    
#def skill
def duopo(WD_min,WD_max,ATK,dp_ex_dmg):
    DPS_duopo = (random.randint(WD_min,WD_max)*2+random.randint(255,275)+(1.486404-0.2)*ATK)*dp_ex_dmg
    return DPS_duopo
def zhuiming_1(WD_min,WD_max,ATK,zm_ex_dmg):
    DPS_zhuiming_1 = (random.randint(WD_min,WD_max)*3 + random.randint(285,315)+(2.169184-0.3)*ATK)*zm_ex_dmg
    return DPS_zhuiming_1
def zhuiming_2(WD_min,WD_max,ATK,zm_ex_dmg):
    DPS_zhuiming_2 = (random.randint(WD_min,WD_max)*3 + random.randint(285,315)+(2.169184-0.3)*ATK)*0.7*zm_ex_dmg
    return DPS_zhuiming_2
def huaxue(ATK,hx_ex_dmg):
    DPS_huaxue = (24 + 0.450151*ATK)*hx_ex_dmg
    return DPS_huaxue
def huaxue(ATK,cx_ex_dmg):
    DPS_chuanxin = (18 + 0.123867*ATK)*cx_ex_dmg
    return DPS_chuanxin
def zhuxing_1(WD_min,WD_max,ATK,zx_ex_dmg):
    DPS_zhuxing1 = (random.randint(WD_min,WD_max)*1+random.randint(104,114)+(0.848942-0.1)*ATK)*zx_ex_dmg
    return DPS_zhuxing1
def zhuxing_2(ATK):
    DPS_zhuxing2 = ATK*0.5
    return DPS_zhuxing2
def baoyu(ATK,by_ex_dmg):
    DPS_baoyu = (random.randint(175,180)+0.187311*ATK)*by_ex_dmg
    return DPS_baoyu
def gangfeng(WD_min,WD_max,ATK):
    DPS_gangfeng = (random.randint(WD_min,WD_max))*1.2+ATK*0.2
    return DPS_gangfeng       
    
