create table Kvantumyi (
	id integer primary key not null,
	Nazvanie_kvantuma text
);

create table Uchebnyie_gruppyi (
	id integer primary key not null,
	Nazvanie_gruppyi text,
	God_zachisleniya text
);

create table Uroveni_obucheniya (
	id integer primary key not null,
	Uroven text,
	Kolichestvo_chasov text,
	Uchebnyie_gruppyi_id integer,
	foreign key (Uchebnyie_gruppyi_id) references Uchebnyie_gruppyi(id) 
);

create table Adresa (
	id integer primary key not null,
	Polnyij_adres text,
	Goroda_id integer,
	foreign key (Goroda_id) references Goroda(id) 
);

create table Uchebnyie_zavedeniya (
	id integer primary key not null,
	Nazvanie_uchebnogo_zavedeniya text,
	Adresa_id integer,
	Direktora_id integer,
	Kontaktnyie_litsa_id integer,
	foreign key (Adresa_id) references Adresa(id) ,
	foreign key (Direktora_id) references Direktora(id) ,
	foreign key (Kontaktnyie_litsa_id) references Kontaktnyie_litsa(id) 
);

create table Klassyi (
	id integer primary key not null,
	Nomer_klassa text
);

create table Roditeli (
	id integer primary key not null
);

create table Sertifikatyi (
	id integer primary key not null,
	Nomer_sertifikata text,
	Prikazyi_id integer,
	foreign key (Prikazyi_id) references Prikazyi(id) 
);

create table Uchaschiesya (
	id integer primary key not null,
	Adresa_id integer,
	Uchebnyie_zavedeniya_id integer,
	Klassyi_id integer,
	Roditeli_id integer,
	Sertifikatyi_id integer,
	foreign key (Adresa_id) references Adresa(id) ,
	foreign key (Uchebnyie_zavedeniya_id) references Uchebnyie_zavedeniya(id) ,
	foreign key (Klassyi_id) references Klassyi(id) ,
	foreign key (Roditeli_id) references Roditeli(id) ,
	foreign key (Sertifikatyi_id) references Sertifikatyi(id) 
);

create table Prikazyi (
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

create table Kontaktnyie_litsa (
	id integer primary key not null
);

create table Lyudi (
	id integer primary key not null,
	FIO text,
	Nomer_telefona text,
	Adres_elektronnoj_pochtyi text
);

create table Prepodavateli (
	id integer primary key not null
);

create table Kvantum_Prepodavatel (
	id integer primary key not null,
	Kvantumyi_id integer,
	Prepodavateli_id integer,
	foreign key (Kvantumyi_id) references Kvantumyi(id) ,
	foreign key (Prepodavateli_id) references Prepodavateli(id) 
);

create table Kvantum_Uroven_obuchenija (
	id integer primary key not null,
	Kvantumyi_id integer,
	Uroveni_obucheniya_id integer,
	foreign key (Kvantumyi_id) references Kvantumyi(id) ,
	foreign key (Uroveni_obucheniya_id) references Uroveni_obucheniya(id) 
);

create table Uroven_obuchenija_Prepodavatel (
	id integer primary key not null,
	Uroveni_obucheniya_id integer,
	Prepodavateli_id integer,
	foreign key (Uroveni_obucheniya_id) references Uroveni_obucheniya(id) ,
	foreign key (Prepodavateli_id) references Prepodavateli(id) 
);

create table Uchashhijsja_Ljudi (
	id integer primary key not null,
	Uchaschiesya_id integer,
	Lyudi_id integer,
	foreign key (Uchaschiesya_id) references Uchaschiesya(id) ,
	foreign key (Lyudi_id) references Lyudi(id) 
);

create table Uchashhijsja_Gruppa (
	id integer primary key not null,
	Uchaschiesya_id integer,
	Uchebnyie_gruppyi_id integer,
	foreign key (Uchaschiesya_id) references Uchaschiesya(id) ,
	foreign key (Uchebnyie_gruppyi_id) references Uchebnyie_gruppyi(id) 
);

create table Uchashhijsja_Prikaz (
	id integer primary key not null,
	Uchaschiesya_id integer,
	Prikazyi_id integer,
	foreign key (Uchaschiesya_id) references Uchaschiesya(id) ,
	foreign key (Prikazyi_id) references Prikazyi(id) 
);

create table Prepodavatel_Ljudi (
	id integer primary key not null,
	Prepodavateli_id integer,
	Lyudi_id integer,
	foreign key (Prepodavateli_id) references Prepodavateli(id) ,
	foreign key (Lyudi_id) references Lyudi(id) 
);

create table Direktor_Ljudi (
	id integer primary key not null,
	Direktora_id integer,
	Lyudi_id integer,
	foreign key (Direktora_id) references Direktora(id) ,
	foreign key (Lyudi_id) references Lyudi(id) 
);

create table Kontaktnoe_lico_Ljudi (
	id integer primary key not null,
	Kontaktnyie_litsa_id integer,
	Lyudi_id integer,
	foreign key (Kontaktnyie_litsa_id) references Kontaktnyie_litsa(id) ,
	foreign key (Lyudi_id) references Lyudi(id) 
);

create table Roditel_Ljudi (
	id integer primary key not null,
	Roditeli_id integer,
	Lyudi_id integer,
	foreign key (Roditeli_id) references Roditeli(id) ,
	foreign key (Lyudi_id) references Lyudi(id) 
);

