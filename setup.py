from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    "boto3",
    "semver",
]

TESTS_REQUIRE = [
    "pytest",
    "pytest-mock",
    "pytest-xdist",
    "autoflake",
    "pre-commit",
]

EXTRAS_REQUIRE = {
    "tests": TESTS_REQUIRE,
}

setup(
    name="docker-wizard",
    version="0.0.1.dev",
    description=("A tool that follows semver to automate new releases of docker images."),
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sagemaker",
    packages=find_packages("docker_wizard"),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "docker-wizard = docker_wizard.main:main",
        ]
    },
)
