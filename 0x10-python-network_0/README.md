# 0x10. Python - Network #0

## curl

cURL command line tool to transfer data over a network

Here are some options, uses, and examples of cURL:

- -X or --request: Specifies the HTTP request method to use. For example, to send a GET request:

        ```
        curl -X GET https://example.com
        ```

- -d or --data: Sends a request body in the HTTP request. For example, to send a POST request with data:

        ```
        curl -X POST -d 'name=value' https://example.com/form
        ```

- -H or --header: Sends an HTTP header in the request. For example, to send a custom User-Agent:

        ```
        curl -H 'User-Agent: MyApp' https://example.com
        ```

- -u or --user: Specifies a user name and password for HTTP authentication. For example, to access a protected resource:

        ```
        curl -u user:password https://example.com/secret
        ```

- -I or --head: Sends a HEAD request (i.e. only retrieves the HTTP headers). For example, to check the status of a resource:

        ```
        curl -I https://example.com/image.jpg
        ```

- -L or --location: Follows redirects. For example, to follow a redirect:

        ```
        curl -L https://example.com/redirect
        ```

- -o or --output: Saves the response body to a file. For example, to save the response to a file:

        ```
        curl -o response.txt https://example.com
        ```

- -s or --silent: Suppresses output. For example, to run a cURL command silently:

        ```
        curl -s https://example.com
        ```

- -w or --write-out: Prints a summary of the request and response. For example, to see the response time and size:

        ```
        curl -w 'Response time: %{time_total}s, Response size: %{size_download} bytes' https://example.com
        ```
