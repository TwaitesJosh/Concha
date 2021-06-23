FROM python:3.7
COPY ./app.py /deploy/
COPY ./model.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./csv_for_model_3_input.csv /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:./Concha"
EXPOSE 80
CMD python app.py