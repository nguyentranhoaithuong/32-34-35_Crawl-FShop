import shutil
import os

ThuMuc='D:\Khai_pha_web\BaoCao\B7_TXLCmt'

hp_path = os.path.join(ThuMuc, 'HP')
if not os.path.exists(hp_path):
    os.mkdir(hp_path)

dell_path = os.path.join(ThuMuc, 'DELL')
if not os.path.exists(dell_path):
    os.mkdir(dell_path)

mac_path = os.path.join(ThuMuc, 'MACBOOK')
if not os.path.exists(mac_path):
    os.mkdir(mac_path)

asus_path = os.path.join(ThuMuc, 'ASUS')
if not os.path.exists(asus_path):
    os.mkdir(asus_path)

msi_path = os.path.join(ThuMuc, 'MSI')
if not os.path.exists(msi_path):
    os.mkdir(msi_path)

lenovo_path = os.path.join(ThuMuc, 'LENOVO')
if not os.path.exists(lenovo_path):
    os.mkdir(lenovo_path)

acer_path = os.path.join(ThuMuc, 'ACER')
if not os.path.exists(acer_path):
    os.mkdir(acer_path)

lg_path = os.path.join(ThuMuc, 'LG')
if not os.path.exists(lg_path):
    os.mkdir(lg_path)

gigabyte_path = os.path.join(ThuMuc, 'GIGABYTE')
if not os.path.exists(gigabyte_path):
    os.mkdir(gigabyte_path)

masstel_path = os.path.join(ThuMuc, 'MASSTEL')
if not os.path.exists(masstel_path):
    os.mkdir(masstel_path)

huawei_path = os.path.join(ThuMuc, 'HUAWEI')
if not os.path.exists(huawei_path):
    os.mkdir(huawei_path)

surface_path = os.path.join(ThuMuc, 'SURFACE')
if not os.path.exists(surface_path):
    os.mkdir(surface_path)

vaio_path = os.path.join(ThuMuc, 'VAIO')
if not os.path.exists(vaio_path):
    os.mkdir(vaio_path)

files=os.listdir(ThuMuc)
for file in files:
    if "hp" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(hp_path)
        shutil.move(a,b)
    elif "dell" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(dell_path)
        shutil.move(a,b)
    elif "macbook" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(mac_path)
        shutil.move(a,b)
    elif "asus" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(asus_path)
        shutil.move(a,b)
    elif "msi" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(msi_path)
        shutil.move(a,b)
    elif "lenovo" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(lenovo_path)
        shutil.move(a,b)
    elif "acer" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(acer_path)
        shutil.move(a,b)
    elif "lg" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(lg_path)
        shutil.move(a,b)
    elif "gigabyte" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(gigabyte_path)
        shutil.move(a,b)
    elif "masstel" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(masstel_path)
        shutil.move(a,b)
    elif "huawei" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(huawei_path)
        shutil.move(a,b)
    elif "surface" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(surface_path)
        shutil.move(a,b)
    elif "vaio" in file:
        a=os.path.join(ThuMuc,file)
        b=os.path.join(vaio_path)
        shutil.move(a,b)