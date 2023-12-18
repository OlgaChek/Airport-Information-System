from sqlmodel import SQLModel, Field, Session, create_engine
from datetime import datetime

class Airport(SQLModel, table=True):
    id_airport: str = Field(primary_key=True)
    airport_name: str
    legal_address: str
    code_IATA_ICAO: str

class Airplane(SQLModel, table=True):
    id_airplane: str = Field(primary_key=True)
    airplane_type: str
    model: str
    capacity: int
    technical_condition: str

class Flight(SQLModel, table=True):
    id_flight: str = Field(primary_key=True)
    departure_date: datetime
    arrival_date: datetime
    departure_airport: str = Field(foreign_key="airport.id_airport")
    arrival_airport: str = Field(foreign_key="airport.id_airport")
    id_airplane: str = Field(foreign_key="airplane.id_airplane")
    num_of_avail_seats: int

class Passenger(SQLModel, table=True):
    id_passenger: str = Field(primary_key=True)
    full_name: str
    series_number_passport: str
    contacts: str

class LoyaltyProgram(SQLModel, table=True):
    id_client: str = Field(primary_key=True)
    id_passenger: str = Field(foreign_key="passenger.id_passenger")
    loyalty_program: str
    discounts_bonuses: float

class Reservation(SQLModel, table=True):
    id_reservation: str = Field(primary_key=True, unique=True)
    id_flight: str = Field(foreign_key="flight.id_flight")
    booking_status: str

class Employee(SQLModel, table=True):
    id_employee: str = Field(primary_key=True)
    full_name: str
    job: str
    certification_license: str
    id_airplane: str = Field(foreign_key="airplane.id_airplane")

class AirTicket(SQLModel, table=True):
    id_airticket: str = Field(primary_key=True)
    id_reservation: str = Field(foreign_key="reservation.id_reservation")
    departure_date: datetime
    arrival_date: datetime
    service_class: str
    id_passenger: str = Field(foreign_key="passenger.id_passenger")
    ticket_price: float

class Payment(SQLModel, table=True):
    id_reservation: str = Field(primary_key=True, foreign_key="reservation.id_reservation")
    payment_state: str 

def create_airport():
    airport1 = Airport(id_airport="JFK", airport_name="Informational Guide to John F. Kennedy International Airport", legal_address="Билдинг 14, Нью-Йорк 11430, США", code_IATA_ICAO="JFK/KJFK")
    airport2 = Airport(id_airport="DME", airport_name="Домодедово", legal_address="Россия, Московская область, Домодедовский район", code_IATA_ICAO="DME/UUDD")
    airport3 = Airport(id_airport="ICN", airport_name="Международный аэропорт Инчхон", legal_address="272 Гонгханг-ро Джун-гу, код 400-700", code_IATA_ICAO="ICN/RKSI")
    airport4 = Airport(id_airport="FCO", airport_name="Фьюмичино", legal_address="Лацио, Рим, Фьюмичино, Via Luigi Bleriot", code_IATA_ICAO="FCO")
    airport5 = Airport(id_airport="AER", airport_name="Международный аэропорт Сочи", legal_address="Россиия, Адлер, Краснодарский край, ул. Мира, 50", code_IATA_ICAO="AER/URSS")
    airport6 = Airport(id_airport="VVO", airport_name="Международный аэропорт Владивосток", legal_address="Россия, Приморский край, г. Артем, ул. Владимира Сайбеля 41", code_IATA_ICAO="VVO/UHWW")
    airport7 = Airport(id_airport="SIN", airport_name="Singapore Changi Airport", legal_address="P.O. Box 1, Singapore 918 141", code_IATA_ICAO="SIN/WSSS")
    airport8 = Airport(id_airport="LED", airport_name="Международный аэропорт Пулково", legal_address="Россия, Санкт-Петербург, Пулковское шоссе, 41, лит.ЗА", code_IATA_ICAO="LED/ULLI")
    airport9 = Airport(id_airport="MRV", airport_name="Международный аэропорт Минеральные Воды имени М. Ю. Лермонтова", legal_address="Россия, Ставропольский край, г. Минеральные Воды, Территория Аэропорт", code_IATA_ICAO="MRV/URMM")
    airport10 = Airport(id_airport="YVR", airport_name="Vancouver International Airport", legal_address="Шоссе Грант МакКоначи, г. Ричмонд, провинция Британская Колумбия, Канада", code_IATA_ICAO="YVR/CYVR")
    airport11 = Airport(id_airport="DXB", airport_name="Аэропорт Дубай", legal_address="Department of Civil Aviation, P.O. Box 2525, Dubai, United Arab Emirates", code_IATA_ICAO="DXB/OMDB")
    with Session(engine) as session:
        session.add(airport1)
        session.add(airport2)
        session.add(airport3)
        session.add(airport4)
        session.add(airport5)
        session.add(airport6)
        session.add(airport7)
        session.add(airport8)
        session.add(airport9)
        session.add(airport10)
        session.add(airport11)
        session.commit()

