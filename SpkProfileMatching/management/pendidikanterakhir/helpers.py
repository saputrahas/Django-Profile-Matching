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

#mendapatkan nilai core factor dan secondary factor
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

def ListPendidikanTerakhir(krywn):
    if len(krywn)>0:
        target = [1,1,2,3,4,5]
        cols = ['SD','SMP','SMA','DIII','Strata_satu','Strata_dua']

        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)

        pt = {
            cols[0] : [int(a.pendidikanterakhirs.SD) for a in krywn],
            cols[1] : [int(a.pendidikanterakhirs.SMP) for a in krywn],
            cols[2] : [int(a.pendidikanterakhirs.SMA) for a in krywn],
            cols[3] : [int(a.pendidikanterakhirs.DIII) for a in krywn],
            cols[4] : [int(a.pendidikanterakhirs.Strata_satu) for a in krywn],
            cols[5] : [int(a.pendidikanterakhirs.Strata_dua) for a in krywn],

        }
        dfpt = pd.DataFrame(data=pt)

        gap = get_gap(dfpt, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []

def CfPenTer(krywn):
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    
    target = [3, 4, 5]
    cols =['DIII','Strata_satu','Strata_dua']
    cf = {
        cols[0] : [int(a.pendidikanterakhirs.DIII) for a in krywn],
        cols[1] : [int(a.pendidikanterakhirs.Strata_satu) for a in krywn],
        cols[2] : [int(a.pendidikanterakhirs.Strata_dua) for a in krywn],

    }
    dfcf = pd.DataFrame(data=cf)

    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    new = pd.concat([dfcfkrn, pb], axis=1)
    return new

def SfPenTer(krywn):
    sfkrn = {'nama': [a.nama for a in krywn]}
    dfsfkrn = pd.DataFrame(data=sfkrn)
    
    target = [1, 1, 2]
    cols =['SD','SMP','SMA']
    sf = {
        cols[0] : [int(a.pendidikanterakhirs.SD) for a in krywn],
        cols[1] : [int(a.pendidikanterakhirs.SMP) for a in krywn],
        cols[2] : [int(a.pendidikanterakhirs.SMA) for a in krywn],

    }
    dfsf = pd.DataFrame(data=sf)

    gap = get_gap(dfsf, target)
    pb = pembobotan(gap, cols)
    new = pd.concat([dfsfkrn, pb], axis=1)
    return new

def NiCfPenTer(krywn):
    
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    target = [3, 4, 5]
    cols =['DIII','Strata_satu','Strata_dua']
    cf = {
        cols[0] : [int(a.pendidikanterakhirs.DIII) for a in krywn],
        cols[1] : [int(a.pendidikanterakhirs.Strata_satu) for a in krywn],
        cols[2] : [int(a.pendidikanterakhirs.Strata_dua) for a in krywn],
    }
 
    dfcf = pd.DataFrame(data=cf)
    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfcfkrn, total], axis=1)
    return new

def NiSfPenTer(krywn):
       
    sfkrn = {'nama': [a.nama for a in krywn]}
    dfsfkrn = pd.DataFrame(data=sfkrn)    
    target = [1, 1, 2]
    cols =['SD','SMP','SMA']
    sf = {
        cols[0] : [int(a.pendidikanterakhirs.SD) for a in krywn],
        cols[1] : [int(a.pendidikanterakhirs.SMP) for a in krywn],
        cols[2] : [int(a.pendidikanterakhirs.SMA) for a in krywn],
    }
    dfsf = pd.DataFrame(data=sf)
    gap = get_gap(dfsf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfsfkrn, total], axis=1)
    return new


def TotalPenTer(krywn):
    krn = {'nama': [a.nama for a in krywn]}
    dfkrn = pd.DataFrame(data=krn)

    targetcf = [3, 4, 5]
    colscf =['DIII','Strata_satu','Strata_dua']
    cf = {
        colscf[0] : [int(a.pendidikanterakhirs.DIII) for a in krywn],
        colscf[1] : [int(a.pendidikanterakhirs.Strata_satu) for a in krywn],
        colscf[2] : [int(a.pendidikanterakhirs.Strata_dua) for a in krywn],
    }
    dfcf = pd.DataFrame(data=cf)
    gapcf = get_gap(dfcf, targetcf)
    pbcf = pembobotan(gapcf, colscf)
    totalcf = get_cfsf(pbcf)


    targetsf = [1, 1, 2]
    colssf =['SD','SMP','SMA']
    sf = {
        colssf[0] : [int(a.pendidikanterakhirs.SD) for a in krywn],
        colssf[1] : [int(a.pendidikanterakhirs.SMP) for a in krywn],
        colssf[2] : [int(a.pendidikanterakhirs.SMA) for a in krywn],
    }
    dfsf = pd.DataFrame(data=sf)
    gapsf = get_gap(dfsf, targetsf)
    pbsf = pembobotan(gapsf, colssf)
    totalsf = get_cfsf(pbsf)
    total = result(totalcf, totalsf)
    new = pd.concat([dfkrn, total], axis=1)
    return new