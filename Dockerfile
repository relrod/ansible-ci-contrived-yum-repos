FROM centos:7

RUN yum -y install createrepo rpmdevtools

VOLUME /mnt
WORKDIR /mnt
