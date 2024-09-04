import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOS = os.getenv('GITHUB_REPOS').split(',')

def get_workflow_runs(repo):
    url = f'https://api.github.com/repos/{repo}/actions/runs'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

@app.route('/metrics', methods=['GET'])
def metrics():
    all_workflow_runs = []
    for repo in GITHUB_REPOS:
        try:
            workflow_runs = get_workflow_runs(repo)
            all_workflow_runs.extend(workflow_runs['workflow_runs'])
        except requests.RequestException as e:
            print(f"Failed to fetch workflow runs for {repo}: {e}")
    return jsonify(all_workflow_runs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
