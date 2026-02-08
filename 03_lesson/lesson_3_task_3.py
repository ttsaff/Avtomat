from address import Address
from mailing import Mailing

to_address = Address("12345", "New York", "5th Avenue", "10", "1A")
from_address = Address("54321", "Los Angeles", "Sunset Boulevard", "20", "2B")
mailing = Mailing(to_address, from_address, 15, "TRACK123")

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.zip}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house_number} - "
    f"{mailing.from_address.apartment_number} "
    f"в {mailing.to_address.zip}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house_number} - "
    f"{mailing.to_address.apartment_number}. "
    f"Стоимость {mailing.cost} рублей."
)