FROM python:3.7-alpine
run apk add --no-cache git && pip install --no-cache-dir flask requests gunicorn && git clone https://github.com/vladsimachkov/telegram_proxy.git
CMD ["gunicorn", "-w 4", "main:app"]