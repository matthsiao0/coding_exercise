FROM python:3.11

ENV FLASK_APP=app.py
RUN pip install flask

# COPY /e_commerce_api/app.py /app/app.py

# ENTRYPOINT flask --app /app/app run --host 0.0.0.0 --port 8000