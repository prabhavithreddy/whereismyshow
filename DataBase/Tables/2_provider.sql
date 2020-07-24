CREATE TABLE IF NOT EXISTS dbo.provider(
	"id" int GENERATED ALWAYS AS IDENTITY,
	"name" varchar(256) not null unique,
	icon_url varchar(1024) not null,
	inserted_date timestamp without time zone default (now() at time zone 'utc'),
	constraint pk_provider_id primary key(id) 
)
