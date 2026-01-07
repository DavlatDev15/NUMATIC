print("1 dan 100 gacha bir son o'ylang.")
print("Savollarga javob bering:")
print("katta  -> agar siz o'ylagan son katta bo'lsa")
print("kichik -> agar kichik bo'lsa")
print("togri  -> agar to'g'ri topsam")

past = 1
yuqori = 100

while True:
    taxmin = (past + yuqori) // 2
    javob = input(f"Siz o'ylagan son {taxmin} mi? ").lower()

    if javob == "togri":
        print("🎉 Topdim!")
        break
    elif javob == "katta":
        past = taxmin + 1
    elif javob == "kichik":
        yuqori = taxmin - 1
    else:
        print("❗ Faqat: katta, kichik yoki togri deb yozing")
