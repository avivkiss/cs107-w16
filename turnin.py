#!/usr/bin/env python

import json, urlparse, os, argparse, requests, glob

SERVER_URL = "http://127.0.0.1:5000"

def path_leaf(path):
  return path.strip('/').strip('\\').split('/')[-1].split('\\')[-1]

def check_submission(problem_set, student_id):
  # My API (2)
  # GET http://127.0.0.1:5000/did_submit/A10940122/2

  try:
    response = requests.get(
      url= urlparse.urljoin(SERVER_URL, "/did_submit/%s/%s" % (student_id, problem_set)),
    )

    jr = json.loads(response.content)
    return jr['did_submit']

  except requests.exceptions.RequestException:
    print('HTTP Request to check submission status failed')

    return False

def submit(problem_set, student_id, turnin):
  files = {}
  for f in turnin:
    files[f] = open(f, 'rb')

  try:
    response = requests.post(
      url=SERVER_URL,
      params={
        "student_id": student_id,
        "problem_set": problem_set,
      },
      files=files
    )
    
    return response.content
  except requests.exceptions.RequestException:
    return 'HTTP Request failed'


student = json.load(open("student_info.json", 'r'))

if student['student_id'] == 'A0000000':
  print "You must fill in the student_info.json file before attempting a turnin."
  exit(0)

# check to see if already submitted
parser = argparse.ArgumentParser(description='Turnin your assignment.')

parser.add_argument('assignment', type=str, help='Directory with assignment to turn in.')

args = vars(parser.parse_args())
problem_set = path_leaf(args.get('assignment'))
student_id = student['student_id']

if check_submission(problem_set, student_id) is True:
  resubmit = raw_input("It looks like you've already made a submission, would you like to resubmit? (y/n) ")
  if resubmit[0] is 'n':
    exit(0)

# glob the assignment for py, pdf and txt

turnin = []

turnin.extend(glob.glob(os.path.join(problem_set, '*.pdf')))
turnin.extend(glob.glob(os.path.join(problem_set, '*.txt')))
turnin.extend(glob.glob(os.path.join(problem_set, '*.py')))
turnin.append('student_info.json')

# send assignment files and student info with problem set arg name

print submit(problem_set, student_id, turnin)
