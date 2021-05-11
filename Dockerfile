FROM python:3.7
RUN pip install fastapi uvicorn sqlalchemy
EXPOSE 80
COPY ./ /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]