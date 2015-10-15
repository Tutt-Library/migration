__author__ = "Jeremy Nelson"
import click
import requests
import xml.etree.ElementTree as etree

etree.register_namespace("", "http://www.loc.gov/mods/v3")
REST_URL = "https://digitalcc.coloradocollege.edu/islandora/rest/v1/object"

# Force MODS to use display mods as a namespace
etree.register_namespace("", "http://www.loc.gov/mods/v3")

@click.command()
@click.option('--pid')
@click.option('--username', prompt='Username')
@click.option('--password', prompt='Password')
def remove_mods_namespace(pid, username, password):
    """Function retrieves MODS datastream, if namespaces are being
    used, replaces with MODS xml without the MODS namespace.

    Args:
       pid -- PID to update MODS

    Returns:
       boolean -- True if successful, False otherwise
    """
    AUTH = (username, password)
    get_mods_url = "{}/{}/datastream/MODS?content=true".format(
        REST_URL,
        pid)
    mods_result = requests.get(
        get_mods_url,
        auth=AUTH)
    if mods_result.status_code < 400:
        mods_xml = etree.XML(mods_result.text)
        put_mods_url = "{}/{}/datastream/MODS".format(
            REST_URL,
            pid)
        put_result = requests.put(
            put_mods_url,
            data={"content": etree.tostring(mods_xml)},
            auth=AUTH)
        if put_result.status_code == 201:
            return True
    return False

        
if __name__ == '__main__':
    remove_mods_namespace()
    
