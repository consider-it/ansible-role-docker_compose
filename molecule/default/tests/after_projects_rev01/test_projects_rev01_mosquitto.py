def test_files(host):
    mosquitto_dir = host.file("/ansible_docker_compose/projects/mosquitto")
    assert mosquitto_dir.is_directory == True
    assert mosquitto_dir.user == "root"
    assert mosquitto_dir.group == "root"
    assert mosquitto_dir.mode == 0o755

    compose_yaml_file = host.file("/ansible_docker_compose/projects/mosquitto/compose.yaml")
    assert compose_yaml_file.is_file == True
    assert compose_yaml_file.user == "root"
    assert compose_yaml_file.group == "root"
    assert compose_yaml_file.mode == 0o644
