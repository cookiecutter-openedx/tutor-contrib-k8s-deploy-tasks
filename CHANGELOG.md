## [18.0.1](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/compare/v18.0.0...v18.0.1) (2024-11-18)


### Bug Fixes

* don't override the entire mfe_config dict. instead, only set individual keys. ([46072cc](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/commit/46072cceff867e592694d53d7c7cf0b1fd2dbce5))
* update individual MFE_CONFIG keys instead of rewriting the entire dict. ([9e7d1ff](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/commit/9e7d1ff856d83a98ea33d1f7e8db727edd3059e1))

## [17.0.7](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/compare/v17.0.6...v17.0.7) (2024-11-18)


### Bug Fixes

* don't override the entire mfe_config dict. instead, only set individual keys. ([46072cc](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/commit/46072cceff867e592694d53d7c7cf0b1fd2dbce5))

# CHANGE LOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [18.0.3](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/compare/v18.0.1...v18.0.3) (2025-6-26)

fix: avoid error when MFE plugin is disabled


## [18.0.1] (2024-4-8)

fix: update individual MFE_CONFIG keys instead of rewriting the entire dict.

### Bug Fixes
## [17.0.7] (2024-11-18)

- fix: don't override the entire mfe_config dict. instead, only set individual keys.

## [17.0.6] (2024-4-8)

### Bug Fixes

* (4_0.E001) As of Django 4.0, the values in the CSRF_TRUSTED_ORIGINS setting must start with ([cca2947](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/commit/cca294747ee5ba2f1344ddb0c65e73ae7ce6f429))


## [17.0.1](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/compare/v17.0.0...v17.0.1) (2024-01-03)

### Bug Fixes

* refactor MFE settings for Palm ([0923d14](https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/commit/0923d148493c371446dcce09ef7945e9e12365ca))

## [18.0.0] (2024-09-26)

- chore: bump to Redwood v18

## [15.0.3] (2023-08-14)

- chore: add cdn host to CORS_ORIGIN_WHITELIST and CSRF_TRUSTED_ORIGINS

## [15.0.2] (2023-08-14)

- propagate lms custom settings to cms

## [15.0.1] (2023-5-18)

- add missing CORS_ORIGIN_WHITELIST hosts
