from address import Address
from mailing import Mailing

to_Address = Address("455000", "Магнитогорск", "Одесская", "17", "1")
from_Address = Address("455000", "Магнитогорск", "Ленина", "1", "1")

mailing = Mailing(
    to_address=to_Address,
    from_address=from_Address,
    cost=150,
    track="455000123456789"
    )

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} -"
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
