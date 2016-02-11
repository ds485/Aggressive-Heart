# Aggressive-Heart

## install on fedora 23
    dnf -y mongodb-server python-pymongo python-parse python-omniORB omniORB-devel omniORB-servers
    systemctl start mongod

## test installation
    1. set user and pw in test.py
    2. run db init
        python ./initdb.py
    3. run server (this prints the AoFactory IOR)
        python ./code.py
    4. run the test.py and at the AoFactory IOR as first arg
        python ./test.py <IOR>

## Help
    To create a custom application model simply edit the ApplicationModel.conf
