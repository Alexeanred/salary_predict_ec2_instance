FROM python:3.9

# work with app
WORKDIR /code
# copy file requirements vào app
COPY ./requirements.txt /code/requirements.txt
# install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# CMD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]