#from concurrent.futures import ThreadPoolExecutor
from oeem_uploader.request import Request

from eemeter.location import Location
from eemeter.evaluation import Period
from eemeter.consumption import ConsumptionData
from eemeter.project import Project

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

def create_eemeter_project(project_row, consumption_data_rows):
    """
    Given a row a pd.DataFrame for projects
    and a set of rows for consumption data rows, 
    return eemeter project. 
    """
    location = Location( zipcode=project_row.zipcode,
            lat_lng=(project_row.latitude, project_row.longitude),
            station=project_row.weather_station)
    baseline_period = Period(project_row.baseline_period_start, project_row.baseline_period_end)
    reporting_period = Period(project_row.reporting_period_start, project_row.reporting_period_end)
    consumptions = _create_eemeter_consumptions(consumption_data_rows)
    project = Project(location, consumptions, baseline_period, reporting_period)

    return project

def _create_eemeter_consumptions(consumption_data_rows):
    """
    from consumption data rows create eemeter objects
    """
    natural_gas_records = [{"start": row.start, "end": row.end, "value": row.value}
            for _, row in consumption_data_rows[consumption_data_rows.fuel_type == "natural_gas"].iterrows()]
    electricity_records = [{"start": row.start, "end": row.end, "value": row.value}
            for _, row in consumption_data_rows[consumption_data_rows.fuel_type == "electricity"].iterrows()]
    consumption = []
    if len(natural_gas_records) > 0:
        cd_g = ConsumptionData(natural_gas_records, "natural_gas", "therm", record_type="arbitrary")
        consumption.append(cd_g)
    if len(electricity_records) > 0:
        cd_e = ConsumptionData(electricity_records, "electricity", "kWh", record_type="arbitrary")
        consumption.append(cd_e)
    return consumption

