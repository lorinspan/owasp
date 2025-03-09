FROM postgres:13

ENV POSTGRES_DB=owasp
ENV POSTGRES_USER=spanlorin
ENV POSTGRES_PASSWORD=owasp

COPY init.sql /docker-entrypoint-initdb.d/
