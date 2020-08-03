CREATE TABLE IF NOT EXISTS dbo.provider(
	"id" int GENERATED ALWAYS AS IDENTITY,
	"name" varchar(256) not null unique,
	icon_url varchar(1024) not null,
	"url" varchar(1024) not null,
	logo varchar(1024) null,
	inserted_date timestamp without time zone default (now() at time zone 'utc'),
	constraint pk_provider_id primary key(id) 
)
;
alter TABLE dbo.provider 
add COLUMN "url" varchar(1024) null
;
alter TABLE dbo.provider 
add COLUMN logo varchar(1024) null