FROM        eb_ubuntu
MAINTAINER  hong4367@gmail.com

# 현재 경로의 모든 파일들을 컨테이너의 /srv/deploy_eb_docker폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd srvdeploy_eb_docker와 같은 효과
WORKDIR     /srv/deploy_eb_docker
# requirements 설치
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/deploy.txt

# RUN        /root/.pyenv/versions/deploy_eb_docker/bin/uwsgi --http :8000 --chdir /srv/deploy_eb_docker/django_app -w config.settings.debug

COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/


COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf


RUN         /root/.pyenv/versions/deploy_eb_docker/bin/python /srv/deploy_eb_docker/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput
CMD         supervisord -n
EXPOSE      80 8000