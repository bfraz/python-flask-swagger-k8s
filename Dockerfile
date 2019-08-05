FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 31722
RUN python setup.py develop
ENTRYPOINT ["python"]
CMD ["rest_api_demo/app.py"]
