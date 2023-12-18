CREATE DATABASE AIRPORT

CREATE TABLE airplane (
	id_airplane VARCHAR NOT NULL, 
	airplane_type VARCHAR NOT NULL, 
	model VARCHAR NOT NULL, 
	capacity INTEGER NOT NULL, 
	technical_condition VARCHAR NOT NULL, 
	PRIMARY KEY (id_airplane)
);

CREATE TABLE airport (
	id_airport VARCHAR NOT NULL, 
	airport_name VARCHAR NOT NULL, 
	legal_address VARCHAR NOT NULL, 
	"code_IATA_ICAO" VARCHAR NOT NULL, 
	PRIMARY KEY (id_airport)
);

CREATE TABLE flight (
	id_flight VARCHAR NOT NULL, 
	departure_date DATETIME NOT NULL, 
	arrival_date DATETIME NOT NULL, 
	departure_airport VARCHAR NOT NULL, 
	arrival_airport VARCHAR NOT NULL, 
	id_airplane VARCHAR NOT NULL, 
	num_of_avail_seats INTEGER NOT NULL, 
	PRIMARY KEY (id_flight), 
	FOREIGN KEY(departure_airport) REFERENCES airport (id_airport), 
	FOREIGN KEY(arrival_airport) REFERENCES airport (id_airport), 
	FOREIGN KEY(id_airplane) REFERENCES airplane (id_airplane)
);

CREATE TABLE reservation (
	id_reservation VARCHAR NOT NULL, 
	id_flight VARCHAR NOT NULL, 
	booking_status VARCHAR NOT NULL, 
	PRIMARY KEY (id_reservation), 
	UNIQUE (id_reservation), 
	FOREIGN KEY(id_flight) REFERENCES flight (id_flight)
);

CREATE TABLE airticket (
	id_airticket VARCHAR NOT NULL, 
	id_reservation VARCHAR NOT NULL, 
	departure_date DATETIME NOT NULL, 
	arrival_date DATETIME NOT NULL, 
	service_class VARCHAR NOT NULL, 
	id_passenger VARCHAR NOT NULL, 
	ticket_price FLOAT NOT NULL, 
	PRIMARY KEY (id_airticket), 
	FOREIGN KEY(id_reservation) REFERENCES reservation (id_reservation), 
	FOREIGN KEY(id_passenger) REFERENCES passenger (id_passenger)
);

CREATE TABLE employee (
	id_employee VARCHAR NOT NULL, 
	full_name VARCHAR NOT NULL, 
	job VARCHAR NOT NULL, 
	certification_license VARCHAR NOT NULL, 
	id_airplane VARCHAR NOT NULL, 
	PRIMARY KEY (id_employee), 
	FOREIGN KEY(id_airplane) REFERENCES airplane (id_airplane)
);

CREATE TABLE passenger (
	id_passenger VARCHAR NOT NULL, 
	full_name VARCHAR NOT NULL, 
	series_number_passport VARCHAR NOT NULL, 
	contacts VARCHAR NOT NULL, 
	PRIMARY KEY (id_passenger)
);

CREATE TABLE loyaltyprogram (
	id_client VARCHAR NOT NULL, 
	id_passenger VARCHAR NOT NULL, 
	loyalty_program VARCHAR NOT NULL, 
	discounts_bonuses FLOAT NOT NULL, 
	PRIMARY KEY (id_client), 
	FOREIGN KEY(id_passenger) REFERENCES passenger (id_passenger)
);

CREATE TABLE payment (
	id_reservation VARCHAR NOT NULL, 
	payment_state VARCHAR NOT NULL, 
	PRIMARY KEY (id_reservation), 
	FOREIGN KEY(id_reservation) REFERENCES reservation (id_reservation)
);
INSERT INTO "airplane" VALUES('AP001','ïàññàæèðñêèé','Boeing 737-800',189,'èñïðàâíîå');
INSERT INTO "airplane" VALUES('AP002','ïàññàæèðñêèé','Airbus A320neo',236,'èñïðàâíîå');
INSERT INTO "airplane" VALUES('AP003','ïàññàæèðñêèé','Embraer RRJ-190',114,'ðàáîòîñïîñîáíîå');
INSERT INTO "airplane" VALUES('AP004','ïàññàæèðñêèé','Airbus A321neo',240,'ðàáîòîñïîñîáíîå');
INSERT INTO "airplane" VALUES('AP005','ïàññàæèðñêèé','Airbus A319',140,'èñïðàâíîå');
INSERT INTO "airplane" VALUES('AP006','ïàññàæèðñêèé','Boeing 777-300',550,'ðàáîòîñïîñîáíîå');

