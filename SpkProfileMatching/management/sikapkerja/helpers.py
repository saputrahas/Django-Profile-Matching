import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 

def get_gap(df, target):
    for idx in range(0,len(df)):
        df.loc[idx] = df.loc[idx] - target
    return df

def bobot(x):
    if x == 0 : return 5
    elif x == 1 : return 4.5
    elif x == -1 : return 4
    elif x == 2 : return 3.5
    elif x == -2 : return 3 
    elif x == 3 : return 2.5
    elif x == -3 : return 2
    elif x == 4 : return 1.5
    elif x == -4 : return 1
    
def pembobotan(df, cols):
    for c in cols:
        df[c] = df[c].apply(bobot)
    return df 

#mendapatkan nilai core factor
def get_cfsf(df1):
    total_column = len(df1.columns)
    cfsf = df1.sum(axis=1) / total_column
    return cfsf

#perhitungan nilai total
def result(cf, sf):
    cf = cf*0.6
    sf = sf*0.4
    total = cf + sf
    return total

def ListSikapKerja(krywn):
    if len(krywn)>0:
        target = [3,4,2,3,3]
        cols = ['energi_psikis','ketelitian','kehati_hatian','pengendalian_prasaan','dorongan_berprestasi']

        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)

        sk = {
            cols[0] : [int(a.sikapkerjas.energi_psikis) for a in krywn],
            cols[1] : [int(a.sikapkerjas.ketelitian) for a in krywn],
            cols[2] : [int(a.sikapkerjas.kehati_hatian) for a in krywn],
            cols[3] : [int(a.sikapkerjas.pengendalian_prasaan) for a in krywn],
            cols[4] : [int(a.sikapkerjas.dorongan_berprestasi) for a in krywn],


        }
        dfsk = pd.DataFrame(data=sk)

        gap = get_gap(dfsk, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []


def CfSikapKerja(krywn):
    if len(krywn)>0:
        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)

        target = [4,3]
        cols = ['ketelitian','pengendalian_prasaan']
        sk = {
            cols[0] : [int(a.sikapkerjas.ketelitian) for a in krywn],
            cols[1] : [int(a.sikapkerjas.pengendalian_prasaan) for a in krywn],
        }
        dfsk = pd.DataFrame(data=sk)

        gap = get_gap(dfsk, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []

def SfSikapKerja(krywn):
    if len(krywn)>0:
        
        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)
        target = [3,2,3]
        cols = ['energi_psikis','kehati_hatian','dorongan_berprestasi']
        sk = {
            cols[0] : [int(a.sikapkerjas.energi_psikis) for a in krywn],
            cols[1] : [int(a.sikapkerjas.kehati_hatian) for a in krywn],
            cols[2] : [int(a.sikapkerjas.dorongan_berprestasi) for a in krywn],


        }
        dfsk = pd.DataFrame(data=sk)

        gap = get_gap(dfsk, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []


def NiCfSik(krywn):
    
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    target = [4,3]
    cols = ['ketelitian','pengendalian_prasaan']
    cf = {
        cols[0] : [int(a.sikapkerjas.ketelitian) for a in krywn],
        cols[1] : [int(a.sikapkerjas.pengendalian_prasaan) for a in krywn],
    }
 
    dfcf = pd.DataFrame(data=cf)
    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfcfkrn, total], axis=1)
    return new

def NiSfSik(krywn):
       
    sfkrn = {'nama': [a.nama for a in krywn]}
    dfsfkrn = pd.DataFrame(data=sfkrn)    
    target = [3,2,3]
    cols = ['energi_psikis','kehati_hatian','dorongan_berprestasi']
    sf = {
        cols[0] : [int(a.sikapkerjas.energi_psikis) for a in krywn],
        cols[1] : [int(a.sikapkerjas.kehati_hatian) for a in krywn],
        cols[2] : [int(a.sikapkerjas.dorongan_berprestasi) for a in krywn],


    }
    dfsf = pd.DataFrame(data=sf)
    gap = get_gap(dfsf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfsfkrn, total], axis=1)
    return new


def TotalSik(krywn):
    krn = {'nama': [a.nama for a in krywn]}
    dfkrn = pd.DataFrame(data=krn)

    targetcf = [4,3]
    colscf = ['ketelitian','pengendalian_prasaan']
    cf = {
        colscf[0] : [int(a.sikapkerjas.ketelitian) for a in krywn],
        colscf[1] : [int(a.sikapkerjas.pengendalian_prasaan) for a in krywn],
    }
    dfcf = pd.DataFrame(data=cf)
    gapcf = get_gap(dfcf, targetcf)
    pbcf = pembobotan(gapcf, colscf)
    totalcf = get_cfsf(pbcf)


    targetsf = [3,2,3]
    colssf = ['energi_psikis','kehati_hatian','dorongan_berprestasi']
    sf = {
        colssf[0] : [int(a.sikapkerjas.energi_psikis) for a in krywn],
        colssf[1] : [int(a.sikapkerjas.kehati_hatian) for a in krywn],
        colssf[2] : [int(a.sikapkerjas.dorongan_berprestasi) for a in krywn],
    }
    dfsf = pd.DataFrame(data=sf)
    gapsf = get_gap(dfsf, targetsf)
    pbsf = pembobotan(gapsf, colssf)
    totalsf = get_cfsf(pbsf)
    total = result(totalcf, totalsf)
    new = pd.concat([dfkrn, total], axis=1)
    return new
