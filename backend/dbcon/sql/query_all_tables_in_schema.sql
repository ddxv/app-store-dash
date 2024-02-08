SELECT table_name
FROM information_schema.tables
WHERE table_schema = :schema_name;
