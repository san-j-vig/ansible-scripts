import os
import pathlib

curr_file_path = str(pathlib.Path(__file__).parent.absolute()) + "/playbooks"

def generate_playbook_yaml(playbook):
    file_path = f"{curr_file_path}/{playbook}/playbook.yml"
    file_content = f"\
- hosts: 'all'\n\
  gather_facts: False\n\
  tasks:\n\
    - copy:\n\
        src: ./resources/\n\
        dest: /tmp/{playbook}\n\
        owner: ansible\n\
        group: ansible\n\
        mode: 0600\n\
    - name: My Task\n\
      become: true\n\
      become_user: root\n\
      script: ./scripts/{playbook}.sh\n\
      register: {playbook}\n\
    - debug: msg='{{ {playbook}.stdout }}'\n\
    - debug: msg='{{ {playbook}.stderr }}'\n\
"
    with open(file_path, mode="w") as fs:
        fs.write(file_content)
        fs.close()

    print("Playbook yaml file generated")


def generate_run_script(playbook):
    file_path = f"{curr_file_path}/{playbook}/run.sh"
    file_content = "\
#!/bin/bash\n\
\n\
playbook_yaml_file = \"playbook.yml\"\n\
read -p \"Enter hosts file path: \" hosts\n\
if [[ -z $hosts ]]; then\n\
    printf \"Please enter a valid hosts file path\"\n\
else\n\
    printf \"Using host file: $hosts\"\n\
    ansible-playbook $playbook_yaml_file -i $hosts\n\
fi\n\
printf \"Execution Complete\"\n\
"
    with open(file_path, mode="w") as fs:
        fs.write(file_content)
        fs.close()

    print("Run script file generated")


def generate_playbook_script(playbook):
    file_path = f"{curr_file_path}/{playbook}/scripts/{playbook}.sh"
    with open(file_path, mode="w") as fs:
        fs.write("")
        fs.close()

    print("Playbook script file generated")


def create_files_and_directories(playbook):
    os.mkdir(f"{curr_file_path}/{playbook}")
    os.mkdir(f"{curr_file_path}/{playbook}/scripts")
    os.mkdir(f"{curr_file_path}/{playbook}/resources")


def main(playbook):
    print(curr_file_path)
    create_files_and_directories(playbook)
    generate_playbook_script(playbook)
    generate_playbook_yaml(playbook)
    generate_run_script(playbook)


if __name__ == "__main__":
    # print(curr_file_path)
    playbook = input("Please enter a new playbook name: ")
    main(playbook)
