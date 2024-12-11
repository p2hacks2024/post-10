FROM rust:slim

# 必要なパッケージをインストール
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends libsqlite3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# エントリポイントスクリプトをコピー
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh \
    && adduser --disabled-password --gecos "" rustuser

# ユーザーを切り替え
USER rustuser

WORKDIR /app

CMD ["cargo", "run"]