INSERT INTO "airport" VALUES('JFK','Informational Guide to John F. Kennedy International Airport','Áèëäèíã 14, Íüþ-Éîðê 11430, ÑØÀ','JFK/KJFK');
INSERT INTO "airport" VALUES('DME','Äîìîäåäîâî','Ðîññèÿ, Ìîñêîâñêàÿ îáëàñòü, Äîìîäåäîâñêèé ðàéîí','DME/UUDD');
INSERT INTO "airport" VALUES('ICN','Ìåæäóíàðîäíûé àýðîïîðò Èí÷õîí','272 Ãîíãõàíã-ðî Äæóí-ãó, êîä 400-700','ICN/RKSI');
INSERT INTO "airport" VALUES('FCO','Ôüþìè÷èíî','Ëàöèî, Ðèì, Ôüþìè÷èíî, Via Luigi Bleriot','FCO');
INSERT INTO "airport" VALUES('AER','Ìåæäóíàðîäíûé àýðîïîðò Ñî÷è','Ðîññèèÿ, Àäëåð, Êðàñíîäàðñêèé êðàé, óë. Ìèðà, 50','AER/URSS');
INSERT INTO "airport" VALUES('VVO','Ìåæäóíàðîäíûé àýðîïîðò Âëàäèâîñòîê','Ðîññèÿ, Ïðèìîðñêèé êðàé, ã. Àðòåì, óë. Âëàäèìèðà Ñàéáåëÿ 41','VVO/UHWW');
INSERT INTO "airport" VALUES('SIN','Singapore Changi Airport','P.O. Box 1, Singapore 918 141','SIN/WSSS');
INSERT INTO "airport" VALUES('LED','Ìåæäóíàðîäíûé àýðîïîðò Ïóëêîâî','Ðîññèÿ, Ñàíêò-Ïåòåðáóðã, Ïóëêîâñêîå øîññå, 41, ëèò.ÇÀ','LED/ULLI');
INSERT INTO "airport" VALUES('MRV','Ìåæäóíàðîäíûé àýðîïîðò Ìèíåðàëüíûå Âîäû èìåíè Ì. Þ. Ëåðìîíòîâà','Ðîññèÿ, Ñòàâðîïîëüñêèé êðàé, ã. Ìèíåðàëüíûå Âîäû, Òåððèòîðèÿ Àýðîïîðò','MRV/URMM');
INSERT INTO "airport" VALUES('YVR','Vancouver International Airport','Øîññå Ãðàíò ÌàêÊîíà÷è, ã. Ðè÷ìîíä, ïðîâèíöèÿ Áðèòàíñêàÿ Êîëóìáèÿ, Êàíàäà','YVR/CYVR');
INSERT INTO "airport" VALUES('DXB','Àýðîïîðò Äóáàé','Department of Civil Aviation, P.O. Box 2525, Dubai, United Arab Emirates','DXB/OMDB');

INSERT INTO "airticket" VALUES('MN789012','ICN456','2023-12-20 01:30:00.000000','2023-12-20 09:55:00.000000','M','PAS0011',29639.0);
INSERT INTO "airticket" VALUES('KL123456','DXB012','2023-12-18 10:29:00.000000','2023-12-18 16:51:00.000000','D','PAS0006',340170.0);
INSERT INTO "airticket" VALUES('KL567890','DXB082','2023-12-18 10:29:00.000000','2023-12-18 16:51:00.000000','D','PAS0005',320100.0);
INSERT INTO "airticket" VALUES('IJ567990','JFK691','2023-12-16 00:05:00.000000','2023-12-16 10:00:00.000000','S','PAS0004',76791.0);
INSERT INTO "airticket" VALUES('ST987896','MRV456','2023-12-22 08:44:00.000000','2023-12-22 12:16:00.000000','S','PAS0007',10799.0);
INSERT INTO "airticket" VALUES('ST909597','MRV989','2023-12-22 08:44:00.000000','2023-12-22 12:16:00.000000','S','PAS0008',10799.0);
INSERT INTO "airticket" VALUES('ST509743','MRV019','2023-12-22 08:44:00.000000','2023-12-22 12:16:00.000000','S','PAS0009',5709.0);
INSERT INTO "airticket" VALUES('ST037826','MRV087','2023-12-22 08:44:00.000000','2023-12-22 12:16:00.000000','S','PAS0010',5100.0);

INSERT INTO "employee" VALUES('EM0001','Áåëîóñîâ Ñåðãåé Àëüáåðòîâ','ñòàðøèé äèñïåò÷åð','äà','');
INSERT INTO "employee" VALUES('EM0002','Ñåðïèîíîâ Íèêîëàé Ôèëèïïîâè÷','ñòàðøèé ïèëîò','äà','AP001');
INSERT INTO "employee" VALUES('EM0003','Íèêîëèí Ôåäîð Àëåêñàíäðîâè÷','ñòàðøèé ïèëîò','äà','AP003');
INSERT INTO "employee" VALUES('EM0004','Ñòåïíîâ Ðîìàí Êèðèëëîâè÷','âòîðîé ïèëîò','äà','AP003');
INSERT INTO "employee" VALUES('EM0005','Ëåñêîâà Àíàñòàñèÿ Àëåêñàíäðîâíà','ñòàðøèé áîðòïðîâîäíèê','äà','AP003');
INSERT INTO "employee" VALUES('EM0006','Âàëóåâ Íèêèòà Äåíèñîâè÷','ñòàæåð','íåò','');

