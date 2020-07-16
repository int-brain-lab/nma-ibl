FROM sinzlab/pytorch

ADD . /src/nma-ibl

RUN pip install -e /src/nma-ibl

