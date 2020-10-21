FROM python:3.8
MAINTAINER MEK

ENV PYTHONUNBUFFERED 1

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
      && ln -sf /dev/stderr /var/log/nginx/error.log


# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/djangoRestApi
COPY start-server.sh /opt/app/
COPY  ./requirements/dev.txt opt/app/requirements.txt
COPY . /opt/app/djangoRestApi/
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app


# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]

