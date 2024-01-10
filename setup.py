import io
import os
from setuptools import setup, find_namespace_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(os.path.join(HERE, "tutork8s_deploy_tasks", "__about__.py"), "rt", encoding="utf-8") as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()

setup(
    name="tutor-contrib-k8s-deploy-tasks",
    version=ABOUT["__version__"],
    url="https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks",
    project_urls={
        "Code": "https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks",
        "Issue tracker": "https://github.com/cookiecutter-openedx/tutor-contrib-k8s-deploy-tasks/issues",
        "Community": "https://github.com/cookiecutter-openedx",
    },
    license="AGPLv3",
    author="Lawrence McDaniel",
    maintainer="Lawrence McDaniel",
    maintainer_email="lpm0073@gmail.com",
    description="A Tutor plugin to manage deployment tasks that are exclusively (or mostly) specific to Kubernetes deployments",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_namespace_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=16.0.0,<17.0.0"],
    entry_points={"tutor.plugin.v1": ["k8s_deploy_tasks = tutork8s_deploy_tasks.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
