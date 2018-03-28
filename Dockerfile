FROM python:alpine
WORKDIR /src
ENTRYPOINT ["python", "-m"]

# Just be lazy and copy everything
COPY plugins .

# Until brewtils with yapconf is published ...
RUN pip install --no-cache-dir "https://github.com/beer-garden/brewtils/archive/master.zip"

# Install all the plugins
RUN find . -maxdepth 1 -type d ! -path "." | xargs pip install --no-cache-dir
