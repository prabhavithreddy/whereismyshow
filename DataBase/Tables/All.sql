CREATE TABLE IF NOT EXISTS dbo.title(
	"id" int GENERATED ALWAYS AS IDENTITY,
	title_id varchar(256) not null unique,
	picture varchar(1024) null,
	"name" varchar(256) not null,
	inserted_date timestamp without time zone not null default (now() at time zone 'utc'),
	constraint pk_title_id primary key(id) 
)
;
CREATE TABLE IF NOT EXISTS dbo.provider(
	"id" int GENERATED ALWAYS AS IDENTITY,
	"name" varchar(256) not null unique,
	icon_url varchar(1024) not null,
	inserted_date timestamp without time zone not null default (now() at time zone 'utc'),
	constraint pk_provider_id primary key(id) 
)
;
create table if not exists dbo.reference(
	"id" int generated always as identity,
	"name" varchar(256) not null unique,
	url varchar(1024) not null unique,
	inserted_date timestamp without time zone not null default (now() at time zone 'utc'),
	constraint pk_reference_id primary key(id) 
)
;
CREATE TABLE IF NOT EXISTS dbo.title_provider(
	"id" int GENERATED ALWAYS AS IDENTITY,
	title_id int not null,
	provider_id int not null,
	url varchar(1024) not null,
	inserted_date timestamp without time zone not null default (now() at time zone 'utc'),
	constraint pk_title_provider_id primary key(id),
	constraint fk_title_provider_title foreign key (title_id) references dbo.title(id),
	constraint fk_title_provider_provider foreign key (provider_id) references dbo.provider(id)
);
CREATE TABLE IF NOT EXISTS dbo.title_references(
	"id" int GENERATED ALWAYS AS IDENTITY,
	title_id int not null,
	reference_id int not null,
	meta_data varchar(1024) not null,
	inserted_date timestamp without time zone not null default (now() at time zone 'utc'),
	constraint pk_title_references_id primary key(id),
	constraint fk_title_references_title foreign key (title_id) references dbo.title(id),
	constraint fk_title_references_reference foreign key (reference_id) references dbo.reference(id)
);