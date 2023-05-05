FROM python:3.9-slim

COPY entrypoint.sh /entrypoint.sh
COPY generate_readme.py /generate_readme.py

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]