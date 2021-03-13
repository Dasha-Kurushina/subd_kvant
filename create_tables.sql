create table Kvantumy (
	id integer primary key not null,
	Nazvanie_kvantuma text
);

create table Uchebnye_gruppy (
	id integer primary key not null,
	Nazvanie_gruppy text,
	God_zachislenija text
);

create table Uroveni_obuchenija (
	id integer primary key not null,
	Uroven text,
	Kolichestvo chasov text,
	Uchebnye_gruppy_id integer,
	foreign key (Uchebnye_gruppy_id) references Uchebnye_gruppy(id) 
);

create table Adresa (
	id integer primary key not null,
	Polnyj_adres text,
	Goroda_id integer,
	foreign key (Goroda_id) references Goroda(id) 
);

create table Uchebnye_zavedenija (
	id integer primary key not null,
	Nazvanie_uchebnogo_zavedenija text,
	Adresa_id integer,
	Direktora_id integer,
	Kontaktnye_lica_id integer,
	foreign key (Adresa_id) references Adresa(id) ,
	foreign key (Direktora_id) references Direktora(id) ,
	foreign key (Kontaktnye_lica_id) references Kontaktnye_lica(id) 
);

create table Klassy (
	id integer primary key not null,
	Nomer_klassa text
);

create table Roditeli (
	id integer primary key not null
);

create table Sertifikaty (
	id integer primary key not null,
	Nomer_sertifikata text,
	Prikazy_id integer,
	foreign key (Prikazy_id) references Prikazy(id) 
);

create table Uchashhiesja (
	id integer primary key not null,
	Adresa_id integer,
	Uchebnye_zavedenija_id integer,
	Klassy_id integer,
	Roditeli_id integer,
	Sertifikaty_id integer,
	foreign key (Adresa_id) references Adresa(id) ,
	foreign key (Uchebnye_zavedenija_id) references Uchebnye_zavedenija(id) ,
	foreign key (Klassy_id) references Klassy(id) ,
	foreign key (Roditeli_id) references Roditeli(id) ,
	foreign key (Sertifikaty_id) references Sertifikaty(id) 
);

create table Prikazy (
	id integer primary key not null,
	Vid_prikaza text,
	Nomer_prikaza text,
	Tekst text
);

create table Goroda (
	id integer primary key not null,
	Nazvanie_goroda text
);

create table Direktora (
	id integer primary key not null
);

create table Kontaktnye_lica (
	id integer primary key not null
);

create table Ljudi (
	id integer primary key not null,
	FIO text,
	Nomer_telefona text,
	Adres_jelektronnoj_pochty text
);

create table Prepodavateli (
	id integer primary key not null
);

create table Kvantum_Prepodavatel (
	id integer primary key not null,
	Kvantumy_id integer,
	Prepodavateli_id integer,
	foreign key (Kvantumy_id) references Kvantumy(id) ,
	foreign key (Prepodavateli_id) references Prepodavateli(id) 
);

create table Kvantum_Uroven_obuchenija (
	id integer primary key not null,
	Kvantumy_id integer,
	Uroveni_obuchenija_id integer,
	foreign key (Kvantumy_id) references Kvantumy(id) ,
	foreign key (Uroveni_obuchenija_id) references Uroveni_obuchenija(id) 
);

create table Uroven_obuchenija_Prepodavatel (
	id integer primary key not null,
	Uroveni_obuchenija_id integer,
	Prepodavateli_id integer,
	foreign key (Uroveni_obuchenija_id) references Uroveni_obuchenija(id) ,
	foreign key (Prepodavateli_id) references Prepodavateli(id) 
);

create table Uchashhijsja_Ljudi (
	id integer primary key not null,
	Uchashhiesja_id integer,
	Ljudi_id integer,
	foreign key (Uchashhiesja_id) references Uchashhiesja(id) ,
	foreign key (Ljudi_id) references Ljudi(id) 
);

create table Uchashhijsja_Gruppa (
	id integer primary key not null,
	Uchashhiesja_id integer,
	Uchebnye_gruppy_id integer,
	foreign key (Uchashhiesja_id) references Uchashhiesja(id) ,
	foreign key (Uchebnye_gruppy_id) references Uchebnye_gruppy(id) 
);

create table Uchashhijsja_Prikaz (
	id integer primary key not null,
	Uchashhiesja_id integer,
	Prikazy_id integer,
	foreign key (Uchashhiesja_id) references Uchashhiesja(id) ,
	foreign key (Prikazy_id) references Prikazy(id) 
);

create table Prepodavatel_Ljudi (
	id integer primary key not null,
	Prepodavateli_id integer,
	Ljudi_id integer,
	foreign key (Prepodavateli_id) references Prepodavateli(id) ,
	foreign key (Ljudi_id) references Ljudi(id) 
);

create table Direktor_Ljudi (
	id integer primary key not null,
	Direktora_id integer,
	Ljudi_id integer,
	foreign key (Direktora_id) references Direktora(id) ,
	foreign key (Ljudi_id) references Ljudi(id) 
);

create table Kontaktnoe_lico_Ljudi (
	id integer primary key not null,
	Kontaktnye_lica_id integer,
	Ljudi_id integer,
	foreign key (Kontaktnye_lica_id) references Kontaktnye_lica(id) ,
	foreign key (Ljudi_id) references Ljudi(id) 
);

create table Roditel_Ljudi (
	id integer primary key not null,
	Roditeli_id integer,
	Ljudi_id integer,
	foreign key (Roditeli_id) references Roditeli(id) ,
	foreign key (Ljudi_id) references Ljudi(id) 
);

