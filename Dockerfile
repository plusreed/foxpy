## BUILDING
##   (from project root directory)
##   $ docker build -t python-for-plusreed-foxpy .
##
## RUNNING
##   $ docker run python-for-plusreed-foxpy

FROM gcr.io/stacksmith-images/minideb-buildpack:jessie-r11

MAINTAINER Bitnami <containers@bitnami.com>

ENV STACKSMITH_STACK_ID="4n52h3h" \
    STACKSMITH_STACK_NAME="Python for plusreed/foxpy" \
    STACKSMITH_STACK_PRIVATE="1"

# Install required system packages
RUN install_packages libc6 libssl1.0.0 libffi6 libncurses5 libtinfo5 zlib1g libreadline6 libsqlite3-0

RUN bitnami-pkg install python-3.6.0-0 --checksum 44db2c169a8eb6ae3c64649c811a285f232d24f9e4773b81b0af57d151e45d63

ENV PATH=/opt/bitnami/python/bin:$PATH

## STACKSMITH-END: Modifications below this line will be unchanged when regenerating

# Python base template
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python"]
