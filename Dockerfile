FROM python:3.10
WORKDIR /myapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#ENV PORT=8000

CMD ["echo", "image Docket Orange County Letting"]

RUN pip install --upgrade pip
COPY ./requirements.txt /myapp/
RUN pip install -r requirements.txt


COPY . /myapp
EXPOSE 8000

#RUN python manage.py collectstatic
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD python manage.py runserver

# run gunicorn
CMD gunicorn Python-OC-Lettings-FR.wsgi:application -- bind @.0.0.0:$PORT



