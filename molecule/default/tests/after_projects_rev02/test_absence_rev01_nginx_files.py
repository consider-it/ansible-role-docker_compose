def test_files(host):
    html_sites_dir = host.file("/ansible_docker_compose/projects/nginx/html_sites")
    assert html_sites_dir.exists == False

    index_html_file = host.file("/ansible_docker_compose/projects/nginx/html_sites/index.html")
    assert index_html_file.exists == False
