CREATE TABLE IF NOT EXISTS dbo.title(
	"id" int GENERATED ALWAYS AS IDENTITY,
	title_id varchar(256) not null unique,
	picture varchar(1024) null,
	"name" varchar(256) not null,
	inserted_date timestamp without time zone default (now() at time zone 'utc'),
	constraint pk_title_id primary key(id) 
)
