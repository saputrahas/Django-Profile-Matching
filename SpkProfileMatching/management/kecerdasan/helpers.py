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


def ListKecerdasanNilai(krywn):
    if len(krywn)>0:
        target = [4, 3, 4, 5, 3]
        cols = ['sistematika_berfikir', 'konsentrasi', 'logika_praktis','imajinasi_kreatif','antisipasi']

        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)

        kec = {
            cols[0] : [int(a.kecerdasans.sistematika_berfikir) for a in krywn],
            cols[1] : [int(a.kecerdasans.konsentrasi) for a in krywn],
            cols[2] : [int(a.kecerdasans.logika_praktis) for a in krywn],
            cols[3] : [int(a.kecerdasans.imajinasi_kreatif) for a in krywn],
            cols[4] : [int(a.kecerdasans.antisipasi) for a in krywn],
        }
        dfkec = pd.DataFrame(data=kec)

        gap = get_gap(dfkec, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []

def CfKecerdasan(krywn):
    
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    
    target = [4, 4, 5]
    cols =['sistematika_berfikir','logika_praktis','imajinasi_kreatif']
    cf = {
        cols[0] : [int(a.kecerdasans.sistematika_berfikir) for a in krywn],
        cols[1] : [int(a.kecerdasans.logika_praktis) for a in krywn],
        cols[2] : [int(a.kecerdasans.imajinasi_kreatif) for a in krywn],
    }
    dfcf = pd.DataFrame(data=cf)

    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    new = pd.concat([dfcfkrn, pb], axis=1)
    return new

def SfKecerdasan(krywn):
    sfkrn = {'nama': [a.nama for a in krywn]}
    dfsfkrn = pd.DataFrame(data=sfkrn)    
    target = [3,3]
    cols =['konsentrasi','antisipasi']
    sf = {
        cols[0] : [int(a.kecerdasans.konsentrasi) for a in krywn],
        cols[1] : [int(a.kecerdasans.antisipasi) for a in krywn],
    }
    dfsf = pd.DataFrame(data=sf)
    gap = get_gap(dfsf, target)
    pb = pembobotan(gap, cols)
    new = pd.concat([dfsfkrn, pb], axis=1)
    return new

def NiCfKecerdasan(krywn):
    
    cfkrn = {'nama': [a.nama for a in krywn]}
    dfcfkrn = pd.DataFrame(data=cfkrn)
    
    target = [4, 4, 5]
    cols =['sistematika_berfikir','logika_praktis','imajinasi_kreatif']
    cf = {
        cols[0] : [int(a.kecerdasans.sistematika_berfikir) for a in krywn],
        cols[1] : [int(a.kecerdasans.logika_praktis) for a in krywn],
        cols[2] : [int(a.kecerdasans.imajinasi_kreatif) for a in krywn],
    }
    dfcf = pd.DataFrame(data=cf)

    gap = get_gap(dfcf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfcfkrn, total], axis=1)
    return new

def NiSfKecerdasan(krywn):
       
    sfkrn = {'nama': [a.nama for a in krywn]}
    dfsfkrn = pd.DataFrame(data=sfkrn)    
    target = [3,3]
    cols =['konsentrasi','antisipasi']
    sf = {
        cols[0] : [int(a.kecerdasans.konsentrasi) for a in krywn],
        cols[1] : [int(a.kecerdasans.antisipasi) for a in krywn],
    }
    dfsf = pd.DataFrame(data=sf)
    gap = get_gap(dfsf, target)
    pb = pembobotan(gap, cols)
    total = get_cfsf(pb)
    new = pd.concat([dfsfkrn, total], axis=1)
    return new


def TotalKec(krywn):
    krn = {'nama': [a.nama for a in krywn]}
    dfkrn = pd.DataFrame(data=krn)

    targetcf = [4, 4, 5]
    colscf =['sistematika_berfikir','logika_praktis','imajinasi_kreatif']
    cf = {
        colscf[0] : [int(a.kecerdasans.sistematika_berfikir) for a in krywn],
        colscf[1] : [int(a.kecerdasans.logika_praktis) for a in krywn],
        colscf[2] : [int(a.kecerdasans.imajinasi_kreatif) for a in krywn],
    }
    dfcf = pd.DataFrame(data=cf)
    gapcf = get_gap(dfcf, targetcf)
    pbcf = pembobotan(gapcf, colscf)
    totalcf = get_cfsf(pbcf)
    
    targetsf = [3,3]
    colssf =['konsentrasi','antisipasi']
    sf = {
        colssf[0] : [int(a.kecerdasans.konsentrasi) for a in krywn],
        colssf[1] : [int(a.kecerdasans.antisipasi) for a in krywn],
    }
    dfsf = pd.DataFrame(data=sf)
    gapsf = get_gap(dfsf, targetsf)
    pbsf = pembobotan(gapsf, colssf)
    totalsf = get_cfsf(pbsf)
    total = result(totalcf, totalsf)
    new = pd.concat([dfkrn, total], axis=1)
    return new