import mongoengine as me
import enum
import random as r


MIN_ID = 1
RADIUS = 0.1


class StatusTaxi(enum.IntEnum):
    AVAILABLE = 1
    NO_AVAILABLE = 2
    WITH_CLIENT = 3


class TaxiPrice(enum.Enum):
    ECONOM = 2
    NORMAL = 3
    LUX = 5


# conn = me.connect('test', username='test', password='onlytest')
# print(conn)

class Client(me.Document):
    """
    geo_from - the source address of the order
    geo_to - the target address of the order
    """
    first_name = me.StringField(max_length=50)
    last_name = me.StringField(max_length=50)
    geo_from = me.PointField()
    geo_to = me.PointField()
    rating = me.FloatField(default=0)
    meta = {
        'auto_create_index': True,
        'indexes': [
            'first_name',
            'last_name',
            ('first_name', 'last_name')
        ]
    }

    def __str__(self):
        return f"Client: {self.first_name} {self.last_name}"

    def find_any_taxi(self):
        taxis = TaxiCar.objects.filter(status=StatusTaxi.AVAILABLE,
            geo__geo_within_center=[self.geo_from['coordinates'], RADIUS])
        # find the nearest taxi car
        nearest = r.choice(taxis)
        return nearest

    def find_taxi(self, price: TaxiPrice):
        taxis = TaxiCar.objects.filter(status=StatusTaxi.AVAILABLE,
            geo__geo_within_center=[self.geo_from['coordinates'], RADIUS],
            price_level = price)
        # find the nearest taxi car
        nearest = r.choice(taxis)
        return nearest        


class TaxiCar(me.Document):
    reg_number = me.StringField(max_length=10, required=True)
    model = me.StringField(max_length=20, required=True)
    status = me.EnumField(StatusTaxi, required=True)
    price_level = me.EnumField(TaxiPrice, required=True)
    rating = me.FloatField(default=0)
    geo = me.PointField()
    client = me.ObjectIdField()
    meta = {
        'auto_create_index': True,
        'indexes': [
            'status',
            ('status', 'geo'),
            ('status', 'geo', 'price_level')
        ]
    }

    def __str__(self):
        if self.status == StatusTaxi.WITH_CLIENT:
            cl = Client.objects.filter(pk=self.client)
            cl = str(cl[0])
        else:
            cl = ""
        return f"Taxi: reg: {self.reg_number} model: {self.model} \
            status: {self.status} price: {self.price_level}" + cl


def fill_db(clients: int, cars: int):
    names = ["Ivan", "Petr", "Oleg", "Danila"]
    surnames = ["Ivanov", "Petrov", "Sidorov", "Kuznecov"]
    reg_numbers = ['A111AA152', 'B222BB152', 'C333CC152', 'E444EE152']
    models = ['Logan', 'Accent', 'Camry', 'Kalina']
    for i in range(clients):
        Client(first_name=r.choice(names), last_name=r.choice(surnames),
            geo_from={'type': 'Point', 'coordinates': [r.uniform(56.25, 56.35), r.uniform(44.08, 43.90)]},
            geo_to={'type': 'Point', 'coordinates': [r.uniform(56.25, 56.35), r.uniform(44.08, 43.90)]}).save()
    for i in range(cars // 2):
        TaxiCar(reg_number=r.choice(reg_numbers),
            model=r.choice(models),
            status=r.choice([i for i in StatusTaxi]),
            price_level=r.choice([i for i in TaxiPrice]),
            geo={'type': 'Point', 'coordinates': [r.uniform(56.25, 56.35), r.uniform(44.08, 43.90)]}).save()
    for i in range(cars // 2 + cars % 2):
        TaxiCar(reg_number=r.choice(reg_numbers),
            model=r.choice(models),
            status=StatusTaxi.AVAILABLE,
            price_level=r.choice([i for i in TaxiPrice]),
            geo={'type': 'Point', 'coordinates': [r.uniform(56.25, 56.35), r.uniform(44.08, 43.90)]}).save()
    for i in TaxiCar.objects.filter(status=StatusTaxi.WITH_CLIENT):
        i.client = r.choice(Client.objects()).pk
        i.save()



conn = me.connect('test', username='test', password='onlytest')
print(conn)

fill_db(6,20)
print(f'Clients in database: {Client.objects.count()}')
print(f'Taxis in database: {TaxiCar.objects.count()}')
cl = r.choice(Client.objects())
print(cl)
print(cl.find_any_taxi())
print(cl.find_taxi(TaxiPrice.ECONOM))
print(cl.find_taxi(TaxiPrice.NORMAL))
print(cl.find_taxi(TaxiPrice.LUX))
print("==============================")
print("Clients:")
for cl in Client.objects():
    print(cl)
print("==============================")
print("Taxis:")
for taxi in TaxiCar.objects():
    print(taxi)

