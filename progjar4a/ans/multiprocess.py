from file_client_cli import remote_get
import time
import datetime
from multiprocessing import Process

def req100():
    texec = dict()
    catat_awal = datetime.datetime.now()
    filename = 'pokijan.jpg'
    for k in range(100):
        print(f"file - {k}")
        waktu = time.time()
        texec[k] = Process(target=remote_get, args=(filename,))
        texec[k].start()
    for k in range(100):
        texec[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")

if __name__ == '__main__':
    req100()