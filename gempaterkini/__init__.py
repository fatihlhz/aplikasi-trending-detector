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
    hasil = dict()
    hasil['tanggal'] = '15 Februari 2022, 16:51:43 WIB'
    hasil['waktu'] = '16:51:43 WIB'
    hasil['magnitudo'] = '3.4'
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 0.72, 'bt': 131.51}
    hasil['pusat gempa'] = 'Pusat gempa berada di laut 29 km Timur Laut Kota Sorong'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Kota Sorong'

    return hasil


def tampilkan_data(result):
    print('Data gempa BMKG hari ini')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat Gempa : {result['pusat gempa']}")
    print(f"Dirasakan : {result['dirasakan']}")

