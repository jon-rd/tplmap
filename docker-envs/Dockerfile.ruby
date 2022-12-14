FROM ruby:3.1-bullseye

RUN gem install slim tilt cuba rack rackup
RUN apt-get update && apt-get install --upgrade dnsutils python3-pip -y
RUN pip3 install requests PyYAML

COPY  . /apps/
WORKDIR /apps/tests/

EXPOSE 15005

CMD cd env_ruby_tests && rackup --host 0.0.0.0 --port 15005
