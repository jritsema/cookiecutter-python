import os
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def post_gen_project():

    if "{{ cookiecutter.container_support }}" != "True":
        remove_file("Dockerfile")
        remove_file(".dockerignore")

    if "{{ cookiecutter.enable_asdf }}" == "True":

        # write python version to .tool-versions
        python_version = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}"
        lines = [f"python {python_version}\n"]

        if "{{ cookiecutter.enable_direnv }}" == "True":
            lines.append("direnv 2.28.0\n")

        with open(".tool-versions", "w") as f:
            f.writelines(lines)

    if "{{ cookiecutter.enable_direnv }}" == "True":
        print("direnv allow .")
        os.system("direnv allow .")
    else:
        remove_file(".envrc")

    if "{{ cookiecutter.enable_aws }}" == "True":
        with open("requirements.txt", "w") as f:
            f.write(f"boto3")

    print("Creating virtual python environment...")
    os.system("python -m venv .venv")

    # create git repo
    os.system("git init && git add . && git commit -m 'initial'")

    print("Done")
    out = f"cd {{ cookiecutter.project_slug }}"
    if "{{ cookiecutter.enable_direnv }}" != "True":
        out += " && . .venv/bin/activate"
    if "{{ cookiecutter.enable_aws }}" == "True":
        out += " && make install"
    print(out)


if __name__ == "__main__":
    post_gen_project()
