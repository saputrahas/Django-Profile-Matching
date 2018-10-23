import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 

from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 

#reportPDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='apllication/pdf')
    return None


#perhitungan

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

def get_ranking(df1,df2,df3,df4,df5):
    df1 = df1*0.2
    df2 = df2*0.25
    df3 = df3*0.15
    df4 = df4*0.25
    df5 = df5*0.15
    total = df1+df2+df3+df4+df5
    return total


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
    return total

def TotalMas(krywn):
    krn = {'nama': [a.nama for a in krywn]}
    dfkrn = pd.DataFrame(data=krn)

    targetcf = [4, 4, 5,5]
    colscf =['duasatu_sd_duaempat','dualima_sd_duadelapan','duasembilan_sd_tigadua','tigatiga_sd_tigaenam']
    cf = {
        colscf[0] : [int(a.masakerjas.duasatu_sd_duaempat) for a in krywn],
        colscf[1] : [int(a.masakerjas.dualima_sd_duadelapan) for a in krywn],
        colscf[2] : [int(a.masakerjas.duasembilan_sd_tigadua) for a in krywn],
        colscf[3] : [int(a.masakerjas.tigatiga_sd_tigaenam) for a in krywn],
    }
    dfcf = pd.DataFrame(data=cf)
    gapcf = get_gap(dfcf, targetcf)
    pbcf = pembobotan(gapcf, colscf)
    totalcf = get_cfsf(pbcf)


    targetsf = [2, 2, 3, 3, 4]
    colssf =['nol_sd_empat','lima_sd_delapan','sembilan_sd_tigaenam','tigabelas_sd_enambelas','tujuhbelas_sd_duapuluh']
    sf = {
        colssf[0] : [int(a.masakerjas.nol_sd_empat) for a in krywn],
        colssf[1] : [int(a.masakerjas.lima_sd_delapan) for a in krywn],
        colssf[2] : [int(a.masakerjas.sembilan_sd_tigaenam) for a in krywn],
        colssf[3] : [int(a.masakerjas.tigabelas_sd_enambelas) for a in krywn],
        colssf[4] : [int(a.masakerjas.tujuhbelas_sd_duapuluh) for a in krywn],    
    }
    dfsf = pd.DataFrame(data=sf)
    gapsf = get_gap(dfsf, targetsf)
    pbsf = pembobotan(gapsf, colssf)
    totalsf = get_cfsf(pbsf)
    total = result(totalcf, totalsf)
    return total

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
    return total

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
    return total

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
    return total

def total_rangking(krywn):
    krn = {'nama': [a.nama for a in krywn]}
    dfkrn = pd.DataFrame(data=krn)

    hasilkec = TotalKec(krywn)
    hasilmas = TotalMas(krywn)
    hasilpen = TotalPenTer(krywn)
    hasilpri = TotalPri(krywn)
    hasilsik = TotalSik(krywn)

    totalrang = get_ranking(hasilkec, hasilmas, hasilpen, hasilpri, hasilsik)
    new = pd.concat([dfkrn, totalrang], axis=1)
    return new
    

    
    
    