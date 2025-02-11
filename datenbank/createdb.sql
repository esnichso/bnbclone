--clear Tabellen
DROP TABLE IF EXISTS Wohnungen;
DROP TABLE IF EXISTS Vermieter;
DROP TABLE IF EXISTS Mieter;
DROP TABLE IF EXISTS Buchungen;

--Create Wonungstabelle
CREATE TABLE "Wohnungen" (
	"WID"	INTEGER NOT NULL UNIQUE,
	"Stadt"	TEXT NOT NULL,
	"Land"	TEXT NOT NULL,
	"Betten"	INTEGER NOT NULL,
	"VermieterID"	INTEGER NOT NULL,
	PRIMARY KEY("WID" AUTOINCREMENT),
	FOREIGN KEY("VermieterID") REFERENCES "Vermieter"("VermieterID")
);



-- Create Vermietertabelle
CREATE TABLE "Vermieter" (
	"VermieterID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	PRIMARY KEY("VermieterID" AUTOINCREMENT)
);

-- Create Mietertabelle
CREATE TABLE "Mieter" (
	"MieterID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	PRIMARY KEY("MieterID" AUTOINCREMENT)
);

-- Create Buchungstabelle
CREATE TABLE "Buchungen" (
	"BuchungsID"	INTEGER NOT NULL UNIQUE,
	"WohnungsID"	INTEGER NOT NULL,
	"MieterID"	INTEGER NOT NULL,
	"Datum"	TEXT NOT NULL,
	FOREIGN KEY("MieterID") REFERENCES "Mieter"("MieterID"),
	FOREIGN KEY("WohnungsID") REFERENCES "Wohnungen"("WID"),
	PRIMARY KEY("BuchungsID" AUTOINCREMENT)
);


--Vermieter erstellen
INSERT INTO "main"."Vermieter" ("Name", "Email") VALUES ('Lucas Buschbeck', 'buschbeck.lucas@gmail.com');
INSERT INTO "main"."Vermieter" ("Name", "Email") VALUES ('Emilian Bohlmann', 'emilian@bohlmann.de');

--Wohnungen erstellen
INSERT INTO "main"."Wohnungen" ("Stadt", "Land", "Betten", "VermieterID") VALUES ('Berlin', 'Deutschland', '4', '1');
INSERT INTO "main"."Wohnungen" ("Stadt", "Land", "Betten", "VermieterID") VALUES ('Madrid', 'Spanien', '6', '1');

-- Mieter erstellen
INSERT INTO "main"."Mieter" ("Name", "Email") VALUES ('Ben Gotschalk', 'ben.gotschalk@gmx.de');

-- Buchung erstellen
INSERT INTO "main"."Buchungen" ("WohnungsID", "MieterID", "Datum") VALUES ('1', '1', '01.01.2025-01.01.2025');




