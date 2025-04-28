from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 16 Pro", "+79031234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22 Ultra", "+79112345678"))
catalog.append(Smartphone("Xiaomi", "Mi 11 Ultra", "+79223456789"))
catalog.append(Smartphone("Huawei", "Pro", "+79334567890"))
catalog.append(Smartphone("Redmi", "9", "+79445678901"))

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")