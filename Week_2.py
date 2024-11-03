öğrenci_1_dict = {"öğrenci no": 103031845, "isim": "Ahmet", "soyisim": "Yıldız", "bölüm": "makina müh", "sınıf": 1}
öğrenci_2_dict = {"öğrenci no": 103031846, "isim": "Meryem", "soyisim": "Kaya", "bölüm": "bigisayar müh", "sınıf": 3}
öğrenci_3_dict = {"öğrenci no": 103031847, "isim": "Mehmet", "soyisim": "Keskin", "bölüm": "yazılım müh", "sınıf": 2}
öğrenci_4_dict = {"öğrenci no": 103031848, "isim": "Mustafa", "soyisim": "Duran", "bölüm": "mekatronik müh", "sınıf": 4}
öğrenci_5_dict = {"öğrenci no": 103031843, "isim": "Sevilay", "soyisim": "Çakır", "bölüm": "endüstri müh", "sınıf": 4}

tüm_öğrenciler = [öğrenci_1_dict, öğrenci_2_dict, öğrenci_3_dict, öğrenci_4_dict, öğrenci_5_dict]

çift_olan = []
tek_olan = []

for öğr in tüm_öğrenciler:
    if (öğr ["öğrenci no"]) %2 == 0:
        çift_olan.append(öğr)
    else:
        tek_olan.append(öğr)


print("çift olan öğr:")
for öğr in çift_olan:
    print(öğr)       


print("tek olan öğr:")
for öğr in tek_olan:
    print(öğr)   


çift_olan_4_sınıf = False
for öğr in çift_olan:
    if öğr ["sınıf"] == 4:
        çift_olan_4_sınıf = True



tek_olan_4_sınıf = False
for öğr in tek_olan:
    if öğr ["sınıf"] == 4:
        tek_olan_4_sınıf = True


print("Numarası çift olan öğrenciler arasında 4. sınıf olanlar", çift_olan_4_sınıf)
print("Numarası tek olan öğrenciler arasında 4. sınıf olanlar", tek_olan_4_sınıf)