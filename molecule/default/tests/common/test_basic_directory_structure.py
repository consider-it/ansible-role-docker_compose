def test_basic_directory_structure(host):
    ansible_docker_compose_dir = host.file("/ansible_docker_compose")
    assert ansible_docker_compose_dir.is_directory == True
    assert ansible_docker_compose_dir.user == "root"
    assert ansible_docker_compose_dir.group == "root"
    assert ansible_docker_compose_dir.mode == 0o755

    projects_dir = host.file("/ansible_docker_compose/projects")
    assert projects_dir.is_directory == True
    assert projects_dir.user == "root"
    assert projects_dir.group == "root"
    assert projects_dir.mode == 0o755

    project_data_dir = host.file("/ansible_docker_compose/project_data")
    assert project_data_dir.is_directory == True
    assert project_data_dir.user == "root"
    assert project_data_dir.group == "root"
    assert project_data_dir.mode == 0o755
