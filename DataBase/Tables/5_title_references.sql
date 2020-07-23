CREATE TABLE IF NOT EXISTS dbo.title_references(
	"id" int GENERATED ALWAYS AS IDENTITY,
	title_id int not null,
	reference_id int not null,
	meta_data varchar(1024) not null,
	inserted_date timestamp without time zone default (now() at time zone 'utc'),
	constraint pk_title_references_id primary key(id),
	constraint fk_title_references_title foreign key (title_id) references dbo.title(id),
	constraint fk_title_references_reference foreign key (reference_id) references dbo.reference(id)
)