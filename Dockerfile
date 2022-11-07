FROM python:3.11.0

ADD /requirements.txt project/requirements.txt
ADD /application/api/config.txt project/application/api/config.txt
ADD /application/api/server.py project/application/api/server.py
ADD /application/api/utils.py project/application/api/utils.py
ADD /application/database/client/client.py project/application/database/client/client.py
ADD /application/database/interactions/Interactor.py project/application/database/interactions/Interactor.py
ADD /application/database/models/models.py project/application/database/models/models.py
ADD /application/database/exceptions.py project/application/database/exceptions.py

# установить необх пакеты
RUN pip install -r /project/requirements.txt
# поставить переменную среду и рабочую директорию (место, где запускается код в docker)
ENV PYTHONPATH="${PYTHONPATH}:/project/application"
WORKDIR /project


EXPOSE 5005
# поднимаем сервак с конфигом
CMD ['python', './application/api/server.py', '--config=./application/api/config.txt']