import requests
import click

@click.command()
def main():
    print("Hello from Jenkins Python project!")
    response = requests.get("https://api.github.com")
    print(f"GitHub API status: {response.status_code}")

if __name__ == "__main__":
    main()

