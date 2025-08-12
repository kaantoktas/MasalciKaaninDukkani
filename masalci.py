hikaye_sablonu = "Bugün {sıfat} bir gündü. {isim} adında bir arkadaşım, {fiil} için {yer} 'e gitti. Oraya {zarf} ulaştı ve {nesne} ile karşılaştı. Çok {duygu} hissetti ve {eylem} ya karar verdi."


print("Masalcı Kaan'ın şatosuna hoş geldin! Lütfen sihirli sözcükleri gir.")
sıfat = input("Bir sıfat gir: ")
isim = input("Bir isim gir: ")
fiil = input("Bir fiil gir: ")
yer = input("Bir yer ismi gir: ")
zarf = input("Bir zarf gir: ")
nesne = input("Bir nesne ismi gir: ")
duygu = input("Bir duygu gir: ")
eylem = input("Bir eylem gir: ")

dolu_hikaye = hikaye_sablonu.format(
    sıfat=sıfat,
    isim=isim,
    fiil=fiil,
    yer=yer,
    zarf=zarf,
    nesne=nesne,
    duygu=duygu,
    eylem=eylem
)

print("\nİşte senin çılgın hikayen:")
print(dolu_hikaye)