print("Toplamsal devamlılık & çarpımsal devamlılık hesaplayıcı\nÇıkmak için bir rakam girin\n")

while(True):

    sumCounter = 0 # Sayaç (Toplamsal devamlılık)
    sumDigit = 0 # Rakamlar toplamı
    sumDigitList = [] # Toplam olarak gösterilecek rakamlar kümesi

    mulCounter = 0 # Sayaç (Çarpımsal devamlılık)
    mulDigit = 1 # Rakamlar çarpımı
    mulDigitList = [] # Çarpım olarak gösterilecek rakamlar kümesi

    number = sumNumber = mulNumber = int(input("Sayı giriniz: "))

    if not number >= 10:

        print("{} geçersiz, çıkış yapılıyor...".format(number))
        break

    else:

        while (sumNumber >= 10): # Toplamsal devamlılık başlangıcı
            
            sumCounter += 1 # Toplamsal devamlılık sayacı
            sumDigit = 0 # Rakamlar toplamını sıfırla

            # Rakamlar toplamı
            for i in str(sumNumber): # Python int içerisinde for ile gezemediği için string'e dönüştürdüm.
                sumDigit += int(i) # Toplama işlemini yapabilmek için str rakamı int'e dönüştürdüm.
                sumDigitList += i

            firstNumber = sumDigitList[0] # Sayının en üst basamağındaki rakam
            lastNumber = sumDigitList[len(sumDigitList) - 1] # Sayının birler basamağındaki rakam

            print("Rakamlar toplamı", firstNumber, "+", end = ' ') # İlk rakamı ve toplama işaretini yazdır, satır atlama

            for i in range(1, len(sumDigitList) - 1): #i 1. indisten son indise kadar (range fonk. son yazılan sayıdan bir önceki sayı sonuncu sayıdır (len(sumDigitList) - 2)
                print("{}".format(sumDigitList[i]), end = ' ') # Mevcut indisteki rakamı yazdır, satır atlama
                print("+", end = ' ') # Toplama işareti yazdır, satır atlama

            print("{}".format(lastNumber), end = ' ') # Son rakamı yazdır, satır atlama
            print("= {}".format(sumDigit), end = '\n') # Eşit işareti ve rakamlar toplamını yazdır, satır atla
            
            if sumDigit >= 10: 
                print("Yeni sayı = {}".format(sumDigit)) # Yeni sayıyı yazdır

            sumNumber = sumDigit # Yeni sayıyı önceki sayının rakamlar toplamı olarak ata
            sumDigitList.clear() # Hesaplanan sayının rakamlarını tutan listeyi temizle

            if sumNumber < 10:
                print("\nToplamsal devamlılık = {} Toplamsal devamlılık kökü = {}\n".format(sumCounter, sumNumber)) # Toplamsal devamlılık sonu
                break
        
        while (mulNumber >= 10): # Çarpımsal devamlılık başlangıcı

            mulCounter += 1 # Çarpımsal devamlılık sayacı
            mulDigit = 1 # Rakamlar çarpımını sıfırla (etkisiz eleman)

            # Rakamlar çarpımı
            for i in str(mulNumber): # Python int içerisinde for ile gezemediği için string'e dönüştürdüm.
                mulDigit = (int(i) * mulDigit) # Çarpım işlemini yapabilmek için str rakamını int'e dönüştürdüm.
                mulDigitList += i

            firstNumber = mulDigitList[0] # Sayının en üst basamağındaki rakam
            lastNumber = mulDigitList[len(mulDigitList) - 1] # Sayının birler basamağındaki rakam

            print("Rakamlar çarpımı", firstNumber, "x", end = ' ') # İlk rakamı ve ilk çarpım işaretini yazdır yazdır, satır atlama

            for i in range(1, len(mulDigitList) - 1): #i 1. indisten son indise kadar (range fonk. son yazılan sayıdan bir önceki sayı sonuncu sayıdır (len(sumDigitList) - 2)
                print("{}".format(mulDigitList[i]), end = ' ') # Mevcut indisteki rakamı yazdır, satır atlama
                print("x", end = ' ') # Çarpım işareti yazdır, satır atlama

            print("{}".format(lastNumber), end = ' ') # Son rakamı yazdır, satır atlama
            print("= {}".format(mulDigit), end = '\n') # Eşit işareti ve rakamlar çarpımını yazdır, satır atla
            
            if mulDigit >= 10:
                print("Yeni sayı = {}".format(mulDigit)) # Yeni sayıyı yazdır

            mulNumber = mulDigit # Yeni sayıyı önceki sayının rakamlar çarpımı olarak ata
            mulDigitList.clear() # Hesaplanan sayının rakamlarını tutan listeyi temizle

            if mulNumber < 10:
                print("\nÇarpımsal devamlılık = {} Çarpımsal devamlılık kökü = {}\n".format(mulCounter, mulNumber)) # Çarpımsal devamlılık sonu
                break
