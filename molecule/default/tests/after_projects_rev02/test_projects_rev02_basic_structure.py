def test_basic_directory_structure(host):
    projects_dir = host.file("/ansible_docker_compose/projects")
    assert sorted(projects_dir.listdir()) == ["mosquitto", "nginx", "nodejs"]

def test_containers(host):
    len(host.docker.get_containers()) == 3
    host.docker("nodejs-node-1").is_running == True
    host.docker("nginx-nginx-1").is_running == True
    host.docker("mosquitto-mosquitto-1").is_running == True
