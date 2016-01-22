# cs107-w16
Code and homework assignments for CSE 107 Winter 2016 @ UCSD

## Assigned Homework

- Classical Encryption (Due 1/19 11:59 AM)
- Block Ciphers (Due 1/21 at 11:59 AM)
- Pseudo-random Functions (Tentatively Due 1/28 at 11:59 AM)
    - exercise_1.py is optional
- Symmetric Encryption (TBA)

## Getting Started
To get started clone this repository with a `--recursive` flag:

    git clone --recursive https://github.com/avivkiss/cs107-w16.git

## Downloading Updates
First commit your changes locally and then

    git pull --rebase; git submodule update --init

## Turning in Homework
Before submitting please fill in the `student_info.json` file with your
information, this is how you will be identified for grading.

### Turnin from a personal computer
To perform a submission go into the root directory and type:

    ./turnin.py assignment_name

replacing "assignment_name" with the folder name of the assignment you wish to turn in. Before your first submission you may need to install the
[Python requests library](http://docs.python-requests.org/en/latest/user/install/).

### Turnin from a lab machine
If you need to turnin from the lab machines you can use [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Do the following in your project directory (you only need this command the first time):

    virtualenv env; source venv/bin/activate; pip install requests; deactivate

This will install requests in a local environment. Now, to turn in:

    source venv/bin/activate; ./turnin.py assignment_folder; deactivate


## More Documentation

You can find additional documentation at the [project site](https://avivkiss.github.io/cs107-w16/index.html).
