# Docker Compose Project Directory Revisions Forming Progression for Testing

This directory contains three revisions of a docker compose projects directory forming a progression for testing.
So in a testing flow one would deploy `projects_rev01` to -`03` one after another and test after each deployment if everything is as expected.

## Revision Changes Graph

Here's a graph visualizing which projects get added, removed, modified or stay the same from each revision to the next:

```
[projects_rev01] -> [projects_rev02] -> [projects_rev03]
|                   |                   |
|-- mosquitto       |-- mosquitto (mod.)|
+-- nginx           |-- nginx (mod.)    |-- nginx
                    +-- nodejs          |-- nodejs (mod.)
                                        +-- redis
```

## Project Descriptions

- `projects_rev01/mosquitto`: Just simply running Mosquitto.
- `projects_rev02/mosquitto`: Basically same as `projects_rev01/mosquitto`, but some file permission changes compared to it 

- `projects_rev01/nginx`: Simply running NGINX and giving it an HTML site to serve.
- `projects_rev02/nginx`: Custom built nginx image, which adds custom configs and HTML during the container build.
- `projects_rev03/nginx`: Same as `projects_rev02/nginx`.

- `projects_rev02/nodejs`: Custom build nodejs image, which contains a simple nodejs application returning a plaintext string.
  The nodejs application uses CommonJS modules.
- `projects_rev03/nodejs`: Custom build nodejs image, which contains a simple nodejs application returning a some JSON.
  The nodejs application uses ECMAScript modules.

- `projects_rev03/redis`: Just simply running Redis.
