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

    html_sites_dir = host.file("/ansible_docker_compose/projects/nginx/html_sites")
    assert html_sites_dir.is_directory == True
    assert html_sites_dir.user == "root"
    assert html_sites_dir.group == "root"
    assert html_sites_dir.mode == 0o755

    index_html_file = host.file("/ansible_docker_compose/projects/nginx/html_sites/index.html")
    assert index_html_file.is_file == True
    assert index_html_file.user == "root"
    assert index_html_file.group == "root"
    assert index_html_file.mode == 0o644

def test_endpoints(host):
    assert host.run("curl localhost:8080").stdout == """<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width"/>
        <title>nginx Docker Compose Project Rev 01</title>
    </head>
    <body>
        <p>nginx Docker Compose Project Rev 01</p>
    </body>
</html>
"""
