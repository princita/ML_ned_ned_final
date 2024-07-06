FROM kong:2.0

COPY kong.yml /usr/local/kong/declarative/kong.yml

ENV KONG_DATABASE=off
ENV KONG_DECLARATIVE_CONFIG=/usr/local/kong/declarative/kong.yml

EXPOSE 8000 8443 8001 8444

CMD ["kong", "start", "--v"]
