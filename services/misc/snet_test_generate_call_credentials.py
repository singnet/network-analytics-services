# Tested on python3.6

# You need to run this on an environment where snet-cli can run

import subprocess
import yaml

def generate_call_credentials():
    agent_address = "0xb57B4c70379E84CD8d42a867cF326d5e0743E11d"  # NetworkAnalyticsServices deployed to Kovan
    result = subprocess.check_output(["snet", "agent", "--at", agent_address, "create-jobs", "--funded", "--signed", "--no-confirm", "--max-price","100000000"])
    job = yaml.load(result)["jobs"][0]
    job_address = job["job_address"]
    job_signature = job["job_signature"]
    print("job_address------------------------------")
    print(job_address)
    print("job_signature----------------------------")
    print(job_signature)


generate_call_credentials()