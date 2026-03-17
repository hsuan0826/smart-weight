CREATE TABLE "users" (
  "user_id" integer PRIMARY KEY,
  "email" varchar UNIQUE NOT NULL,
  "password_hash" varchar(60) NOT NULL,
  "first_name" varchar,
  "last_name" varchar,
  "dob" date NOT NULL,
  "initial_wt" float NOT NULL,
  "target_wt" float,
  "height" float,
  "created_at" timestamp NOT NULL DEFAULT 'now()'
);

CREATE TABLE "weight_log" (
  "log_id" integer PRIMARY KEY,
  "weight" float NOT NULL,
  "time_of_day" varchar NOT NULL,
  "user_id" integer NOT NULL,
  "date" date NOT NULL,
  "logged_at" timestamp NOT NULL DEFAULT 'now()'
);

ALTER TABLE "weight_log" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id") DEFERRABLE INITIALLY IMMEDIATE;
