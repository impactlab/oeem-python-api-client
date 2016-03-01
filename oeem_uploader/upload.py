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

def upload_projects(records):
    """
    Takes in a list of projects,
    uploads them to the configured datastore.
    """
    ### functionalize and map this rather than for loop
    request = Request()
    for record in records:
        r = get_or_create_project(record)
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


def get_or_create(item_name, extra_info, get_url, create_url, data):


    response = Request.get(get_url)

    if response.status_code != 200:
        message = "GET error ({}): {}\n{}".format(
                response.status_code, get_url, response.text)
        raise ValueError(message)

    pks = [item["id"] for item in response.json()]

    if pks == []:
        response = Request.post(create_url,
                                data)

        if response.status_code != 201:
            message = "Create POST error ({}): {}\n{}\n{}".format(
                    response.status_code, create_url, data, response.text)
            raise ValueError(message)

        pk = response.json()["id"]

        if verbose:
            print("Created {} ({}, pk={})".format(item_name, extra_info, pk))

        return pk, True
    else:
        pk = pks[0]

        if len(pks) > 1:
            message = (
                "Found multiple {} instances ({}) for {}; using pk={}"
                .format(item_name, pks, extra_info, pk)
            )
            warnings.warn(message)

        if verbose:
            print("Existing {} ({}, pk={})".format(item_name, extra_info, pk))

        return pk, False

def get_or_create_project(project_id, project_owner_id,
        baseline_period_start, baseline_period_end,
        reporting_period_start, reporting_period_end,
        latitude, longitude, zipcode, weather_station, url, token, verify=True):

    get_url = url + PROJECT_URL + "?project_id={}".format(project_id)
    create_url = url + PROJECT_URL

    data = {
        "project_id": project_id,
        "project_owner": project_owner_id,
        "baseline_period_start": baseline_period_start,
        "baseline_period_end": baseline_period_end,
        "reporting_period_start": reporting_period_start,
        "reporting_period_end": reporting_period_end,
        "latitude": latitude,
        "longitude": longitude,
        "zipcode": zipcode,
        "weather_station": weather_station,
    }


    return get_or_create("Project", project_id, get_url, create_url, data,
            token, verify=True, verbose=True)

