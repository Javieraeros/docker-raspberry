FROM debian
RUN apt-get update && apt-get install -y transmission-daemon nano
RUN mkdir -p /var/lib/transmission-daemon/.config/transmission-daemon/resume && chmod 777 /var/lib/transmission-daemon/.config/transmission-daemon/resume
ADD settings.json /etc/transmission-daemon/settings.json
USER root
CMD service transmission-daemon start && tail -F /var/log/faillog
