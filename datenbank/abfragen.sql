-- Wohnungen auflisten
SELECT * FROM Vermieter, Wohnungen WHERE Vermieter.VermieterID == Wohnungen.VermieterID;

--Buchungen auflisten
SELECT Buchungen.BuchungsID, Mieter.name, Wohnungen.WID, Buchungen.Datum FROM Buchungen, Mieter, Wohnungen WHERE Buchungen.WohnungsID = Wohnungen.WID
