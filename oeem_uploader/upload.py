#from concurrent.futures import ThreadPoolExecutor
from oeem_uploader.request import Request

def upload_consumption(records):
    """
    Takes in a list of consumption records, uploads
    to the configured oee datastore.
    """
    group_records_by_project
    group_by_consumption_metadata
    #  Itertools group-by
    for project, fuel_type, records in groups:
        if projec_exists(project):
            metadata = get_or_create_metadata(fuel_type)
            response = post_consumption_records(project, metadata, records)
            process_response(response)

def process_response():
    pass


def upload_record(record, request):
    return request.post('projects', data=record)


def upload_projects(records):
    """
    Takes in a list of projects,
    uploads them to the configured datastore.
    """
    ### functionalize and map this rather than for loop
    request = Request()
    for record in records:
        r = upload_record(record, request)
        if r.status_code == 200:
            pass
        else:
            attempt_update_project(record)

def attempt_update_project(project):
    """
    Takes a project and attempts an UPDATE
    """
    get_project_from_server 
    if projects == same():
        pass 
        """log(already online)"""
    else:
        if should_i_update():
            project.update()

def should_project_update(project):
    """
    Returns True/False if a project should
    HTTP update or not. 
    """
    pass

