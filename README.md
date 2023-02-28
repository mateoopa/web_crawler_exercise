# Web crawler Dataloop exercise
web crawler exercise for datloop

## Prerequisites
- [Python](https://www.python.org/) (with [pip](https://pypi.org/project/pip/)) installed on your development machine. If you do not have Python, visit the previous link for download options.

## Configure the web crawler

1. In your command-line interface (CLI), navigate to this directory and run the following command to install requirements.

    ```Shell
    pip install -r requirements.txt
    ```
    
## Run the web crawler

1. Run the following command in your CLI to start the web crawler.

    ```Shell
    python crawler.py <start_url: string> <depth: number>
    ```
    
    For example:
    
    ```Shell
    python crawler.py https://github.com/ 3
    ```
