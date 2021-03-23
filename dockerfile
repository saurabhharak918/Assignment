FROM python:3.7.6

COPY Templates .


COPY Assignment.py .

COPY urlFile.text .

Run pip install flask


CMD ["python","./Assignment.py"]