
FROM python:3.9

# set workdir
WORKDIR /app

# copy code from working DIR
COPY . . 

# install requirement
RUN pip install --no-cache-dir -r requirements.txt

# expose app to 8000 port
EXPOSE 8000

# set the cmd to run when container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]