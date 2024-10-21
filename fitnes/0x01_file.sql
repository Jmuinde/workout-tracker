--

create DATABASE if not exists workout_dtbse;
USE workout_dtbse;

create TABLE if not exists persons
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	age INT,
	gender VARCHAR(256),
	height_cms INT,
	weight_kgs INT,
	PRIMARY KEY(id)
	
);

create TABLE if not exists exercise
(
	exercise_id INT UNIQUE NOT NULL,
	exercise_name VARCHAR(256),
	exercise_ype set('Strength','Cardio'),
	muscle_group set('Chest', 'Back', 'Legs', 'Shoulders', 'Arms'),
	difficulty ENUM('low', 'Medium', 'High'),
	PRIMARY KEY(exercise_id),
	person_id int not null,
	FOREIGN KEY(person_id)
		REFERENCES workout_dtbse.persons(id)
);

create TABLE if not exists sessions
(
	duration varchar(20) not null,
	reps int default 0,
	sets int default 0,
	weights_used int default 0,
	person_id int not null,
	FOREIGN KEY(person_id)
		REFERENCES workout_dtbse.persons(id)
);
create TABLE if not exists time_tracking
(
	day Date,
	week INT,
	month INT check(month between 1 and 12),
	year INT check(year >=2024),
	person_id int not null,
	FOREIGN KEY(person_id)
		REFERENCES workout_dtbse.persons(id)
);
create TABLE if not exists nutrition
(
	meals_perday int,
	composition set('Carbs', 'Proteins', 'Fats'),
	prepration set('homemade', 'resturant', 'fast food joint'),
	person_id int not null,
	FOREIGN KEY(person_id)
		REFERENCES workout_dtbse.persons(id)
);







