from smartphone import Smartphone

catalog = [Smartphone("Apple", "iPhone 12", "+1234567890"),
        Smartphone("MOTOROLA", "E398", "+4545454545"),
        Smartphone("Apple", "iPhone 14", "+1254545890"),
        Smartphone("Nokia", "3310", "+1234567890"),
        Smartphone("Apple", "iPhone 17", "+6789098765")]

for phone in catalog:  
    print(f"{phone.mark} - {phone.model}. {phone.number}")