CREATE TABLE IF NOT EXISTS dbo.title_provider(
	"id" int GENERATED ALWAYS AS IDENTITY,
	title_id int not null,
	provider_id int not null,
	url varchar(1024) not null,
	inserted_date timestamp without time zone default (now() at time zone 'utc'),
	constraint pk_title_provider_id primary key(id),
	constraint fk_title_provider_title foreign key (title_id) references dbo.title(id),
	constraint fk_title_provider_provider foreign key (provider_id) references dbo.provider(id)
)