FROM python:3.9-alpine
COPY . /opt
# No dependencies for now
# RUN pip install --no-cache-dir -r /opt/requirements.txt
ENTRYPOINT ["python", "/opt/codelephant/codelephant/main.py", "/app"]