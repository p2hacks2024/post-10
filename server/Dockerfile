FROM rust:1.62.0-slim

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh \
    && adduser -q --gecos "" --disabled-login rustuser

USER rustuser

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]