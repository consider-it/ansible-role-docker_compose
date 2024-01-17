def test_files(host):
    nodejs_dir = host.file("/ansible_docker_compose/projects/nodejs")
    assert nodejs_dir.is_directory == True
    assert nodejs_dir.user == "root"
    assert nodejs_dir.group == "root"
    assert nodejs_dir.mode == 0o755

    compose_yaml_file = host.file("/ansible_docker_compose/projects/nodejs/compose.yaml")
    assert compose_yaml_file.is_file == True
    assert compose_yaml_file.user == "root"
    assert compose_yaml_file.group == "root"
    assert compose_yaml_file.mode == 0o644

    Dockerfile_file = host.file("/ansible_docker_compose/projects/nodejs/Dockerfile")
    assert Dockerfile_file.is_file == True
    assert Dockerfile_file.user == "root"
    assert Dockerfile_file.group == "root"
    assert Dockerfile_file.mode == 0o644

    app_dir = host.file("/ansible_docker_compose/projects/nodejs/app")
    assert app_dir.is_directory == True
    assert app_dir.user == "root"
    assert app_dir.group == "root"
    assert app_dir.mode == 0o755

    main_mjs_file = host.file("/ansible_docker_compose/projects/nodejs/app/main.mjs")
    assert main_mjs_file.is_file == True
    assert main_mjs_file.user == "root"
    assert main_mjs_file.group == "root"
    assert main_mjs_file.mode == 0o644

def test_endpoints(host):
    assert host.run("curl localhost:3000").stdout == '{"rev":2,"project":"nodejs","meta":"Docker Compose Project"}'
