from library import download_gambar, get_url_list, kirim_gambar
import time
import datetime

def kirim_semua():
    urls = get_url_list()
    temp = 0

    catat = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu_proses = download_gambar(urls[k])
        print(f"completed {waktu_proses} detik")
        UDP_IP_ADDRESS = "192.168.122.214"
        UDP_IP_ADDRESS2 = "192.168.122.111"
        if temp == 0:
            kirim_gambar(UDP_IP_ADDRESS, 5050, f"{k}.jpg")
            temp = temp + 1
        elif temp == 1:
            kirim_gambar(UDP_IP_ADDRESS2, 5050, f"{k}.jpg")
    selesai = datetime.datetime.now() - catat
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik")


#fungsi download_gambar akan dijalankan secara berurutan

if __name__=='__main__':
    kirim_semua()