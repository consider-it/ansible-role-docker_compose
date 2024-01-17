# Links & Resources
# - https://hub.docker.com/_/nginx

FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

RUN rm -r /etc/nginx/conf.d/*
COPY ./conf.d /etc/nginx/conf.d

RUN rm -r /usr/share/nginx/html/*
COPY html/ /usr/share/nginx/html
