from setuptools import setup

setup(
    name="project-b",
    version="1.2.0",
    description="Date, string, file and logging utilities",
    author="Not Important",
    packages=[],
    py_modules=[
        "date_utils",
        "string_utils",
        "file_utils",
        "logger_utils",
    ],
    package_dir={"": "src"},
    python_requires=">=3.11",
)
