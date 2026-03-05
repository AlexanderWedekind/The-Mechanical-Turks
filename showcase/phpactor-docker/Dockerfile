FROM php:8.2-cli

RUN apt-get update && apt-get install -y \
    git unzip libzip-dev \
    && docker-php-ext-install zip 

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

RUN composer global require phpactor/phpactor:^2024.06 --ignore-platform-reqs

ENV PATH="/root/.composer/vendor/bin:${PATH}"

WORKDIR /app
