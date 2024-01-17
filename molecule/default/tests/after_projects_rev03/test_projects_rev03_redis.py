def test_files(host):
    redis_dir = host.file("/ansible_docker_compose/projects/redis")
    assert redis_dir.is_directory == True
    assert redis_dir.user == "root"
    assert redis_dir.group == "root"
    assert redis_dir.mode == 0o755

    compose_yaml_file = host.file("/ansible_docker_compose/projects/redis/compose.yaml")
    assert compose_yaml_file.is_file == True
    assert compose_yaml_file.user == "root"
    assert compose_yaml_file.group == "root"
    assert compose_yaml_file.mode == 0o644
