"""
This is the workflow module (library)
"""
from graph_utility import Graph

class JobFlow:
    """
    use centralized marker table and pre-assigned input/output filenames to avoid ambiguity (just like the fact that
    SCOPE script must have at least one input and output)
    In this case, there will be a name assigner that should be independent from actual python job scripts. The python
    job scrpit should take input/output file path as script parameters, just like SCOPE script does.
    The whole system will work like the Cosmos/SCOPE system and workflow.
    """
    def __init__(self):
        self.job_list = []
        self.dag_pointing_to_upstream = {}
        self.dag_pointing_to_downstream = {}
        self.job_lookup_table = {}
        self.job_id_to_name = {}
        self.job_name_to_id = {}

    def load_dag_definition(self, dag_definition):
        """ key entry point for loading workflow definition """
        self.job_list = []
        for job_def in dag_definition:
            self.job_list.append(EtlJob(job_def))
        self.create_reference_tables()
        self.create_dag_from_reference_tables()
        self.dag_sanity_check()

    def create_reference_tables(self):
        for job in self.job_list:
            self.job_lookup_table[job.job_uuid] = job
            self.job_id_to_name[job.job_uuid] = job.job_name
            self.job_name_to_id[job.job_name] = job.job_id

    def create_dag_from_reference_tables(self):
        for job in self.job_list:
            self.job_lookup_table[job.job_uuid] = job
            self.job_name_to_id[job.job_name] = job.job_id

        # setup dag using job_uuid as node value
        for job in self.job_list:
            self.dag_pointing_to_upstream[job.job_uuid] = []
            for up_stream_job_name in job.depend_on:
                upstream_job_id = self.job_name_to_id[up_stream_job_name]
                self.dag_pointing_to_upstream[job.job_uuid].append(upstream_job_id)

        self.dag_pointing_to_downstream = self.generate_reverse_graph(self.dag_pointing_to_upstream)

    def generate_reverse_graph(self, graph):
        """
        Generate the edge-reversed version of input directed graph
        :param graph: a directed graph
        :return: the edge-reversed version of input directed graph
        """
        answer = {}

        for parent, children in graph:
            for child in children:
                if child not in answer:
                    answer[child] = []
                answer[child].append(parent)
        return answer

    def dag_sanity_check(self):
        """
        dag structure sanity check:
            the dag should not contain cycles
            the dag should be connected, no islands allowed
        :return:
        """
        good_graph = True # note: use exception

        if Graph.has_cycles(graph=self.dag_pointing_to_upstream) or \
                Graph.has_cycles(graph=self.dag_pointing_to_downstream):
            good_graph = False
        if not Graph.is_connected(graph=self.dag_pointing_to_upstream) or \
            not Graph.is_connected(graph=self.dag_pointing_to_downstream):
            good_graph = False

        if not good_graph:
            print("DAG doesn't pass sanity check, please check your dag definition")

import uuid

class EtlJob:
    def __init__(self, param_bag=None):
        """
        Definition of a input->processing->output processing job

        :param param_bag: a dictionary storing all arguments

        fields:
        job_uuid: job's UUID (self generated)
        job_name: job's name (referred to by other jobs)
        upstream_file_table: the upstream folder locations
        downstream_file_table: the downstream folder locations
        trigger_type: trigger by dependency or by clock
        depend_on: the list of jobs that needs to be done before this job can start
        action: the action performed by this job, usually consumes the input and output locations
        copy_stream: whether to copy the output stream at stage
        """
        self.job_uuid = str(uuid.uuid4())
        self.status = "not started" # not started, running, failed, success

        if param_bag:
            if "job_name" in param_bag: self.job_name = param_bag["job_name"]
            if "upstream_file_table" in param_bag: self.upstream_file_table = param_bag["upstream_file_table"]
            if "downstream_file_table" in param_bag: self.downstream_file_table = param_bag["downstream_file_table"]
            if "trigger_type" in param_bag: self.trigger_type = param_bag["trigger_type"]
            if "depend_on" in param_bag: self.depend_on = param_bag["depend_on"]
            if "action" in param_bag: self.action = param_bag["action"]
            if "copy_stream" in param_bag: self.copy_stream = param_bag["copy_stream"] # should be user input
