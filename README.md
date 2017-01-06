rdb-fullstack
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

To run the tournament project you need to:

- type "git clone https://github.com/DavidKnott/fullstack-nanodegree-vm.git" into your terminal

- enter "cd fullstack-nanodegree-vm/vagrant"

- "vagrant up" (you can turn off the VM with 'vagrant halt')

- "vagrant ssh" (from here you can type 'exit' to log out)

- cd /vagrant/tournament

- psql -f tournament.sql

- python tournament_test.py

- if it works correctly you should see "Success!  All tests pass!"