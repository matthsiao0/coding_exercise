FROM    ubuntu:latest

ARG     ARCH=${arch}
ARG     FFMPEG_VERSION=6.1.1

RUN     apt update --assume-yes && apt upgrade --assume-yes

RUN     apt install curl --assume-yes && \
            apt install make --assume-yes && \
            apt install xz-utils --assume-yes && \
            apt-get install build-essential --assume-yes

RUN     curl https://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.xz \
            -o ffmpeg.tar.xz

RUN     ls
RUN     tar -x -f ffmpeg.tar.xz

RUN     cd ffmpeg-${FFMPEG_VERSION} && \
            ./configure --enable-cross-compile && \
            make && \
            make install