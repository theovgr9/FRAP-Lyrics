DROP TABLE "Artist";
DROP TABLE "Album";

CREATE TABLE "Artist"(
	"id_artiste"	INTEGER NOT NULL UNIQUE,
	"nom_artiste" 	TEXT,
	PRIMARY KEY("id_artiste")
	);

CREATE TABLE "Album"(
	"id_artiste"	INTEGER NOT NULL,
	"nom_album"		INTEGER,
	FOREIGN KEY("id_artiste") REFERENCES Artist(id_artiste)
	);
