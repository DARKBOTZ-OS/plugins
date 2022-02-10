FROM DARKBOTZ-OS/darkbot:latest

RUN git clone https://github.com/DARKBOTZ-OS/Plugins.git /root/darkbot

WORKDIR /root/darkbot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/darkbot/bin:$PATH"

CMD ["python3", "-m", "darkbot"]
