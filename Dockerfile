FROM tiangolo/uwsgi-nginx:python3.8
ADD . /code
WORKDIR /code
EXPOSE 5000
COPY ./app/requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app/app.py /code
CMD ["python", "app/app.py"]