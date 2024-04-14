```sh
Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.

C:\Users\sofia>dir
 Volume in drive C is SYSTEM
 Volume Serial Number is 4A0A-36B0

 Directory of C:\Users\sofia

2022-04-17  23:52    <DIR>          .
2022-04-17  23:52    <DIR>          ..
2021-07-28  22:12             7 159 -1.14-windows.xml
2021-11-10  23:24    <DIR>          .android
2022-04-17  21:13    <DIR>          .aws
2022-04-17  21:13    <DIR>          .azure
2022-04-17  23:52    <DIR>          .config
2022-04-17  21:13    <DIR>          .docker
2021-02-08  13:43    <DIR>          .dotnet
2021-02-10  04:02                16 .emulator_console_auth_token
2021-02-10  14:00    <DIR>          .gradle
2021-02-07  15:21    <DIR>          .jdks
2021-08-25  17:56    <DIR>          .librarymanager
2021-02-07  03:23    <DIR>          .m2
2021-03-01  17:56    <DIR>          .templateengine
2021-11-07  14:05    <DIR>          .thumbnails
2022-04-17  23:43    <DIR>          .vscode
2021-02-10  03:58    <DIR>          3D Objects
2021-05-06  08:21    <DIR>          AndroidStudioProjects
2022-04-18  14:12    <DIR>          Calibre Library
2022-04-17  23:47    <DIR>          Code
2021-02-10  03:58    <DIR>          Contacts
2022-03-25  20:47    <DIR>          curseforge
2021-05-06  08:33    <DIR>          Desktop
2021-02-08  13:47    <DIR>          Documents
2022-04-18  16:16    <DIR>          Downloads
2021-02-10  03:58    <DIR>          Favorites
2021-02-07  15:21    <DIR>          IdeaProjects
2021-08-04  00:28            21 881 java_error_in_idea64_13632.log
2021-02-10  03:58    <DIR>          Links
2021-02-10  03:58    <DIR>          Music
2022-04-19  15:53    <DIR>          OneDrive
2022-04-17  11:00    <DIR>          Pictures
2021-12-08  17:33    <DIR>          Saved Games
2021-02-10  03:58    <DIR>          Searches
2021-02-08  15:45    <DIR>          source
2021-05-01  00:24                 0 Sti_Trace.log
2021-02-10  01:31    <DIR>          StudioProjects
2022-04-17  13:11    <DIR>          Videos
               4 File(s)         29 056 bytes
              35 Dir(s)  31 736 049 664 bytes free

C:\Users\sofia>cd desktop

C:\Users\sofia\Desktop>mkdir hello-docker

C:\Users\sofia\Desktop>cd hello-docker

C:\Users\sofia\Desktop\hello-docker>code .

C:\Users\sofia\Desktop\hello-docker>node app.js
Hello Docker!

C:\Users\sofia\Desktop\hello-docker>docker build -t  hello-docker .
[+] Building 10.6s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 99B                                                                                0.0s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/node:alpine                                                     3.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 165B                                                                                  0.0s
 => [1/3] FROM docker.io/library/node:alpine@sha256:f61706c2cb120c06cf4fdcf60a2822a804b0bd90b6b2209be1ee00db1d331  7.1s
 => => resolve docker.io/library/node:alpine@sha256:f61706c2cb120c06cf4fdcf60a2822a804b0bd90b6b2209be1ee00db1d331  0.0s
 => => sha256:e4c1ed79355cd19e255c26caf6a46734208a41d06fff16bdeb404cc988b7668a 1.16kB / 1.16kB                     0.0s
 => => sha256:ff748fa0ddfacab0ba165ba8ec7e57162298249326207d9f8a3af38a31de991c 6.58kB / 6.58kB                     0.0s
 => => sha256:df9b9388f04ad6279a7410b85cedfdcb2208c0a003da7ab5613af71079148139 2.81MB / 2.81MB                     0.4s
 => => sha256:b6fc737eaa4496a79bfb406d5be930bce84d86ea1f1d8108b85fe4cf50350c55 45.85MB / 45.85MB                   4.6s
 => => sha256:662377124a47035d2a2d3cee42fc8a01c780a21b7b99c7dca63b39d6752b3352 2.34MB / 2.34MB                     1.0s
 => => sha256:f61706c2cb120c06cf4fdcf60a2822a804b0bd90b6b2209be1ee00db1d33130c 1.43kB / 1.43kB                     0.0s
 => => extracting sha256:df9b9388f04ad6279a7410b85cedfdcb2208c0a003da7ab5613af71079148139                          0.3s
 => => sha256:3271f77c0e25c84f7b4169ce7a11b9e45626d21cccf7666fd6623bc7e4e7e43b 449B / 449B                         0.7s
 => => extracting sha256:b6fc737eaa4496a79bfb406d5be930bce84d86ea1f1d8108b85fe4cf50350c55                          2.0s
 => => extracting sha256:662377124a47035d2a2d3cee42fc8a01c780a21b7b99c7dca63b39d6752b3352                          0.1s
 => => extracting sha256:3271f77c0e25c84f7b4169ce7a11b9e45626d21cccf7666fd6623bc7e4e7e43b                          0.0s
 => [2/3] COPY . /app                                                                                              0.2s
 => [3/3] WORKDIR /app                                                                                             0.1s
 => exporting to image                                                                                             0.1s
 => => exporting layers                                                                                            0.1s
 => => writing image sha256:4c589f56b4541b4ed775ea49cdd29cf5f4ce82b8a2ca54839ad1e07e2e337dab                       0.0s
 => => naming to docker.io/library/hello-docker                                                                    0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

C:\Users\sofia\Desktop\hello-docker>docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
hello-docker   latest    4c589f56b454   29 seconds ago   168MB

C:\Users\sofia\Desktop\hello-docker>docker image ls
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
hello-docker   latest    4c589f56b454   42 seconds ago   168MB

C:\Users\sofia\Desktop\hello-docker>curl 172.17.0.3
curl: (28) Failed to connect to 172.17.0.3 port 80 after 21000 ms: Timed out

C:\Users\sofia\Desktop\hello-docker>

-----

Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.

C:\Users\sofia>d:

D:\>docker  run hello-docker
Hello Docker!

D:\>docker run ubunto
Unable to find image 'ubunto:latest' locally
docker: Error response from daemon: pull access denied for ubunto, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.

D:\> docker-compose --version
Docker Compose version v2.4.1

D:\>docker ?
docker: '?' is not a docker command.
See 'docker --help'

D:\>docker --help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "C:\\Users\\sofia\\.docker")
  -c, --context string     Name of the context to use to connect to the
                           daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "C:\\Users\\sofia\\.docker\\ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "C:\\Users\\sofia\\.docker\\cert.pem")
      --tlskey string      Path to TLS key file (default
                           "C:\\Users\\sofia\\.docker\\key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.8.2)
  compose*    Docker Compose (Docker Inc., v2.4.1)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
  scan*       Docker Scan (Docker Inc., v0.17.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/

D:\>docker cp help
"docker cp" requires exactly 2 arguments.
See 'docker cp --help'.

Usage:  docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
        docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

Copy files/folders between a container and the local filesystem

D:\>docker images
REPOSITORY     TAG       IMAGE ID       CREATED       SIZE
hello-docker   latest    4c589f56b454   2 hours ago   168MB

D:\>docker rm --help

Usage:  docker rm [OPTIONS] CONTAINER [CONTAINER...]

Remove one or more containers

Options:
  -f, --force     Force the removal of a running container (uses SIGKILL)
  -l, --link      Remove the specified link
  -v, --volumes   Remove anonymous volumes associated with the container

D:\>docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:10d7d58d5ebd2a652f4d93fdd86da8f265f5318c6a73cc5b6a9798ff6d2b2e67
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


D:\>docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
e0b25ef51634: Pull complete
Digest: sha256:9101220a875cee98b016668342c489ff0674f247f6ca20dfc91b91c0f28581ae
Status: Downloaded newer image for ubuntu:latest
root@2704a5a5fc44:/# ls -la
total 56
drwxr-xr-x   1 root root 4096 Apr 20 00:31 .
drwxr-xr-x   1 root root 4096 Apr 20 00:31 ..
-rwxr-xr-x   1 root root    0 Apr 20 00:31 .dockerenv
lrwxrwxrwx   1 root root    7 Apr  5 04:59 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr 20 00:31 dev
drwxr-xr-x   1 root root 4096 Apr 20 00:31 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Apr  5 04:59 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr  5 04:59 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Apr  5 04:59 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Apr  5 04:59 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Apr  5 04:59 media
drwxr-xr-x   2 root root 4096 Apr  5 04:59 mnt
drwxr-xr-x   2 root root 4096 Apr  5 04:59 opt
dr-xr-xr-x 233 root root    0 Apr 20 00:31 proc
drwx------   2 root root 4096 Apr  5 05:02 root
drwxr-xr-x   5 root root 4096 Apr  5 05:02 run
lrwxrwxrwx   1 root root    8 Apr  5 04:59 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Apr  5 04:59 srv
dr-xr-xr-x  11 root root    0 Apr 20 00:31 sys
drwxrwxrwt   2 root root 4096 Apr  5 05:02 tmp
drwxr-xr-x  13 root root 4096 Apr  5 04:59 usr
drwxr-xr-x  11 root root 4096 Apr  5 05:02 var
root@2704a5a5fc44:/# exit
exit

D:\>docker tun --help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "C:\\Users\\sofia\\.docker")
  -c, --context string     Name of the context to use to connect to the
                           daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "C:\\Users\\sofia\\.docker\\ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "C:\\Users\\sofia\\.docker\\cert.pem")
      --tlskey string      Path to TLS key file (default
                           "C:\\Users\\sofia\\.docker\\key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.8.2)
  compose*    Docker Compose (Docker Inc., v2.4.1)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
  scan*       Docker Scan (Docker Inc., v0.17.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/

D:\>docker run --help

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
      --add-host list                  Add a custom host-to-IP mapping
                                       (host:ip)
  -a, --attach list                    Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16            Block IO (relative weight),
                                       between 10 and 1000, or 0 to
                                       disable (default 0)
      --blkio-weight-device list       Block IO weight (relative device
                                       weight) (default [])
      --cap-add list                   Add Linux capabilities
      --cap-drop list                  Drop Linux capabilities
      --cgroup-parent string           Optional parent cgroup for the
                                       container
      --cgroupns string                Cgroup namespace to use
                                       (host|private)
                                       'host':    Run the container in
                                       the Docker host's cgroup namespace
                                       'private': Run the container in
                                       its own private cgroup namespace
                                       '':        Use the cgroup
                                       namespace as configured by the
                                                  default-cgroupns-mode
                                       option on the daemon (default)
      --cidfile string                 Write the container ID to the file
      --cpu-period int                 Limit CPU CFS (Completely Fair
                                       Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair
                                       Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in
                                       microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in
                                       microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution
                                       (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution
                                       (0-3, 0,1)
  -d, --detach                         Run container in background and
                                       print container ID
      --detach-keys string             Override the key sequence for
                                       detaching a container
      --device list                    Add a host device to the container
      --device-cgroup-rule list        Add a rule to the cgroup allowed
                                       devices list
      --device-read-bps list           Limit read rate (bytes per second)
                                       from a device (default [])
      --device-read-iops list          Limit read rate (IO per second)
                                       from a device (default [])
      --device-write-bps list          Limit write rate (bytes per
                                       second) to a device (default [])
      --device-write-iops list         Limit write rate (IO per second)
                                       to a device (default [])
      --disable-content-trust          Skip image verification (default true)
      --dns list                       Set custom DNS servers
      --dns-option list                Set DNS options
      --dns-search list                Set custom DNS search domains
      --domainname string              Container NIS domain name
      --entrypoint string              Overwrite the default ENTRYPOINT
                                       of the image
  -e, --env list                       Set environment variables
      --env-file list                  Read in a file of environment variables
      --expose list                    Expose a port or a range of ports
      --gpus gpu-request               GPU devices to add to the
                                       container ('all' to pass all GPUs)
      --group-add list                 Add additional groups to join
      --health-cmd string              Command to run to check health
      --health-interval duration       Time between running the check
                                       (ms|s|m|h) (default 0s)
      --health-retries int             Consecutive failures needed to
                                       report unhealthy
      --health-start-period duration   Start period for the container to
                                       initialize before starting
                                       health-retries countdown
                                       (ms|s|m|h) (default 0s)
      --health-timeout duration        Maximum time to allow one check to
                                       run (ms|s|m|h) (default 0s)
      --help                           Print usage
  -h, --hostname string                Container host name
      --init                           Run an init inside the container
                                       that forwards signals and reaps
                                       processes
  -i, --interactive                    Keep STDIN open even if not attached
      --ip string                      IPv4 address (e.g., 172.30.100.104)
      --ip6 string                     IPv6 address (e.g., 2001:db8::33)
      --ipc string                     IPC mode to use
      --isolation string               Container isolation technology
      --kernel-memory bytes            Kernel memory limit
  -l, --label list                     Set meta data on a container
      --label-file list                Read in a line delimited file of labels
      --link list                      Add link to another container
      --link-local-ip list             Container IPv4/IPv6 link-local
                                       addresses
      --log-driver string              Logging driver for the container
      --log-opt list                   Log driver options
      --mac-address string             Container MAC address (e.g.,
                                       92:d0:c6:0a:29:33)
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus
                                       swap: '-1' to enable unlimited swap
      --memory-swappiness int          Tune container memory swappiness
                                       (0 to 100) (default -1)
      --mount mount                    Attach a filesystem mount to the
                                       container
      --name string                    Assign a name to the container
      --network network                Connect a container to a network
      --network-alias list             Add network-scoped alias for the
                                       container
      --no-healthcheck                 Disable any container-specified
                                       HEALTHCHECK
      --oom-kill-disable               Disable OOM Killer
      --oom-score-adj int              Tune host's OOM preferences (-1000
                                       to 1000)
      --pid string                     PID namespace to use
      --pids-limit int                 Tune container pids limit (set -1
                                       for unlimited)
      --platform string                Set platform if server is
                                       multi-platform capable
      --privileged                     Give extended privileges to this
                                       container
  -p, --publish list                   Publish a container's port(s) to
                                       the host
  -P, --publish-all                    Publish all exposed ports to
                                       random ports
      --pull string                    Pull image before running
                                       ("always"|"missing"|"never")
                                       (default "missing")
      --read-only                      Mount the container's root
                                       filesystem as read only
      --restart string                 Restart policy to apply when a
                                       container exits (default "no")
      --rm                             Automatically remove the container
                                       when it exits
      --runtime string                 Runtime to use for this container
      --security-opt list              Security Options
      --shm-size bytes                 Size of /dev/shm
      --sig-proxy                      Proxy received signals to the
                                       process (default true)
      --stop-signal string             Signal to stop a container
                                       (default "15")
      --stop-timeout int               Timeout (in seconds) to stop a
                                       container
      --storage-opt list               Storage driver options for the
                                       container
      --sysctl map                     Sysctl options (default map[])
      --tmpfs list                     Mount a tmpfs directory
  -t, --tty                            Allocate a pseudo-TTY
      --ulimit ulimit                  Ulimit options (default [])
  -u, --user string                    Username or UID (format:
                                       <name|uid>[:<group|gid>])
      --userns string                  User namespace to use
      --uts string                     UTS namespace to use
  -v, --volume list                    Bind mount a volume
      --volume-driver string           Optional volume driver for the
                                       container
      --volumes-from list              Mount volumes from the specified
                                       container(s)
  -w, --workdir string                 Working directory inside the container

D:\>docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

D:\>docker ps --help

Usage:  docker ps [OPTIONS]

List containers

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all
                        states) (default -1)
  -l, --latest          Show the latest created container (includes all
                        states)
      --no-trunc        Don't truncate output
  -q, --quiet           Only display container IDs
  -s, --size            Display total file sizes

D:\>docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                     PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   4 minutes ago   Exited (0) 3 minutes ago             mystifying_johnson
88a1cdea06c6   hello-world    "/hello"                 5 minutes ago   Exited (0) 5 minutes ago             serene_satoshi
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   3 hours ago     Exited (0) 3 hours ago               pensive_burnell

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

D:\>docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                    PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   9 hours ago    Exited (0) 9 hours ago              mystifying_johnson
88a1cdea06c6   hello-world    "/hello"                 9 hours ago    Exited (0) 9 hours ago              serene_satoshi
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   11 hours ago   Exited (0) 11 hours ago             pensive_burnell

D:\>docker start mystifying_johnson
mystifying_johnson

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED       STATUS         PORTS     NAMES
2704a5a5fc44   ubuntu    "bash"    9 hours ago   Up 5 seconds             mystifying_johnson

D:\>docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                    PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   9 hours ago    Up 16 seconds                       mystifying_johnson
88a1cdea06c6   hello-world    "/hello"                 9 hours ago    Exited (0) 9 hours ago              serene_satoshi
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   12 hours ago   Exited (0) 12 hours ago             pensive_burnell

D:\>docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED       STATUS          PORTS     NAMES
2704a5a5fc44   ubuntu    "bash"    9 hours ago   Up 21 seconds             mystifying_johnson

D:\>docker exec mystifying_johnson ls -la
total 56
drwxr-xr-x   1 root root 4096 Apr 20 00:31 .
drwxr-xr-x   1 root root 4096 Apr 20 00:31 ..
-rwxr-xr-x   1 root root    0 Apr 20 00:31 .dockerenv
lrwxrwxrwx   1 root root    7 Apr  5 04:59 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr 20 09:15 dev
drwxr-xr-x   1 root root 4096 Apr 20 00:31 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Apr  5 04:59 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr  5 04:59 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Apr  5 04:59 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Apr  5 04:59 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Apr  5 04:59 media
drwxr-xr-x   2 root root 4096 Apr  5 04:59 mnt
drwxr-xr-x   2 root root 4096 Apr  5 04:59 opt
dr-xr-xr-x 226 root root    0 Apr 20 09:15 proc
drwx------   1 root root 4096 Apr 20 00:31 root
drwxr-xr-x   5 root root 4096 Apr  5 05:02 run
lrwxrwxrwx   1 root root    8 Apr  5 04:59 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Apr  5 04:59 srv
dr-xr-xr-x  11 root root    0 Apr 20 09:15 sys
drwxrwxrwt   2 root root 4096 Apr  5 05:02 tmp
drwxr-xr-x  13 root root 4096 Apr  5 04:59 usr
drwxr-xr-x  11 root root 4096 Apr  5 05:02 var

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED      STATUS      PORTS     NAMES
2704a5a5fc44   ubuntu    "bash"    4 days ago   Up 4 days             mystifying_johnson

D:\>docker stop mystifying_johnson
mystifying_johnson

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED      STATUS                     PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   4 days ago   Exited (0) 6 seconds ago             mystifying_johnson
88a1cdea06c6   hello-world    "/hello"                 4 days ago   Exited (0) 4 days ago                serene_satoshi
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   4 days ago   Exited (0) 4 days ago                pensive_burnell

D:\>docker rename mystifying_johnson ubuntu01

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED      STATUS                     PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   4 days ago   Exited (0) 3 minutes ago             ubuntu01
88a1cdea06c6   hello-world    "/hello"                 4 days ago   Exited (0) 4 days ago                serene_satoshi
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   4 days ago   Exited (0) 4 days ago                pensive_burnell

D:\>docker rename serene_satoshi hello_mine

D:\>docker rename pensive_burnell hello_ex

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED      STATUS                     PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   4 days ago   Exited (0) 4 minutes ago             ubuntu01
88a1cdea06c6   hello-world    "/hello"                 4 days ago   Exited (0) 4 days ago                hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   4 days ago   Exited (0) 4 days ago                hello_ex

D:\>docker stats
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
^C
D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED      STATUS                   PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   4 days ago   Exited (0) 7 hours ago             ubuntu01
88a1cdea06c6   hello-world    "/hello"                 4 days ago   Exited (0) 4 days ago              hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   5 days ago   Exited (0) 5 days ago              hello_ex

D:\>docker start ubunto01
Error response from daemon: No such container: ubunto01
Error: failed to start containers: ubunto01

D:\>docker start ubuntu01
ubuntu01

D:\> notepad index.html

D:\>docker run alpine
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
df9b9388f04a: Already exists
Digest: sha256:4edbd2beb5f78b1014028f4fbb99f3237d9561100b6881aabbf5acce2c4f9454
Status: Downloaded newer image for alpine:latest

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS     NAMES
9c15b5ad2417   alpine         "/bin/sh"                33 seconds ago   Exited (0) 33 seconds ago             gallant_pike
2704a5a5fc44   ubuntu         "bash"                   4 days ago       Up 6 minutes                          ubuntu01
88a1cdea06c6   hello-world    "/hello"                 4 days ago       Exited (0) 4 days ago                 hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   5 days ago       Exited (0) 5 days ago                 hello_ex

D:\>docker rename gallant_pike web01

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS     NAMES
9c15b5ad2417   alpine         "/bin/sh"                59 seconds ago   Exited (0) 59 seconds ago             web01
2704a5a5fc44   ubuntu         "bash"                   4 days ago       Up 7 minutes                          ubuntu01
88a1cdea06c6   hello-world    "/hello"                 4 days ago       Exited (0) 4 days ago                 hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   5 days ago       Exited (0) 5 days ago                 hello_ex

D:\>docker exec web01 apk add nginx
Error response from daemon: Container 9c15b5ad241772915e9bd1032f79f496740ed81c54291c729bb87ed36827fe09 is not running

D:\>docker start web01
web01

D:\>docker exec web01 apk add nginx
Error response from daemon: Container 9c15b5ad241772915e9bd1032f79f496740ed81c54291c729bb87ed36827fe09 is not running

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                      PORTS     NAMES
9c15b5ad2417   alpine         "/bin/sh"                34 hours ago   Exited (0) 19 seconds ago             web01
2704a5a5fc44   ubuntu         "bash"                   6 days ago     Up 34 hours                           ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago     Exited (0) 6 days ago                 hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago     Exited (0) 6 days ago                 hello_ex

D:\>docker start -d web01
unknown shorthand flag: 'd' in -d
See 'docker start --help'.

D:\>docker run -d web01
Unable to find image 'web01:latest' locally
docker: Error response from daemon: pull access denied for web01, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.

D:\>docker  start -?
unknown shorthand flag: '?' in -?
See 'docker start --help'.

D:\>docker  start --help

Usage:  docker start [OPTIONS] CONTAINER [CONTAINER...]

Start one or more stopped containers

Options:
  -a, --attach               Attach STDOUT/STDERR and forward signals
      --detach-keys string   Override the key sequence for detaching a
                             container
  -i, --interactive          Attach container's STDIN

D:\>docker  run --help

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
      --add-host list                  Add a custom host-to-IP mapping
                                       (host:ip)
  -a, --attach list                    Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16            Block IO (relative weight),
                                       between 10 and 1000, or 0 to
                                       disable (default 0)
      --blkio-weight-device list       Block IO weight (relative device
                                       weight) (default [])
      --cap-add list                   Add Linux capabilities
      --cap-drop list                  Drop Linux capabilities
      --cgroup-parent string           Optional parent cgroup for the
                                       container
      --cgroupns string                Cgroup namespace to use
                                       (host|private)
                                       'host':    Run the container in
                                       the Docker host's cgroup namespace
                                       'private': Run the container in
                                       its own private cgroup namespace
                                       '':        Use the cgroup
                                       namespace as configured by the
                                                  default-cgroupns-mode
                                       option on the daemon (default)
      --cidfile string                 Write the container ID to the file
      --cpu-period int                 Limit CPU CFS (Completely Fair
                                       Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair
                                       Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in
                                       microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in
                                       microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution
                                       (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution
                                       (0-3, 0,1)
  -d, --detach                         Run container in background and
                                       print container ID
      --detach-keys string             Override the key sequence for
                                       detaching a container
      --device list                    Add a host device to the container
      --device-cgroup-rule list        Add a rule to the cgroup allowed
                                       devices list
      --device-read-bps list           Limit read rate (bytes per second)
                                       from a device (default [])
      --device-read-iops list          Limit read rate (IO per second)
                                       from a device (default [])
      --device-write-bps list          Limit write rate (bytes per
                                       second) to a device (default [])
      --device-write-iops list         Limit write rate (IO per second)
                                       to a device (default [])
      --disable-content-trust          Skip image verification (default true)
      --dns list                       Set custom DNS servers
      --dns-option list                Set DNS options
      --dns-search list                Set custom DNS search domains
      --domainname string              Container NIS domain name
      --entrypoint string              Overwrite the default ENTRYPOINT
                                       of the image
  -e, --env list                       Set environment variables
      --env-file list                  Read in a file of environment variables
      --expose list                    Expose a port or a range of ports
      --gpus gpu-request               GPU devices to add to the
                                       container ('all' to pass all GPUs)
      --group-add list                 Add additional groups to join
      --health-cmd string              Command to run to check health
      --health-interval duration       Time between running the check
                                       (ms|s|m|h) (default 0s)
      --health-retries int             Consecutive failures needed to
                                       report unhealthy
      --health-start-period duration   Start period for the container to
                                       initialize before starting
                                       health-retries countdown
                                       (ms|s|m|h) (default 0s)
      --health-timeout duration        Maximum time to allow one check to
                                       run (ms|s|m|h) (default 0s)
      --help                           Print usage
  -h, --hostname string                Container host name
      --init                           Run an init inside the container
                                       that forwards signals and reaps
                                       processes
  -i, --interactive                    Keep STDIN open even if not attached
      --ip string                      IPv4 address (e.g., 172.30.100.104)
      --ip6 string                     IPv6 address (e.g., 2001:db8::33)
      --ipc string                     IPC mode to use
      --isolation string               Container isolation technology
      --kernel-memory bytes            Kernel memory limit
  -l, --label list                     Set meta data on a container
      --label-file list                Read in a line delimited file of labels
      --link list                      Add link to another container
      --link-local-ip list             Container IPv4/IPv6 link-local
                                       addresses
      --log-driver string              Logging driver for the container
      --log-opt list                   Log driver options
      --mac-address string             Container MAC address (e.g.,
                                       92:d0:c6:0a:29:33)
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus
                                       swap: '-1' to enable unlimited swap
      --memory-swappiness int          Tune container memory swappiness
                                       (0 to 100) (default -1)
      --mount mount                    Attach a filesystem mount to the
                                       container
      --name string                    Assign a name to the container
      --network network                Connect a container to a network
      --network-alias list             Add network-scoped alias for the
                                       container
      --no-healthcheck                 Disable any container-specified
                                       HEALTHCHECK
      --oom-kill-disable               Disable OOM Killer
      --oom-score-adj int              Tune host's OOM preferences (-1000
                                       to 1000)
      --pid string                     PID namespace to use
      --pids-limit int                 Tune container pids limit (set -1
                                       for unlimited)
      --platform string                Set platform if server is
                                       multi-platform capable
      --privileged                     Give extended privileges to this
                                       container
  -p, --publish list                   Publish a container's port(s) to
                                       the host
  -P, --publish-all                    Publish all exposed ports to
                                       random ports
      --pull string                    Pull image before running
                                       ("always"|"missing"|"never")
                                       (default "missing")
      --read-only                      Mount the container's root
                                       filesystem as read only
      --restart string                 Restart policy to apply when a
                                       container exits (default "no")
      --rm                             Automatically remove the container
                                       when it exits
      --runtime string                 Runtime to use for this container
      --security-opt list              Security Options
      --shm-size bytes                 Size of /dev/shm
      --sig-proxy                      Proxy received signals to the
                                       process (default true)
      --stop-signal string             Signal to stop a container
                                       (default "15")
      --stop-timeout int               Timeout (in seconds) to stop a
                                       container
      --storage-opt list               Storage driver options for the
                                       container
      --sysctl map                     Sysctl options (default map[])
      --tmpfs list                     Mount a tmpfs directory
  -t, --tty                            Allocate a pseudo-TTY
      --ulimit ulimit                  Ulimit options (default [])
  -u, --user string                    Username or UID (format:
                                       <name|uid>[:<group|gid>])
      --userns string                  User namespace to use
      --uts string                     UTS namespace to use
  -v, --volume list                    Bind mount a volume
      --volume-driver string           Optional volume driver for the
                                       container
      --volumes-from list              Mount volumes from the specified
                                       container(s)
  -w, --workdir string                 Working directory inside the container

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                      PORTS     NAMES
9c15b5ad2417   alpine         "/bin/sh"                35 hours ago   Exited (0) 21 minutes ago             web01
2704a5a5fc44   ubuntu         "bash"                   6 days ago     Up 35 hours                           ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago     Exited (0) 6 days ago                 hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago     Exited (0) 6 days ago                 hello_ex

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED      STATUS        PORTS     NAMES
2704a5a5fc44   ubuntu    "bash"    6 days ago   Up 35 hours             ubuntu01

D:\>docker --help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "C:\\Users\\sofia\\.docker")
  -c, --context string     Name of the context to use to connect to the
                           daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "C:\\Users\\sofia\\.docker\\ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "C:\\Users\\sofia\\.docker\\cert.pem")
      --tlskey string      Path to TLS key file (default
                           "C:\\Users\\sofia\\.docker\\key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.8.2)
  compose*    Docker Compose (Docker Inc., v2.4.1)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
  scan*       Docker Scan (Docker Inc., v0.17.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/

D:\>docker exec -it web01 ash
Error response from daemon: Container 9c15b5ad241772915e9bd1032f79f496740ed81c54291c729bb87ed36827fe09 is not running

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                      PORTS     NAMES
9c15b5ad2417   alpine         "/bin/sh"                35 hours ago   Exited (0) 25 minutes ago             web01
2704a5a5fc44   ubuntu         "bash"                   6 days ago     Up 35 hours                           ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago     Exited (0) 6 days ago                 hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago     Exited (0) 6 days ago                 hello_ex

D:\>docker  -rm web01
unknown shorthand flag: 'r' in -rm
See 'docker --help'.

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "C:\\Users\\sofia\\.docker")
  -c, --context string     Name of the context to use to connect to the
                           daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "C:\\Users\\sofia\\.docker\\ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "C:\\Users\\sofia\\.docker\\cert.pem")
      --tlskey string      Path to TLS key file (default
                           "C:\\Users\\sofia\\.docker\\key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.8.2)
  compose*    Docker Compose (Docker Inc., v2.4.1)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
  scan*       Docker Scan (Docker Inc., v0.17.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/


D:\>docker rm web01
web01

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED      STATUS                  PORTS     NAMES
2704a5a5fc44   ubuntu         "bash"                   6 days ago   Up 35 hours                       ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago   Exited (0) 6 days ago             hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago   Exited (0) 6 days ago             hello_ex

D:\>docker run -it --name web01 alpine
/ # ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ # exit

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                     PORTS     NAMES
96c305c6dfbd   alpine         "/bin/sh"                16 seconds ago   Exited (0) 3 seconds ago             web01
2704a5a5fc44   ubuntu         "bash"                   6 days ago       Up 35 hours                          ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago       Exited (0) 6 days ago                hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago       Exited (0) 6 days ago                hello_ex

D:\>dockker exec a-container apk add nginx
'dockker' is not recognized as an internal or external command,
operable program or batch file.

D:\>docker exec a-container apk add nginx
Error: No such container: a-container

D:\>docker exec web01 apk add nginx
Error response from daemon: Container 96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb is not running

D:\>docker start web01
web01

D:\>docker exec web01 apk add nginx
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/2) Installing pcre (8.45-r1)
(2/2) Installing nginx (1.20.2-r0)
Executing nginx-1.20.2-r0.pre-install
Executing nginx-1.20.2-r0.post-install
Executing busybox-1.34.1-r5.trigger
OK: 7 MiB in 16 packages

D:\>docker  cp web01:/etc/nginx/conf.d/default.conf .
Error: No such container:path: web01:/etc/nginx/conf.d/default.conf

D:\>docker cp web01:/etc/nginx/conf.d/default.conf .
Error: No such container:path: web01:/etc/nginx/conf.d/default.conf

D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                  PORTS     NAMES
96c305c6dfbd   alpine         "/bin/sh"                26 minutes ago   Up 24 minutes                     web01
2704a5a5fc44   ubuntu         "bash"                   6 days ago       Up 35 hours                       ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago       Exited (0) 6 days ago             hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago       Exited (0) 6 days ago             hello_ex

D:\>docker exec -it web01 ash
/ # ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ # ls /etc/nginx/
fastcgi.conf    fastcgi_params  http.d          mime.types      modules         nginx.conf      scgi_params     uwsgi_params
/ # ls /etc/nginx/conf.d/
ls: /etc/nginx/conf.d/: No such file or directory
/ # ls /etc/nginx/http.d/
default.conf
/ # exit

D:\>docker cp web01:/etc/nginx/http.d/default.conf .

D:\>notepad default.conf

D:\>docker cp default.conf web01:/etc/ngix/http.d/default.conf
Error: No such container:path: web01:\etc\ngix\http.d

D:\>docker cp default.conf web01:/etc/nginx/http.d/default.conf

D:\>docker exec web01 cat /etc/nginx/http.d/default.conf
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/;
}

D:\>docker stats
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O   PIDS
96c305c6dfbd   web01      0.00%     1.617MiB / 25.01GiB   0.01%     3.01MB / 49.3kB   0B / 0B     1
2704a5a5fc44   ubuntu01   0.00%     832KiB / 25.01GiB     0.00%     3.82kB / 0B       0B / 0B     1
^C
D:\>docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS                  PORTS     NAMES
96c305c6dfbd   alpine         "/bin/sh"                2 hours ago   Up 2 hours                        web01
2704a5a5fc44   ubuntu         "bash"                   6 days ago    Up 37 hours                       ubuntu01
88a1cdea06c6   hello-world    "/hello"                 6 days ago    Exited (0) 6 days ago             hello_mine
1268dfd2b867   hello-docker   "docker-entrypoint.s…"   6 days ago    Exited (0) 6 days ago             hello_ex

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND     CREATED       STATUS        PORTS     NAMES
96c305c6dfbd   alpine    "/bin/sh"   2 hours ago   Up 2 hours              web01
2704a5a5fc44   ubuntu    "bash"      6 days ago    Up 37 hours             ubuntu01

D:\>notepad index.html

D:\>docker cp index.html web01:/var/www/

D:\>docker exec web01 cat web01:/var/www/index.html
cat: can't open 'web01:/var/www/index.html': No such file or directory

D:\>docker exec web01 more web01:/var/www/index.html
more: can't open 'web01:/var/www/index.html': No such file or directory

D:\>docker exec web01 cat /var/www/index.html
Hello world!
D:\>docker exec -dt web01 nginx -g 'pid /tmp/nginx.pid; daemon off; &'
''' is not recognized as an internal or external command,
operable program or batch file.

D:\>docker exec -dt web01 nginx -g "pid /tmp/nginx.pid; daemon off; &"

D:\>docker inspect web01
[
    {
        "Id": "96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb",
        "Created": "2022-04-26T09:57:14.6992727Z",
        "Path": "/bin/sh",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 2247,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-04-26T09:59:21.3805878Z",
            "FinishedAt": "2022-04-26T09:57:27.7016081Z"
        },
        "Image": "sha256:0ac33e5f5afa79e084075e8698a22d574816eea8d7b7d480586835657c3e1c8b",
        "ResolvConfPath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/hostname",
        "HostsPath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/hosts",
        "LogPath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb-json.log",
        "Name": "/web01",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                43,
                130
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c-init/diff:/var/lib/docker/overlay2/d4e3b3468f8d5658ccc1dbfa3f553cef8ec3a1800f357d90133b8974f0a4bf1c/diff",
                "MergedDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c/merged",
                "UpperDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c/diff",
                "WorkDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "96c305c6dfbd",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh"
            ],
            "Image": "alpine",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "e326007d25881fc09de1517b3eb99ea6171d55f52a5c13e12bb5c161c16441af",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/e326007d2588",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "e175506f88eb86f2743e43fcfb38c7193dcf73d5189225851a2b2ba1ae643920",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "5fc9dc982faa511aca60bbfa73f7766eb549a8f713e74ae4a29cec55b71096d5",
                    "EndpointID": "e175506f88eb86f2743e43fcfb38c7193dcf73d5189225851a2b2ba1ae643920",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]

D:\>curl 172.17.0.2
^C
D:\>curl 172.17.0.3
curl: (28) Failed to connect to 172.17.0.3 port 80 after 21002 ms: Timed out

D:\>docker attach -ti web01
unknown shorthand flag: 't' in -ti
See 'docker attach --help'.

D:\>docker attach --help

Usage:  docker attach [OPTIONS] CONTAINER

Attach local standard input, output, and error streams to a running container

Options:
      --detach-keys string   Override the key sequence for detaching a
                             container
      --no-stdin             Do not attach STDIN
      --sig-proxy            Proxy all received signals to the process
                             (default true)

D:\>docker atach web01
docker: 'atach' is not a docker command.
See 'docker --help'

D:\>docker attach web01
/ # ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ # cd var
/var # ls
cache  empty  lib    local  lock   log    mail   opt    run    spool  tmp    www
/var # cd www
/var/www # ls
index.html  localhost
/var/www # cat index.html
Hello world!/var/www #
/var/www # cl /
/bin/sh: cl: not found
/var/www # cd /
/ # ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ # cd etc
/etc # ls
alpine-release  group           inittab         modules-load.d  opt             profile         services        ssl1.1
apk             group-          issue           motd            os-release      profile.d       shadow          sysctl.conf
conf.d          hostname        logrotate.d     mtab            passwd          protocols       shadow-         sysctl.d
crontabs        hosts           modprobe.d      network         passwd-         resolv.conf     shells          udhcpd.conf
fstab           init.d          modules         nginx           periodic        securetty       ssl
/etc # cd nginx
/etc/nginx # ls
fastcgi.conf    fastcgi_params  http.d          mime.types      modules         nginx.conf      scgi_params     uwsgi_params
/etc/nginx # cd http.d
/etc/nginx/http.d # ls
default.conf
/etc/nginx/http.d # cd /
/ # nginx --help
nginx: invalid option: "-"
/ # nginx -?
nginx version: nginx/1.20.2
Usage: nginx [-?hvVtTq] [-s signal] [-p prefix]
             [-e filename] [-c filename] [-g directives]

Options:
  -?,-h         : this help
  -v            : show version and exit
  -V            : show version and configure options then exit
  -t            : test configuration and exit
  -T            : test configuration, dump it and exit
  -q            : suppress non-error messages during configuration testing
  -s signal     : send signal to a master process: stop, quit, reopen, reload
  -p prefix     : set prefix path (default: /var/lib/nginx/)
  -e filename   : set error log file (default: logs/error.log)
  -c filename   : set configuration file (default: /etc/nginx/nginx.conf)
  -g directives : set global directives out of configuration file

/ # nginx -g 'pid /tmp/nginx.pid;  daemon off; &'
nginx: [emerg] unexpected end of parameter, expecting ";" in command line
/ # nginx -g 'pid /tmp/nginx.pid;  daemon off;'
test
exit
^C/ # nginx -s start
nginx: invalid option: "-s start"
/ # nginx
/ # nginx -v
nginx version: nginx/1.20.2
/ # nginx -V
nginx version: nginx/1.20.2
built with OpenSSL 1.1.1l  24 Aug 2021 (running with OpenSSL 1.1.1n  15 Mar 2022)
TLS SNI support enabled
configure arguments: --prefix=/var/lib/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib/nginx/modules --conf-path=/etc/nginx/nginx.conf --pid-path=/run/nginx/nginx.pid --lock-path=/run/nginx/nginx.lock --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --with-perl_modules_path=/usr/lib/perl5/vendor_perl --user=nginx --group=nginx --with-threads --with-file-aio --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_addition_module --with-http_xslt_module=dynamic --with-http_image_filter_module=dynamic --with-http_geoip_module=dynamic --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_auth_request_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_slice_module --with-http_stub_status_module --with-http_perl_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-stream=dynamic --with-stream_ssl_module --with-stream_realip_module --with-stream_geoip_module=dynamic --with-stream_ssl_preread_module --add-dynamic-module=/home/buildozer/aports/main/nginx/src/njs-0.7.0/nginx --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx_devel_kit-0.3.1/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/traffic-accounting-nginx-module-2.0/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/array-var-nginx-module-0.05/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx_brotli-1.0.0rc/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx_cache_purge-2.5.1/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx_cookie_flag_module-1.1.0/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-dav-ext-module-3.0.0/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/echo-nginx-module-0.62/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/encrypted-session-nginx-module-0.08/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx-fancyindex-0.5.1/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx_http_geoip2_module-3.3/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/headers-more-nginx-module-0.33/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-log-zmq-1.0.0/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/lua-nginx-module-0.10.20/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/lua-upstream-nginx-module-0.07/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/naxsi-1.3/naxsi_src --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nchan-1.2.8/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/redis2-nginx-module-0.15/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/set-misc-nginx-module-0.32/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-http-shibboleth-2.0.1/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx_http_untar_module-1.0/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-upload-progress-module-0.9.2/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-upstream-fair-0.1.3/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/ngx_upstream_jdomain-1.1.5/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-vod-module-1.28/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-module-vts-0.1.18/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/mod_zip-1.2.0/ --add-dynamic-module=/home/buildozer/aports/main/nginx/src/nginx-rtmp-module-1.2.2/
/ # nginx -s stop
/ # apt update
/bin/sh: apt: not found
/ # apk update
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
v3.15.4-52-gaf7b2b3e8c [https://dl-cdn.alpinelinux.org/alpine/v3.15/main]
v3.15.4-63-g929a19c729 [https://dl-cdn.alpinelinux.org/alpine/v3.15/community]
OK: 15854 distinct packages available
/ # apk upgrade
OK: 7 MiB in 16 packages
/ # nginx -v
nginx version: nginx/1.20.2
/ # nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
/ # ls -la
total 80
drwxr-xr-x    1 root     root          4096 Apr 26 12:19 .
drwxr-xr-x    1 root     root          4096 Apr 26 12:19 ..
-rwxr-xr-x    1 root     root             0 Apr 26 09:57 .dockerenv
drwxr-xr-x    2 root     root          4096 Apr  4 16:06 bin
drwxr-xr-x    5 root     root           360 Apr 26 09:59 dev
drwxr-xr-x    1 root     root          4096 Apr 26 09:59 etc
drwxr-xr-x    2 root     root          4096 Apr  4 16:06 home
drwxr-xr-x    1 root     root          4096 Apr  4 16:06 lib
drwxr-xr-x    5 root     root          4096 Apr  4 16:06 media
drwxr-xr-x    2 root     root          4096 Apr  4 16:06 mnt
drwxr-xr-x    2 root     root          4096 Apr  4 16:06 opt
dr-xr-xr-x  228 root     root             0 Apr 26 09:59 proc
drwx------    1 root     root          4096 Apr 26 09:57 root
drwxr-xr-x    1 root     root          4096 Apr 26 09:59 run
drwxr-xr-x    2 root     root          4096 Apr  4 16:06 sbin
drwxr-xr-x    2 root     root          4096 Apr  4 16:06 srv
dr-xr-xr-x   11 root     root             0 Apr 26 09:59 sys
drwxrwxrwt    1 root     root          4096 Apr 26 12:58 tmp
drwxr-xr-x    1 root     root          4096 Apr  4 16:06 usr
drwxr-xr-x    1 root     root          4096 Apr 26 09:59 var
/ # cd  etc
/etc # cd nginx
/etc/nginx # ls -la
total 48
drwxr-xr-x    4 root     root          4096 Apr 26 09:59 .
drwxr-xr-x    1 root     root          4096 Apr 26 09:59 ..
-rw-r--r--    1 root     root          1077 Nov 17 13:04 fastcgi.conf
-rw-r--r--    1 root     root          1007 Nov 17 13:04 fastcgi_params
drwxr-xr-x    2 root     root          4096 Apr 26 12:11 http.d
-rw-r--r--    1 root     root          5231 Nov 17 13:04 mime.types
drwxr-xr-x    2 root     root          4096 Apr 26 09:59 modules
-rw-r--r--    1 root     root          3357 Nov 17 13:04 nginx.conf
-rw-r--r--    1 root     root           636 Nov 17 13:04 scgi_params
-rw-r--r--    1 root     root           664 Nov 17 13:04 uwsgi_params
/etc/nginx # nano
/bin/sh: nano: not found
/etc/nginx # vi
/etc/nginx # apt add nano
/bin/sh: apt: not found
/etc/nginx # apk add nano
(1/3) Installing ncurses-terminfo-base (6.3_p20211120-r0)
(2/3) Installing ncurses-libs (6.3_p20211120-r0)
(3/3) Installing nano (5.9-r0)
Executing busybox-1.34.1-r5.trigger
OK: 8 MiB in 19 packages
/etc/nginx # ls -la
total 48
drwxr-xr-x    4 root     root          4096 Apr 26 09:59 .
drwxr-xr-x    1 root     root          4096 Apr 26 21:18 ..
-rw-r--r--    1 root     root          1077 Nov 17 13:04 fastcgi.conf
-rw-r--r--    1 root     root          1007 Nov 17 13:04 fastcgi_params
drwxr-xr-x    2 root     root          4096 Apr 26 12:11 http.d
-rw-r--r--    1 root     root          5231 Nov 17 13:04 mime.types
drwxr-xr-x    2 root     root          4096 Apr 26 09:59 modules
-rw-r--r--    1 root     root          3357 Nov 17 13:04 nginx.conf
-rw-r--r--    1 root     root           636 Nov 17 13:04 scgi_params
-rw-r--r--    1 root     root           664 Nov 17 13:04 uwsgi_params
/etc/nginx # nano nginx.conf
/etc/nginx # exit

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED      STATUS        PORTS     NAMES
2704a5a5fc44   ubuntu    "bash"    6 days ago   Up 46 hours             ubuntu01

D:\>docker start web01
web01

D:\>docker container ls
CONTAINER ID   IMAGE     COMMAND     CREATED        STATUS         PORTS     NAMES
96c305c6dfbd   alpine    "/bin/sh"   11 hours ago   Up 2 seconds             web01
2704a5a5fc44   ubuntu    "bash"      6 days ago     Up 46 hours              ubuntu01

D:\>docker exec -dt web01 nginx -g 'pid /tmp/nginx.pid; daemon off; &'
''' is not recognized as an internal or external command,
operable program or batch file.

D:\>docker exec -dt web01 nginx -g "pid /tmp/nginx.pid; daemon off; &"

D:\>curl 172.17.0.3
curl: (28) Failed to connect to 172.17.0.3 port 80 after 21003 ms: Timed out

D:\>docker inspect web01
[
    {
        "Id": "96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb",
        "Created": "2022-04-26T09:57:14.6992727Z",
        "Path": "/bin/sh",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 2576,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-04-26T21:24:52.3400071Z",
            "FinishedAt": "2022-04-26T21:24:26.9580634Z"
        },
        "Image": "sha256:0ac33e5f5afa79e084075e8698a22d574816eea8d7b7d480586835657c3e1c8b",
        "ResolvConfPath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/hostname",
        "HostsPath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/hosts",
        "LogPath": "/var/lib/docker/containers/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb/96c305c6dfbd969728a42a7d2a531364f53a25783ac25ff1323f9dd00fefebeb-json.log",
        "Name": "/web01",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                43,
                130
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c-init/diff:/var/lib/docker/overlay2/d4e3b3468f8d5658ccc1dbfa3f553cef8ec3a1800f357d90133b8974f0a4bf1c/diff",
                "MergedDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c/merged",
                "UpperDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c/diff",
                "WorkDir": "/var/lib/docker/overlay2/0acdc83c3af24b1bfb6551632a36f6cd74be572db7976b3a565c5902079f5f7c/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "96c305c6dfbd",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh"
            ],
            "Image": "alpine",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "a84d308d3e689c30fddbc8c734cf76d9f2a28e8156ea844cbfc89c5f54c75dcd",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/a84d308d3e68",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "aea9643c4f651a36423b911748b13413ca87e19fb8a7dfa318c3a5c9f1f944d2",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "5fc9dc982faa511aca60bbfa73f7766eb549a8f713e74ae4a29cec55b71096d5",
                    "EndpointID": "aea9643c4f651a36423b911748b13413ca87e19fb8a7dfa318c3a5c9f1f944d2",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]

D:\>curl 172.17.0.3
curl: (28) Failed to connect to 172.17.0.3 port 80 after 21000 ms: Timed out

D:\>ping 172.17.0.2

Pinging 172.17.0.2 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 172.17.0.2:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),

D:\>docker commit web01 web-base
sha256:65c3e71f7a75b8d977b34c1748df953a9e01311381a28ee2f0409b408d206d8c

D:\>docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
Digest: sha256:4edbd2beb5f78b1014028f4fbb99f3237d9561100b6881aabbf5acce2c4f9454
Status: Image is up to date for alpine:latest
docker.io/library/alpine:latest

D:\>docker image ls
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
web-base       latest    65c3e71f7a75   26 minutes ago   10.2MB
hello-docker   latest    4c589f56b454   7 days ago       168MB
ubuntu         latest    825d55fb6340   3 weeks ago      72.8MB
alpine         latest    0ac33e5f5afa   3 weeks ago      5.57MB
hello-world    latest    feb5d9fea6a5   7 months ago     13.3kB

D:\>docker image rm web-base
Untagged: web-base:latest
Deleted: sha256:65c3e71f7a75b8d977b34c1748df953a9e01311381a28ee2f0409b408d206d8c
Deleted: sha256:4c551c6ebc19b371126c17b83e87490ce02e865bf905236929a97ada46f40eff

D:\>docker image ls
REPOSITORY     TAG       IMAGE ID       CREATED        SIZE
hello-docker   latest    4c589f56b454   7 days ago     168MB
ubuntu         latest    825d55fb6340   3 weeks ago    72.8MB
alpine         latest    0ac33e5f5afa   3 weeks ago    5.57MB
hello-world    latest    feb5d9fea6a5   7 months ago   13.3kB

D:\>docker image inspect hello-world
[
    {
        "Id": "sha256:feb5d9fea6a5e9606aa995e879d862b825965ba48de054caab5ef356dc6b3412",
        "RepoTags": [
            "hello-world:latest"
        ],
        "RepoDigests": [
            "hello-world@sha256:10d7d58d5ebd2a652f4d93fdd86da8f265f5318c6a73cc5b6a9798ff6d2b2e67"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2021-09-23T23:47:57.442225064Z",
        "Container": "8746661ca3c2f215da94e6d3f7dfdcafaff5ec0b21c9aff6af3dc379a82fbc72",
        "ContainerConfig": {
            "Hostname": "8746661ca3c2",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/hello\"]"
            ],
            "Image": "sha256:b9935d4e8431fb1a7f0989304ec86b3329a99a25f5efdc7f09f3f8c41434ca6d",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "DockerVersion": "20.10.7",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/hello"
            ],
            "Image": "sha256:b9935d4e8431fb1a7f0989304ec86b3329a99a25f5efdc7f09f3f8c41434ca6d",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 13256,
        "VirtualSize": 13256,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/5a8d9399590f0d1e89d6164aaea069b90dafa01762f2473a7c90f8f41ef984cc/merged",
                "UpperDir": "/var/lib/docker/overlay2/5a8d9399590f0d1e89d6164aaea069b90dafa01762f2473a7c90f8f41ef984cc/diff",
                "WorkDir": "/var/lib/docker/overlay2/5a8d9399590f0d1e89d6164aaea069b90dafa01762f2473a7c90f8f41ef984cc/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e07ee1baac5fae6a26f30cabfe54a36d3402f96afda318fe0a96cec4ca393359"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]

D:\>cd app

D:\app>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

D:\app>dir
 Volume in drive D is New Volume
 Volume Serial Number is 561E-6D68

 Directory of D:\app

2022-04-27  00:10    <DIR>          .
2022-04-27  00:10    <DIR>          ..
2020-06-12  15:34             1 134 index.js
2020-06-12  15:34            11 528 nodesource_setup.sh
2022-04-27  00:10    <DIR>          node_modules
2020-06-12  15:34            14 156 package-lock.json
2020-06-12  15:34               455 package.json
2022-04-27  00:10    <DIR>          public
2022-04-27  00:10    <DIR>          views
               4 File(s)         27 273 bytes
               5 Dir(s)  72 370 503 680 bytes free

D:\app>notepad Dockerfile

D:\app>docker build . -t appimage
[+] Building 0.0s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 2B                                                                                           0.0s
 => CANCELED [internal] load .dockerignore                                                                                   0.0s
 => => transferring context:                                                                                                 0.0s
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount051619569/Dockerfile: no such file or directory

D:\app>docker build d:\app\Dockerfile -t appimage
unable to prepare context: path "d:\\app\\Dockerfile" not found

D:\app>docker build d:\app -t appimage
[+] Building 0.1s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 2B                                                                                           0.0s
 => [internal] load .dockerignore                                                                                            0.0s
 => => transferring context: 2B                                                                                              0.0s
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount911977875/Dockerfile: no such file or directory

D:\app>docker build d:\app -t appimage
[+] Building 0.0s (1/2)
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 2B                                                                                           0.0s
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount573483205/Dockerfile: no such file or directory

D:\app>
```
