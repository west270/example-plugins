FROM python:alpine
WORKDIR /src
ENTRYPOINT ["python", "-m"]

# Just be lazy and copy everything
COPY . .

# Install all the plugins
RUN pip install brewtils \
  && find . -maxdepth 1 -type d ! -name ".*" | xargs pip install --no-cache-dir
