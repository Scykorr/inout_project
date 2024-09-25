#!/bin/bash

echo "#> Обновляю проект из Git[Oscar]"
git pull

echo "#> Активирую виртуальное окружение"
source env/bin/activate

echo "#> Устанавливаю зависимости и обновляю БД и статику"
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput

echo "#> Процедура обновления закончена. Деактивирую виртуальное окружение"
deactivate

echo "#> Перезапускаю сервисы"
systemctl restart site
systemctl restart nginx

echo "#> Все необходимые процедуры выполнены, можно проверять обновления"
