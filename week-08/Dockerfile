FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    libpam0g-dev \
    autoconf \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY samba-3.0.37.tar.gz .
RUN tar -xzf samba-3.0.37.tar.gz --strip-components=1

WORKDIR /build/source

RUN cp /usr/share/misc/config.guess . && cp /usr/share/misc/config.sub . && \
    ./configure \
    --build=aarch64-linux-gnu \
    --prefix=/usr/local/samba \
    --without-krb5 \
    --without-ads \
    --without-ldap \
    --without-acl-support \
    2>&1

RUN make -j1 CFLAGS="-w -fcommon" && make install

RUN mkdir -p /var/log/samba /tmp/share /usr/local/samba/var/locks

COPY smb.conf /usr/local/samba/lib/smb.conf
COPY usermap.sh /usr/local/samba/bin/usermap.sh
COPY start.sh /start.sh

RUN chmod +x /usr/local/samba/bin/usermap.sh /start.sh

EXPOSE 139 445

CMD ["/start.sh"]
