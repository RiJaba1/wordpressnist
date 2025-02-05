FROM python:3

WORKDIR /usr/src/app

#RUN python -m venv /opt/venv
#ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt --root-user-action=ignore

COPY . .

ENTRYPOINT [ "python", "./wordpress.py" ]
