# base image  
FROM python:3.10.10

# where your code lives  
WORKDIR /apps

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory.
COPY . .
# run this command to install all dependencies
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 9000
# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]