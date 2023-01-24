FROM public.ecr.aws/lambda/python:3.8

RUN yum install unzip -y
RUN python3.8 -m pip install --upgrade pip

ENV PYTHONUNBUFFERED 1

RUN cat /etc/os-release

# install headless chrome
    # RUN curl -O  https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
    COPY google-chrome-stable_current_x86_64.rpm ./
    RUN yum install ./google-chrome-stable_current_x86_64.rpm -y


# download chromedriver
    RUN mkdir /opt/chrome
    # RUN curl -O https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver_linux64.zip
    COPY chromedriver_linux64.zip ./
    RUN unzip chromedriver_linux64.zip -d /opt/chrome

COPY app.py requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
