from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
    },
    # Add here settings that don't have a reasonable default for all users. For
    # instance: passwords, secret keys, etc.
    "unique": {
        # "SECRET_KEY": "\{\{ 24|random_string \}\}",
    },
    # Danger zone! Add here values to override settings from Tutor core or other plugins.
    "overrides": {
        # "PLATFORM_NAME": "My platform",
    },
}

################# Initialization tasks
hooks.Filters.COMMANDS_INIT.add_item((
     "lms",
     ("k8s_deploy_tasks", "tasks", "lms", "fix_oauth_redirect_uris"),
 ))
hooks.Filters.COMMANDS_INIT.add_item((
     "lms",
     ("k8s_deploy_tasks", "tasks", "lms", "nutmeg_deploy_tasks"),
 ))
hooks.Filters.COMMANDS_INIT.add_item((
     "cms",
     ("k8s_deploy_tasks", "tasks", "cms", "nutmeg_deploy_tasks"),
 ))
hooks.Filters.COMMANDS_INIT.add_item((
     "mysql",
     ("k8s_deploy_tasks", "tasks", "mysql", "add_user_profiles"),
 ))

################# Docker image management
# To build an image with `tutor images build myimage`, add a Dockerfile to templates/k8s_deploy_tasks/build/myimage and write:
# hooks.Filters.IMAGES_BUILD.add_item((
#     "myimage",
#     ("plugins", "k8s_deploy_tasks", "build", "myimage"),
#     "docker.io/myimage:\{\{ K8S_DEPLOY_TASKS_VERSION \}\}",
#     (),
# )
# To pull/push an image with `tutor images pull myimage` and `tutor images push myimage`, write:
# hooks.Filters.IMAGES_PULL.add_item((
#     "myimage",
#     "docker.io/myimage:\{\{ K8S_DEPLOY_TASKS_VERSION \}\}",
# )
# hooks.Filters.IMAGES_PUSH.add_item((
#     "myimage",
#     "docker.io/myimage:\{\{ K8S_DEPLOY_TASKS_VERSION \}\}",
# )


################# You don't really have to bother about what's below this line,
################# except maybe for educational purposes :)

# Plugin templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutork8s_deploy_tasks", "templates")
)
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("k8s_deploy_tasks/build", "plugins"),
        ("k8s_deploy_tasks/apps", "plugins"),
    ],
)
# Load all patches from the "patches" folder
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutork8s_deploy_tasks", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"K8S_DEPLOY_TASKS_{key}", value)
        for key, value in config["defaults"].items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"K8S_DEPLOY_TASKS_{key}", value)
        for key, value in config["unique"].items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))
