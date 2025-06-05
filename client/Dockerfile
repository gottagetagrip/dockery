FROM python:3.10-slim
 
RUN pip install mysql-connector-python
 
COPY client.py /client.py
 
CMD ["python", "/client.py"]