import logging
import subprocess

from .. import constants

logger = logging.getLogger('davy')


def set_up_new_ftb_server(server_name, installer_zip_url):
    server_folder = constants.SERVER_DIRECTORY + server_name
    server_zip = server_folder + "server.zip"
    logger.debug('Starting to launch server.')
    subprocess.call(['mkdir', server_folder])
    subprocess.call(['wget', installer_zip_url, server_folder + "server.zip"])
    subprocess.call(['unzip', server_zip])
    subprocess.call(['chmod', '777', server_folder + 'FTBInstall.sh', server_folder + 'ServerStart.sh'])
    subprocess.call(['rm', server_folder + "eula.txt"])
    subprocess.call(['touch', server_folder + "eula.txt"])
    subprocess.call(['echo', 'eula=true', ">>", server_folder + "eula.txt"])


def start_ftb_server(server_name):
    server_folder = constants.SERVER_DIRECTORY + server_name
    subprocess.call(['/bin/bash', server_folder + 'ServerStart.sh'])
