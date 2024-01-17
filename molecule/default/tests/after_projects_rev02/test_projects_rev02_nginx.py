def test_files(host):
    nginx_dir = host.file("/ansible_docker_compose/projects/nginx")
    assert nginx_dir.is_directory == True
    assert nginx_dir.user == "root"
    assert nginx_dir.group == "root"
    assert nginx_dir.mode == 0o755

    compose_yaml_file = host.file("/ansible_docker_compose/projects/nginx/compose.yaml")
    assert compose_yaml_file.is_file == True
    assert compose_yaml_file.user == "root"
    assert compose_yaml_file.group == "root"
    assert compose_yaml_file.mode == 0o644

    build_dir = host.file("/ansible_docker_compose/projects/nginx/build")
    assert build_dir.is_directory == True
    assert build_dir.user == "root"
    assert build_dir.group == "root"
    assert build_dir.mode == 0o755

    nginx_conf_file = host.file("/ansible_docker_compose/projects/nginx/build/nginx.conf")
    assert nginx_conf_file.is_file == True
    assert nginx_conf_file.user == "root"
    assert nginx_conf_file.group == "root"
    assert nginx_conf_file.mode == 0o644

    nginx_Containerfile_file = host.file("/ansible_docker_compose/projects/nginx/build/nginx.Containerfile")
    assert nginx_Containerfile_file.is_file == True
    assert nginx_Containerfile_file.user == "root"
    assert nginx_Containerfile_file.group == "root"
    assert nginx_Containerfile_file.mode == 0o644

    conf_d_dir = host.file("/ansible_docker_compose/projects/nginx/build/conf.d")
    assert conf_d_dir.is_directory == True
    assert conf_d_dir.user == "root"
    assert conf_d_dir.group == "root"
    assert conf_d_dir.mode == 0o755

    default_conf_file = host.file("/ansible_docker_compose/projects/nginx/build/conf.d/default.conf")
    assert default_conf_file.is_file == True
    assert default_conf_file.user == "root"
    assert default_conf_file.group == "root"
    assert default_conf_file.mode == 0o644

    port_81_conf_file = host.file("/ansible_docker_compose/projects/nginx/build/conf.d/port_81.conf")
    assert port_81_conf_file.is_file == True
    assert port_81_conf_file.user == "root"
    assert port_81_conf_file.group == "root"
    assert port_81_conf_file.mode == 0o644

    html_dir = host.file("/ansible_docker_compose/projects/nginx/build/html")
    assert html_dir.is_directory == True
    assert html_dir.user == "root"
    assert html_dir.group == "root"
    assert html_dir.mode == 0o755

    index_html_file = host.file("/ansible_docker_compose/projects/nginx/build/html/index.html")
    assert index_html_file.is_file == True
    assert index_html_file.user == "root"
    assert index_html_file.group == "root"
    assert index_html_file.mode == 0o644

def test_endpoints(host):
    assert host.run("curl localhost:8080").stdout == '{"port": 80, "project": "nginx Docker Compose Project Rev 02"}'
    assert host.run("curl localhost:8081").stdout == '{"port": 81, "project": "nginx Docker Compose Project Rev 02"}'
    assert host.run("curl localhost:8082").stdout == """<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width"/>
        <title>Port 82: nginx Docker Compose Project Rev 02</title>
    </head>
    <body>
        <p>Port 82: nginx Docker Compose Project Rev 02</p>
    </body>
</html>
"""
