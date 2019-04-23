"""
This is user defined workflow definition
"""

import job_script_list

"""
# first initiate dag:
dag_def = []

# then add individual jobs:

# add job no.1
dag_def.append({
    "job_name" : job's name (referred to by other jobs),
    "upstream_file_table" : the upstream folder locations,
    "downstream_file_table" : the downstream folder locations,
    "trigger_type" : trigger by dependency or by clock,
    "depend_on" : the list of jobs that needs to be done before this job can start,
    "action" : the action performed by this job, usually consumes the input and output locations,
    “retries" : retry if the job failed
})

# add job no.2
dag_def.append({
    "job_name" : job's name (referred to by other jobs),
    "upstream_file_table" : the upstream folder locations,
    "downstream_file_table" : the downstream folder locations,
    "trigger_type" : trigger by dependency or by clock,
    "depend_on" : the list of jobs that needs to be done before this job can start,
    "action" : the action performed by this job, usually consumes the input and output locations,
})

# add job no.3
dag_def.append({
    "job_name" : job's name (referred to by other jobs),
    "upstream_file_table" : the upstream folder locations,
    "downstream_file_table" : the downstream folder locations,
    "trigger_type" : trigger by dependency or by clock,
    "depend_on" : the list of jobs that needs to be done before this job can start,
    "action" : the action performed by this job, usually consumes the input and output locations,
})
"""
