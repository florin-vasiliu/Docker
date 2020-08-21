# pull official base image
FROM postgres:12-alpine

# run create.sql on init
ADD create.sql /socker-entrypoint-initdb.d