def create_airplane():
    airplane1 = Airplane(id_airplane="AP001", airplane_type="пассажирский", model="Boeing 737-800", capacity=189, technical_condition="исправное")
    airplane2 = Airplane(id_airplane="AP002", airplane_type="пассажирский", model="Airbus A320neo", capacity=236, technical_condition="исправное")
    airplane3 = Airplane(id_airplane="AP003", airplane_type="пассажирский", model="Embraer RRJ-190", capacity=114, technical_condition="работоспособное")
    airplane4 = Airplane(id_airplane="AP004", airplane_type="пассажирский", model="Airbus A321neo", capacity=240, technical_condition="работоспособное")
    airplane5 = Airplane(id_airplane="AP005", airplane_type="пассажирский", model="Airbus A319", capacity=140, technical_condition="исправное")
    airplane6 = Airplane(id_airplane="AP006", airplane_type="пассажирский", model="Boeing 777-300", capacity=550, technical_condition="работоспособное")
    with Session(engine) as session:
        session.add(airplane1)
        session.add(airplane2)
        session.add(airplane3)
        session.add(airplane4)
        session.add(airplane5)
        session.add(airplane6)
        session.commit()

def create_flight():
    flight1 = Flight(id_flight="BRU955", departure_date=datetime.strptime("2023-12-16 00:05:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-16 10:00:00", "%Y-%m-%d %H:%M:%S"), departure_airport="DME", arrival_airport="JFK", id_airplane="AP003", num_of_avail_seats=114)
    flight2 = Flight(id_flight="SBI2154", departure_date=datetime.strptime("2023-12-20 01:30:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-20 09:55:00", "%Y-%m-%d %H:%M:%S"), departure_airport="DME", arrival_airport="ICN", id_airplane="AP002", num_of_avail_seats=236)
    flight3 = Flight(id_flight="UAE130", departure_date=datetime.strptime("2023-12-18 10:29:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-18 16:51:00", "%Y-%m-%d %H:%M:%S"), departure_airport="DME", arrival_airport="DXB", id_airplane="AP006", num_of_avail_seats=550)
    flight4 = Flight(id_flight="SDM6355", departure_date=datetime.strptime("2023-12-22 08:44:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-22 12:16:00", "%Y-%m-%d %H:%M:%S"), departure_airport="LED", arrival_airport="MRV", id_airplane="AP004", num_of_avail_seats=240)
    with Session(engine) as session:
        session.add(flight1)
        session.add(flight2)
        session.add(flight3)
        session.add(flight4)
        session.commit()

def create_passenger():
    passenger1 = Passenger(id_passenger="PAS0001", full_name="Харитонов Максим Маркович", series_number_passport="4965 207768", contacts="email1@example.com, +7(495)652-63-38")
    passenger2 = Passenger(id_passenger="PAS0002", full_name="Харитонова Юлия Николаевна", series_number_passport="4579 699581", contacts="email2@example.com, +7(495)769-85-12")
    passenger3 = Passenger(id_passenger="PAS0003", full_name="Харитонова Мария Максимовна", series_number_passport="4295 979396", contacts="")
    passenger4 = Passenger(id_passenger="PAS0004", full_name="Мощенский Максим Юрьевич", series_number_passport="4982 410174", contacts="+7(912)255-35-67, maksim9015@rambler.ru")
    passenger5 = Passenger(id_passenger="PAS0005", full_name="Ягункина Ксения Андреевна", series_number_passport="4584 579044", contacts="+7(911)763-45-12, mirskaya@mail.ru")
    passenger6 = Passenger(id_passenger="PAS0006", full_name="Ягункин Александр Дмитриевич", series_number_passport="4818 553753", contacts="+7(912)119-50-62")
    passenger7 = Passenger(id_passenger="PAS0007", full_name="Белоусов Сергей Николаевич", series_number_passport="4852 609717", contacts="+7(495)769-85-12, sergeybel@gmail.ru")
    passenger8 = Passenger(id_passenger="PAS0008", full_name="Белоусова Анна Олеговна", series_number_passport="4852 619917", contacts="+7(495)896-25-12, annabel@mail.ru")
    passenger9 = Passenger(id_passenger="PAS0009", full_name="Белоусов Андрей Сергеевич", series_number_passport="4711 251795", contacts="")
    passenger10 = Passenger(id_passenger="PAS0010", full_name="Белоусов Александр Сергеевич", series_number_passport="4711 296690", contacts="")
    passenger11 = Passenger(id_passenger="PAS0011", full_name="Широкова Елена Даниловна", series_number_passport="4933 664782", contacts="+7(981)878-38-95, lena52@gmail.com")
    with Session(engine) as session:
        session.add(passenger1)
        session.add(passenger2)
        session.add(passenger3)
        session.add(passenger4)
        session.add(passenger5)
        session.add(passenger6)
        session.add(passenger7)
        session.add(passenger8)
        session.add(passenger9)
        session.add(passenger10)
        session.add(passenger11)
        session.commit()

