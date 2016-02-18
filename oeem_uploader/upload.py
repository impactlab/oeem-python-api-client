from concurrent.futures import ThreadPoolExecutor 

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
    """NAME"""
    pass



def upload_projects(records):
    """
    Takes in a list of projects,
    uploads them to the configured datastore. 
    """
    pass

    ### functionalize and map this rather than for loop 
    for record in records: 
        record.upload()
        if status == 200
            good. 
        elif status == 422|409: 
            attempt_update_project(record)
        else: 
            "LOG server or other error"

def attempt_update_project(project):
    """
    Takes a project and attempts an UPDATE
    """
    get_project_from_server 
    if projects == same():
        log(already online)
    else:
        if should_i_update():
            project.update()

def should_project_update(project):
    """
    Returns True/False if a project should
    HTTP update or not. 
    """
    pass
