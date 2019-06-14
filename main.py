import os

from dotenv import load_dotenv

from github import Github, Gist
from github import GithubObject, InputFileContent

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

g = Github(GITHUB_TOKEN)
u = g.get_user()

# Create a gist
gist = u.create_gist(
    public=False,
    files={
        "Test Name": InputFileContent(content="Test Content")
    },
    description=GithubObject.NotSet)

# Publish an edit
gist.edit(
    files={
        "Test Name": InputFileContent("Test Content 2")
    }
)
