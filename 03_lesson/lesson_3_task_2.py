from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "A53", "+79001234567"),
    Smartphone("Apple", "Iphone 14", "+79007654321"),
    Smartphone("Nokia", "3310", "+79001236745"),
    Smartphone("Samsung", "S21 Ultra", "+79001235476"),
    Smartphone("Tecno", "Camon 40", "+79001237654"),
    ]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