def create_loyaltyProgram():
    loyaltyProgram1 = LoyaltyProgram(id_client="LP0001", id_passenger="PAS0001", loyalty_program="S7 Priority", discounts_bonuses=2)
    loyaltyProgram2 = LoyaltyProgram(id_client="LP0002", id_passenger="PAS0002", loyalty_program="Аэрофлот Бонус", discounts_bonuses=50)
    loyaltyProgram3 = LoyaltyProgram(id_client="LP0003", id_passenger="PAS0011", loyalty_program="Аэрофлот Бонус", discounts_bonuses=80)
    loyaltyProgram4 = LoyaltyProgram(id_client="LP0004", id_passenger="PAS0011", loyalty_program="S7 Priority", discounts_bonuses=10)
    loyaltyProgram5 = LoyaltyProgram(id_client="LP0005", id_passenger="PAS0007", loyalty_program="Крылья", discounts_bonuses=15)
    loyaltyProgram6 = LoyaltyProgram(id_client="LP0006", id_passenger="PAS0004", loyalty_program="Аэрофлот Бонус", discounts_bonuses=60)
    with Session(engine) as session:
        session.add(loyaltyProgram1)
        session.add(loyaltyProgram2)
        session.add(loyaltyProgram3)
        session.add(loyaltyProgram4)
        session.add(loyaltyProgram5)
        session.add(loyaltyProgram6)
        session.commit()

def create_reservation():
    reservation1 = Reservation(id_reservation="ICN456", id_flight="SBI2154", booking_status="подтвержден")
    reservation2 = Reservation(id_reservation="ICN789", id_flight="SBI2154", booking_status="отменен")
    reservation3 = Reservation(id_reservation="DXB012", id_flight="UAE130", booking_status="подтвержден")
    reservation4 = Reservation(id_reservation="DXB082", id_flight="UAE130", booking_status="подтвержден")
    reservation5 = Reservation(id_reservation="MRV456", id_flight="SDM6355", booking_status="подтвержден")
    reservation6 = Reservation(id_reservation="MRV989", id_flight="SDM6355", booking_status="подтвержден")
    reservation7 = Reservation(id_reservation="MRV019", id_flight="SDM6355", booking_status="подтвержден")
    reservation8 = Reservation(id_reservation="MRV087", id_flight="SDM6355", booking_status="подтвержден")
    reservation9 = Reservation(id_reservation="JFK705", id_flight="BRU955", booking_status="подтвержден")
    reservation10 = Reservation(id_reservation="JFK219", id_flight="BRU955", booking_status="подтвержден")
    reservation11= Reservation(id_reservation="JFK373", id_flight="BRU955", booking_status="подтвержден")
    reservation11= Reservation(id_reservation="JFK691", id_flight="BRU955", booking_status="подтвержден")
    with Session(engine) as session:
        session.add(reservation1)
        session.add(reservation2)
        session.add(reservation3)
        session.add(reservation4)
        session.add(reservation5)
        session.add(reservation6)
        session.add(reservation7)
        session.add(reservation8)
        session.add(reservation9)
        session.add(reservation10)
        session.add(reservation11)
        session.commit()