INSERT INTO "flight" VALUES('BRU955','2023-12-16 00:05:00.000000','2023-12-16 10:00:00.000000','DME','JFK','AP003',114);
INSERT INTO "flight" VALUES('SBI2154','2023-12-20 01:30:00.000000','2023-12-20 09:55:00.000000','DME','ICN','AP002',236);
INSERT INTO "flight" VALUES('UAE130','2023-12-18 10:29:00.000000','2023-12-18 16:51:00.000000','DME','DXB','AP006',550);
INSERT INTO "flight" VALUES('SDM6355','2023-12-22 08:44:00.000000','2023-12-22 12:16:00.000000','LED','MRV','AP004',240);

INSERT INTO "loyaltyprogram" VALUES('LP0001','PAS0001','S7 Priority',2.0);
INSERT INTO "loyaltyprogram" VALUES('LP0002','PAS0002','Àýðîôëîò Áîíóñ',50.0);
INSERT INTO "loyaltyprogram" VALUES('LP0003','PAS0011','Àýðîôëîò Áîíóñ',80.0);
INSERT INTO "loyaltyprogram" VALUES('LP0004','PAS0011','S7 Priority',10.0);
INSERT INTO "loyaltyprogram" VALUES('LP0005','PAS0007','Êðûëüÿ',15.0);
INSERT INTO "loyaltyprogram" VALUES('LP0006','PAS0004','Àýðîôëîò Áîíóñ',60.0);

INSERT INTO "passenger" VALUES('PAS0001','Õàðèòîíîâ Ìàêñèì Ìàðêîâè÷','4965 207768','email1@example.com, +7(495)652-63-38');
INSERT INTO "passenger" VALUES('PAS0002','Õàðèòîíîâà Þëèÿ Íèêîëàåâíà','4579 699581','email2@example.com, +7(495)769-85-12');
INSERT INTO "passenger" VALUES('PAS0003','Õàðèòîíîâà Ìàðèÿ Ìàêñèìîâíà','4295 979396','');
INSERT INTO "passenger" VALUES('PAS0004','Ìîùåíñêèé Ìàêñèì Þðüåâè÷','4982 410174','+7(912)255-35-67, maksim9015@rambler.ru');
INSERT INTO "passenger" VALUES('PAS0005','ßãóíêèíà Êñåíèÿ Àíäðååâíà','4584 579044','+7(911)763-45-12, mirskaya@mail.ru');
INSERT INTO "passenger" VALUES('PAS0006','ßãóíêèí Àëåêñàíäð Äìèòðèåâè÷','4818 553753','+7(912)119-50-62');
INSERT INTO "passenger" VALUES('PAS0007','Áåëîóñîâ Ñåðãåé Íèêîëàåâè÷','4852 609717','+7(495)769-85-12, sergeybel@gmail.ru');
INSERT INTO "passenger" VALUES('PAS0008','Áåëîóñîâà Àííà Îëåãîâíà','4852 619917','+7(495)896-25-12, annabel@mail.ru');
INSERT INTO "passenger" VALUES('PAS0009','Áåëîóñîâ Àíäðåé Ñåðãååâè÷','4711 251795','');
INSERT INTO "passenger" VALUES('PAS0010','Áåëîóñîâ Àëåêñàíäð Ñåðãååâè÷','4711 296690','');
INSERT INTO "passenger" VALUES('PAS0011','Øèðîêîâà Åëåíà Äàíèëîâíà','4933 664782','+7(981)878-38-95, lena52@gmail.com');

INSERT INTO "payment" VALUES('ICN456','îïëà÷åíî');
INSERT INTO "payment" VALUES('DXB012','îïëà÷åíî');
INSERT INTO "payment" VALUES('DXB082','îïëà÷åíî');
INSERT INTO "payment" VALUES('JFK691','íå îïëà÷åíî');
INSERT INTO "payment" VALUES('MRV456','îæèäàåòñÿ');

INSERT INTO "reservation" VALUES('ICN456','SBI2154','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('ICN789','SBI2154','îòìåíåí');
INSERT INTO "reservation" VALUES('DXB012','UAE130','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('DXB082','UAE130','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('MRV456','SDM6355','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('MRV989','SDM6355','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('MRV019','SDM6355','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('MRV087','SDM6355','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('JFK705','BRU955','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('JFK219','BRU955','ïîäòâåðæäåí');
INSERT INTO "reservation" VALUES('JFK691','BRU955','ïîäòâåðæäåí');

