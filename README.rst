k8s_deploy_tasks plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

tutor plugin to manage deployment tasks that are exclusively (or mostly) specific to Kubernetes deployments.


- *oauth misconfiguration*. tutor relies on an environment variable `ENABLE_HTTPS` to determine the protocol of the production oauth client for applications that rely on the LMS oauth service. For Kubernetes installations however, this value needs to be set to `false` which results in ./manage.py lms create_dot_application misconfiguring the oauth client. This plugin reconfigures the oauth clients of cms, discovery, ecommerce and credentials to use `https` protocol for redirect URI.
- *Nutmeg upgrade and initializataion tasks* There are a few manage.py tasks that need to run for platforms that are upgrading to Nutmeg or newer from Maple or older. This plugin runs those tasks for you. For more information see `Open edX Nutmeg Release <https://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/nutmeg.html>`_

Installation
------------

::

    pip install git+https://github.com/myusername/tutor-contrib-k8s-deploy-tasks

Usage
-----

::

    tutor plugins enable k8s_deploy_tasks


License
-------

This software is licensed under the terms of the AGPLv3.