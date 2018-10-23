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


def ListPrilaku(krywn):
    if len(krywn)>0:
        target = [3,3,4,5]
        cols = ['dominance','influences','steadines','compliance']

        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)

        pr = {
            cols[0] : [int(a.prilakus.dominance) for a in krywn],
            cols[1] : [int(a.prilakus.influences) for a in krywn],
            cols[2] : [int(a.prilakus.steadines) for a in krywn],
            cols[3] : [int(a.prilakus.compliance) for a in krywn],


        }
        dfpr = pd.DataFrame(data=pr)

        gap = get_gap(dfpr, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []

def CfPrilaku(krywn):
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    
    target = [4, 5]
    cols =['steadines','compliance']
    cf = {
        cols[0] : [int(a.prilakus.steadines) for a in krywn],
        cols[1] : [int(a.prilakus.compliance) for a in krywn],

    }
    dfcf = pd.DataFrame(data=cf)

    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    new = pd.concat([dfcfkrn, pb], axis=1)
    return new

def SfPrilaku(krywn):
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    
    target = [3, 3]
    cols =['dominance','influences']
    cf = {
        cols[0] : [int(a.prilakus.dominance) for a in krywn],
        cols[1] : [int(a.prilakus.influences) for a in krywn],

    }
    dfcf = pd.DataFrame(data=cf)

    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    new = pd.concat([dfcfkrn, pb], axis=1)
    return new

def NiCfPri(krywn):
    
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    target = [4, 5]
    cols =['steadines','compliance']
    cf = {
        cols[0] : [int(a.prilakus.steadines) for a in krywn],
        cols[1] : [int(a.prilakus.compliance) for a in krywn],

    }
 
    dfcf = pd.DataFrame(data=cf)
    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfcfkrn, total], axis=1)
    return new

def NiSfPri(krywn):
       
    sfkrn = {'nama': [a.nama for a in krywn]}
    dfsfkrn = pd.DataFrame(data=sfkrn)    
    target = [3, 3]
    cols =['dominance','influences']
    sf = {
        cols[0] : [int(a.prilakus.dominance) for a in krywn],
        cols[1] : [int(a.prilakus.influences) for a in krywn],

    }
    dfsf = pd.DataFrame(data=sf)
    gap = get_gap(dfsf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfsfkrn, total], axis=1)
    return new


def TotalPri(krywn):
    krn = {'nama': [a.nama for a in krywn]}
    dfkrn = pd.DataFrame(data=krn)

    targetcf = [4, 5]
    colscf =['steadines','compliance']
    cf = {
        colscf[0] : [int(a.prilakus.steadines) for a in krywn],
        colscf[1] : [int(a.prilakus.compliance) for a in krywn],

    }
    dfcf = pd.DataFrame(data=cf)
    gapcf = get_gap(dfcf, targetcf)
    pbcf = pembobotan(gapcf, colscf)
    totalcf = get_cfsf(pbcf)


    targetsf = [3, 3]
    colssf =['dominance','influences']
    sf = {
        colssf[0] : [int(a.prilakus.dominance) for a in krywn],
        colssf[1] : [int(a.prilakus.influences) for a in krywn],

    }
    dfsf = pd.DataFrame(data=sf)
    gapsf = get_gap(dfsf, targetsf)
    pbsf = pembobotan(gapsf, colssf)
    totalsf = get_cfsf(pbsf)
    total = result(totalcf, totalsf)
    new = pd.concat([dfkrn, total], axis=1)
    return new

