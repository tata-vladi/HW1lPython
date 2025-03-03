from address import Address
from mailing import Mailing

sender_address = Address(index="125310", city="Москва", street="Митинская", house=57, apartment=21)
receiver_address = Address(index="644076", city="Омск", street="Василия Товстухо", house=2, apartment=15)


mailing = Mailing(
    to_address=receiver_address,
    from_address=sender_address,
    cost=1000.0,
    track="ABC123"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")


