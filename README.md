# Aggressive-Heart

## install on fedora 23
    dnf -y mongodb-server python-pymongo python-parse python-omniORB omniORB-devel omniORB-servers
    systemctl start mongod

## test installation
    1. set user and pw in test.py
    2. run db init
        python ./initdb.py
    3. start omniNames
        omniNames -datadir /tmp -start 2809
    4. run server
        python ./code.py
    5. run the test.py
        python ./test.py

## Help
    To create a custom application model simply edit the ApplicationModel.conf
