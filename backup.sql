BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER UNIQUE,
	"phone"	TEXT NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "appointments" (
	"id"	INTEGER UNIQUE,
	"itemid"	INTEGER,
	"userid"	INTEGER,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "superadmins" (
	"id"	INTEGER UNIQUE,
	"phone"	TEXT UNIQUE
);
CREATE TABLE IF NOT EXISTS "admins" (
	"id"	INTEGER DEFAULT 0,
	"phone"	INTEGER
);
CREATE TABLE IF NOT EXISTS "items" (
	"id"	INTEGER UNIQUE,
	"title"	TEXT,
	"price"	INTEGER,
	"timecoof"	INTEGER DEFAULT 1,
	"specify"	TEXT DEFAULT 'No',
	"desc"	TEXT,
	"img"	TEXT DEFAULT 'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800',
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "users" VALUES (163170038,'79254565027','Федя');
INSERT INTO "users" VALUES (850151206,'79875595848','Тим');
INSERT INTO "users" VALUES (852191502,'+79506151022','Изменить имя');
INSERT INTO "users" VALUES (1063818741,'79867526035','Макс');
INSERT INTO "users" VALUES (5103935094,'79524589640','Наталья');
INSERT INTO "appointments" VALUES (17,13,852191502,' 2022-12-22');
INSERT INTO "appointments" VALUES (18,0,163170038,' 2022-12-22');
INSERT INTO "appointments" VALUES (19,13,852191502,' 2022-12-30');
INSERT INTO "appointments" VALUES (20,13,852191502,' 2022-12-29. По цене: 1000');
INSERT INTO "appointments" VALUES (21,13,852191502,' 2022-12-28. По цене: 1000');
INSERT INTO "appointments" VALUES (22,12,852191502,' 2022-12-30. По цене: 1000');
INSERT INTO "appointments" VALUES (23,15,852191502,' 2022-12-23. По цене: 1000');
INSERT INTO "appointments" VALUES (24,12,852191502,' 2022-12-24. По цене: 1000');
INSERT INTO "appointments" VALUES (25,15,852191502,' 2022-12-26. По цене: 1000');
INSERT INTO "appointments" VALUES (26,12,852191502,' 2022-12-22. По цене: 1000');
INSERT INTO "appointments" VALUES (27,14,852191502,' 2022-12-31. По цене: 1000');
INSERT INTO "appointments" VALUES (28,14,852191502,' 2022-12-24. По цене: 1000');
INSERT INTO "appointments" VALUES (29,13,852191502,' 2022-12-31. По цене: 1000');
INSERT INTO "appointments" VALUES (30,4,852191502,' 2022-12-30. По цене: 1000');
INSERT INTO "appointments" VALUES (31,4,852191502,' 2022-12-23. По цене: 1000');
INSERT INTO "appointments" VALUES (32,13,852191502,' 2022-12-29. По цене: 1000. ');
INSERT INTO "appointments" VALUES (33,13,852191502,' 2022-12-30. По цене: 1000. ');
INSERT INTO "appointments" VALUES (34,13,852191502,' 2022-12-28. По цене: 1000. . Время записи: 12:00 - 13:00');
INSERT INTO "appointments" VALUES (35,13,5103935094,' 2022-12-24. По цене: 1000. . Время записи: 8:00 - 9:00');
INSERT INTO "appointments" VALUES (36,15,852191502,' 2022-12-29. По цене: 1000. . Время записи: 20:00');
INSERT INTO "appointments" VALUES (37,2,852191502,' 2022-12-29. По цене: 1000. Время записи: Снять Площадка для мастер-классов. На 2022-12-29. По цене: 1000');
INSERT INTO "appointments" VALUES (38,22,852191502,' 2022-12-28. По цене: 1000. Время записи: Снять Звуковое оборудование. На 2022-12-28. По цене: 1000');
INSERT INTO "appointments" VALUES (39,16,852191502,' 2022-12-28. По цене: 1000. Время записи: 4:00');
INSERT INTO "appointments" VALUES (40,2,852191502,' 2022-12-29. По цене: 1000. Время записи: Снять Площадка для мастер-классов. На 2022-12-29. По цене: 1000');
INSERT INTO "appointments" VALUES (41,5,852191502,' 2022-12-30. По цене: 1000. Время записи: Снять Работа специалиста по свету (гафер). На 2022-12-30. По цене: 1000');
INSERT INTO "appointments" VALUES (42,13,852191502,' 2022-12-28. По цене: 1000. . Время записи: 1:00');
INSERT INTO "appointments" VALUES (43,1,852191502,' 2023-01-10. По цене: 1000. Время записи: Снять Зеленая зона. На 2023-01-10. По цене: 1000');
INSERT INTO "appointments" VALUES (44,13,852191502,' 2023-01-19. По цене: 1000. . Время записи: 4:00');
INSERT INTO "appointments" VALUES (45,13,852191502,' 2023-01-19. По цене: 1000. . Время записи: 23:00');
INSERT INTO "superadmins" VALUES (852191502,'+79506151022');
INSERT INTO "items" VALUES (0,'Белая зона (1200 рублей)',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (1,'Зеленая зона',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (2,'Площадка для мастер-классов',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (3,'Корпоративы',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (4,'Создание ролика под ключ',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (5,'Работа специалиста по свету (гафер)',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (6,'Работа специалиста по 3д(UnrealEngine)',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (7,'Работа видеографа',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (8,'Работа специалиста по цветокоррекции',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (9,'Работа моушн-дизайнера',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (10,'Работа сценариста',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (11,'Работа технического ассистента',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (12,'Посиделки и киновечера часовой доступ в пространство 200 рублей, в момент киновечера 300 рублей',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (13,'Зона PS5 (300 рублей в час)',1000,24,'No','Зона PS5 (300 рублей в час). По факту','https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (14,'Зона VR (500 рублей в час)',1000,24,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (15,'Фотозона (500 рублей 30 мин)',1000,48,'No',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (16,'Объективы',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (17,'Камеры',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (18,'Постоянный свет',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (19,'Импульсный свет',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (20,'Трансляционное оборудование',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (21,'Стойки, штативы, стабилизация',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (22,'Звуковое оборудование',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
INSERT INTO "items" VALUES (23,'Видеорекордеры',1000,1,'Obr',NULL,'https://via.placeholder.com/750/F2A650/FFFFFF/?text=ISO800');
COMMIT;
