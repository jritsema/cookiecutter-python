import logging
from log import debug, info, warn, error

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("{{ cookiecutter.project_name }}")
    info({"project_name": "{{ cookiecutter.project_name }}"})


if __name__ == "__main__":
    main()
