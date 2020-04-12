FROM python:3.7-alpine
RUN pip install flask requests gunicorn
CMD ["gunicorn", "-w 4", "main:app"]