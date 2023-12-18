from sqlmodel import Session, select, and_
from models import engine, Airport, Airplane, Flight, Passenger, LoyaltyProgram, Reservation, Employee, AirTicket, Payment

#Клиенты, оплатившие бронь
def select_payment_completed():
    query: select = (select(Passenger.full_name)
        .join(AirTicket, AirTicket.id_passenger == Passenger.id_passenger)
        .join(Reservation, Reservation.id_reservation == AirTicket.id_reservation)
        .join(Payment, and_(Payment.id_reservation == Reservation.id_reservation, Payment.payment_state == "оплачено")))
    with Session(engine) as session:
        paid_passengers = session.exec(query)
        for passenger in paid_passengers:
            print(passenger)

#Клиенты, которые летят определенным рейсом
def select_flight_passengers():
    target_flight_id = "SDM6355"
    query = (select(Passenger.full_name)
        .join(AirTicket, AirTicket.id_passenger == Passenger.id_passenger)
        .join(Reservation, Reservation.id_reservation == AirTicket.id_reservation)
        .where(Reservation.id_flight == target_flight_id))
    with Session(engine) as session:
        flight_passengers = session.exec(query)
        for passenger in flight_passengers:
            print(passenger)

#Самолеты рейсов
def select_flight_details():
    query = (select(Airplane.model, Flight.departure_date, Airport.airport_name)
            .join(Airplane, Airplane.id_airplane == Flight.id_airplane)
            .join(Airport, Airport.id_airport == Flight.arrival_airport))
    with Session(engine) as session:
        flight_details = session.exec(query)
        for flight_detail in flight_details:
            print(f"Самолет {flight_detail.model} вылетает {flight_detail.departure_date} в {flight_detail.airport_name}")

#Клиенты с программой лояльности
def select_passengers_loyalty_program():
    query = (select(Passenger.full_name, LoyaltyProgram.loyalty_program)
            .join(LoyaltyProgram, Passenger.id_passenger == LoyaltyProgram.id_passenger))
    with Session(engine) as session:
        passengers = session.exec(query)
        for passenger in passengers:
            print(f"Клиент {passenger.full_name} с программой лояльности от {passenger.loyalty_program}")

#Персонал на выбранном борту
def select_employees_on_board():
    target_airplane = "AP003"
    query = (select(Employee.full_name, Employee.job)
             .join(Airplane, Airplane.id_airplane == Employee.id_airplane)
             .where(Employee.id_airplane == target_airplane))
    with Session(engine) as session:
        employees_on_board = session.exec(query)
        for employee_on_board in employees_on_board:
            print(f"Сотрудник {target_airplane}: {employee_on_board.full_name};\n                 Должность: {employee_on_board.job}")

def run_all_queries():
    select_payment_completed()
    print("\n")
    select_flight_passengers()
    print("\n")
    select_flight_details()
    print("\n")
    select_passengers_loyalty_program()
    print("\n")
    select_employees_on_board()

run_all_queries()