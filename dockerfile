FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000