k8s_deploy_tasks plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

tutor plugin to manage deployment tasks that are exclusively (or mostly) specific to Kubernetes deployments.


- *oauth misconfiguration*. tutor relies on an environment variable `ENABLE_HTTPS` to determine the protocol of the production oauth client for applications that rely on the LMS oauth service. For Kubernetes installations however, this value needs to be set to `false` which results in ./manage.py lms create_dot_application misconfiguring the oauth client for some, but not all, of these oauth clients. This plugin reconfigures the oauth clients of cms, discovery, ecommerce and credentials to use `https` protocol for redirect URI.
- *Nutmeg upgrade and initializataion tasks* There are a few manage.py tasks that need to run for platforms that are upgrading to Nutmeg or newer from Maple or older. This plugin runs those tasks for you. For more information see `Open edX Nutmeg Release <https://edx.readthedocs.io/projects/open-edx-release-notes/en/latest/nutmeg.html>`_
- *Missing user profile records*. User accounts created with manage.py lack a corresponding auth_userprofile record, which causes a 500 exception during login for that account. Adds a blank record in cases where a record is missing.
- *MFE misconfiguration*. tutor-mfe relies on the value of ENABLE_HTTPS when generating the dict MFE_CONFIG, which in the case of k8s deployments will result in the browser blocking content due to "Mixed content". This plugin overrides the results of tutor-mfe openedx-lms-production-settings, replacing protocol produced by logic relying on ENABLE_HTTPS (assumed to result in 'http') with the hard-coded value 'https'.
- *Xblock storage configuration*. creates this `custom storage configuration <./tutork8s_deploy_tasks/patches/openedx-common-settings>`_ designed to leverage this `custom kubernetes ExternalService <https://github.com/lpm0073/cookiecutter-openedx-devops/blob/main/%7B%7Bcookiecutter.github_repo_name%7D%7D/terraform/environments/modules/kubernetes_ingress_clb/manifests/proxy-service.yml.tpl>`_ and `ingress <https://github.com/lpm0073/cookiecutter-openedx-devops/blob/main/%7B%7Bcookiecutter.github_repo_name%7D%7D/terraform/environments/modules/kubernetes_ingress_clb/manifests/ingress-scorm-proxy-service.yml.tpl>`_ created by Cookiecutter for supporting AWS S3 storage for Xblocks.

Installation
------------

::

    pip install tutor-contrib-k8s-deploy-tasks

Usage
-----

::

    tutor plugins enable k8s_deploy_tasks


License
-------

This software is licensed under the terms of the AGPLv3.