def create_employee():
    employee1 = Employee(id_employee="EM0001", id_airplane="", full_name="Белоусов Сергей Альбертов", job="старший диспетчер", certification_license="да")
    employee2 = Employee(id_employee="EM0002", id_airplane="AP001", full_name="Серпионов Николай Филиппович", job="старший пилот", certification_license="да")
    employee3 = Employee(id_employee="EM0003", id_airplane="AP003", full_name="Николин Федор Александрович", job="старший пилот", certification_license="да")
    employee4 = Employee(id_employee="EM0004", id_airplane="AP003", full_name="Степнов Роман Кириллович", job="второй пилот", certification_license="да")
    employee5 = Employee(id_employee="EM0005", id_airplane="AP003", full_name="Лескова Анастасия Александровна", job="старший бортпроводник", certification_license="да")
    employee6 = Employee(id_employee="EM0006", id_airplane="", full_name="Валуев Никита Денисович", job="стажер", certification_license="нет")
    with Session(engine) as session:
        session.add(employee1)
        session.add(employee2)
        session.add(employee3)
        session.add(employee4)
        session.add(employee5)
        session.add(employee6)
        session.commit()

def create_airTicket():
    airTicket1 = AirTicket(id_airticket="MN789012", id_reservation="ICN456", departure_date=datetime.strptime("2023-12-20 01:30:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-20 09:55:00", "%Y-%m-%d %H:%M:%S"), service_class="M", id_passenger="PAS0011", ticket_price=29639)
    airTicket2 = AirTicket(id_airticket="KL123456", id_reservation="DXB012", departure_date=datetime.strptime("2023-12-18 10:29:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-18 16:51:00", "%Y-%m-%d %H:%M:%S"), service_class="D", id_passenger="PAS0006", ticket_price=340170)    
    airTicket3 = AirTicket(id_airticket="KL567890", id_reservation="DXB082", departure_date=datetime.strptime("2023-12-18 10:29:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-18 16:51:00", "%Y-%m-%d %H:%M:%S"), service_class="D", id_passenger="PAS0005", ticket_price=320100)
    airTicket4 = AirTicket(id_airticket="IJ567990", id_reservation="JFK691", departure_date=datetime.strptime("2023-12-16 00:05:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-16 10:00:00", "%Y-%m-%d %H:%M:%S"), service_class="S", id_passenger="PAS0004", ticket_price=76791) 
    airTicket5 = AirTicket(id_airticket="ST987896", id_reservation="MRV456", departure_date=datetime.strptime("2023-12-22 08:44:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-22 12:16:00", "%Y-%m-%d %H:%M:%S"), service_class="S", id_passenger="PAS0007", ticket_price=10799) 
    airTicket6 = AirTicket(id_airticket="ST909597", id_reservation="MRV989", departure_date=datetime.strptime("2023-12-22 08:44:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-22 12:16:00", "%Y-%m-%d %H:%M:%S"), service_class="S", id_passenger="PAS0008", ticket_price=10799) 
    airTicket7 = AirTicket(id_airticket="ST509743", id_reservation="MRV019", departure_date=datetime.strptime("2023-12-22 08:44:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-22 12:16:00", "%Y-%m-%d %H:%M:%S"), service_class="S", id_passenger="PAS0009", ticket_price=5709) 
    airTicket8 = AirTicket(id_airticket="ST037826", id_reservation="MRV087", departure_date=datetime.strptime("2023-12-22 08:44:00", "%Y-%m-%d %H:%M:%S"), arrival_date=datetime.strptime("2023-12-22 12:16:00", "%Y-%m-%d %H:%M:%S"), service_class="S", id_passenger="PAS0010", ticket_price=5100) 
    with Session(engine) as session:
        session.add(airTicket1)
        session.add(airTicket2)
        session.add(airTicket3)
        session.add(airTicket4)
        session.add(airTicket5)
        session.add(airTicket6)
        session.add(airTicket7)
        session.add(airTicket8)
        session.commit()

def create_payment():
    payment1 = Payment(id_reservation="ICN456", payment_state="оплачено")
    payment2 = Payment(id_reservation="DXB012", payment_state="оплачено")
    payment3 = Payment(id_reservation="DXB082", payment_state="оплачено")
    payment4 = Payment(id_reservation="JFK691", payment_state="не оплачено")
    payment5 = Payment(id_reservation="MRV456", payment_state="ожидается")
    with Session(engine) as session:
        session.add(payment1)
        session.add(payment2)
        session.add(payment3)
        session.add(payment4)
        session.add(payment5)
        session.commit()

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

create_airport()
create_airplane()
create_flight()
create_passenger()
create_loyaltyProgram()
create_reservation()
create_employee()
create_airTicket()
create_payment()