create table if not exists dbo.reference(
	"id" int generated always as identity,
	"name" varchar(256) not null unique,
	icon_url varchar(1024) not null unique,
	inserted_date timestamp without time zone default (now() at time zone 'utc'),
	constraint pk_reference_id primary key(id) 
)
