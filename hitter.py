def cold(x):
    if x <= 20:
        return 1
    elif x > 20 and x < 40:
        return (40 - x) / 20
    else:
        return 0

def warm(x):
    if x >= 40 and x <= 60:
        return (x - 40) / 20
    elif x > 60 and x < 80:
        return (80 - x) / 20
    else:
        return 0

def hot(x):
    if x >= 80:
        return 1
    elif x > 60 and x < 80:
        return (x - 60) / 20
    else:
        return 0

# Defuzzification
def defuzzify(cold_degree, warm_degree, hot_degree):
    return (cold_degree * 20 + warm_degree * 50 + hot_degree * 90) / (cold_degree + warm_degree + hot_degree)

# Fuzzy logic controller
def fuzzy_controller(temperature):
    cold_degree = cold(temperature)
    warm_degree = warm(temperature)
    hot_degree = hot(temperature)

    return defuzzify(cold_degree, warm_degree, hot_degree)

# Main function
def main():
    print("Selamat datang di pengatur pemanas air panas fuzzy!")
    print("Masukkan suhu air (dalam derajat Celcius):")
    temperature = float(input())
    
    # Menampilkan pilihan tingkat suhu air
    print("Pilih tingkat suhu air:")
    print("1. Dingin")
    print("2. Hangat")
    print("3. Panas")

    choice = int(input("Pilihan: "))

    if choice == 1:
        print("Anda memilih tingkat suhu Dingin.")
        print("Hasil pengaturan suhu: ", fuzzy_controller(temperature), "derajat Celcius")
    elif choice == 2:
        print("Anda memilih tingkat suhu Hangat.")
        print("Hasil pengaturan suhu: ", fuzzy_controller(temperature), "derajat Celcius")
    elif choice == 3:
        print("Anda memilih tingkat suhu Panas.")
        print("Hasil pengaturan suhu: ", fuzzy_controller(temperature), "derajat Celcius")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
