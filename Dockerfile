FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .
CMD ["pip", "install", "fix_gdal-0.0.7.dev0-py3-none-any.whl"]
CMD ["pip", "install", "GDAL-3.0.1-cp37-cp37m-win_amd64.whl"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
