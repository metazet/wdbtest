# wdbtest

Installation
------------

- pull repo
```bash
git clone git@github.com:metazet/wdbtest.git
```

- goto repo
```bash
cd wdbtest
```

- create virtualenv
```bash
virtualenv --no-site-packages --python=python3.7 venv
```

- use this venv
```bash
source venv/bin/activate
```

- install packages
```bash
pip install -r requirements.txt
```

Usage
-----

- run wdb
```bash
wdb.server.py
```

- run django app (in separated terminal)
```bash
python3 manage.py runserver
```

Now you can open http://127.0.0.1:8000/ in your browser and this django page will generate exception which will be caught by wdb. Enjoy :)