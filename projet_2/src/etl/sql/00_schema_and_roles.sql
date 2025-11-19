-- 00_schema_and_roles.sql
CREATE SCHEMA IF NOT EXISTS amazon AUTHORIZATION admin;
SET search_path TO amazon, public;

DO $$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'etl') THEN
    CREATE ROLE etl LOGIN PASSWORD 'etl_password';
  END IF;
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'readonly_user') THEN
    CREATE ROLE readonly_user LOGIN PASSWORD 'my_jedha_student_pwd_for_rncp_37172';
  END IF;
END$$;

GRANT USAGE ON SCHEMA amazon TO etl, readonly_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA amazon GRANT SELECT ON TABLES TO readonly_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA amazon GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO etl;
