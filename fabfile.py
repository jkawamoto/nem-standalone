# pylint: skip-file
#
# fabfile.py
#
# Copyright (c) 2015-2016 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
from fabric.api import *
from fabric.contrib.project import rsync_project
env.use_ssh_config = True

PACKAGE = "nem-standalone"

@task
def build():
    """ Build a Docker image.
    """
    run("mkdir -p " + PACKAGE)
    rsync_project(
        local_dir=".", remote_dir=PACKAGE, exclude=['.git', "ncc", "nis", "client"])
    with cd(PACKAGE):
        run("docker build -t jkawamoto/{0} .".format(PACKAGE))


@task
def up():
    """Up docker compose.
    """
    with cd(PACKAGE):
        run("docker-compose up -d")


@task
def up():
    """down docker compose.
    """
    with cd(PACKAGE):
        run("docker-compose down")


@task
def logs():
    """Get docker compose logs.
    """
    with cd(PACKAGE):
        run("docker-compose logs")
