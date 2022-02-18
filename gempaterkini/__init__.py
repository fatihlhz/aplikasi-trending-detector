import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    tanggal = 15 Februari 2022,
    waktu = 16:51:43 WIB
    magnitudo = 3.4
    kedalaman = 10 km
    lokasi = 0.72 LS - 131.51 BT
    pusat gempa = Pusat gempa berada di laut 29 km Timur Laut Kota Sorong
    dirasakan = Dirasakan (Skala MMI): II Kota Sorong
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(',')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('Data tidak tersedia')
        return
    print('Data gempa BMKG hari ini')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Pusat Gempa : {result['lokasi']}")
    print(f"Dirasakan : {result['dirasakan']}")
