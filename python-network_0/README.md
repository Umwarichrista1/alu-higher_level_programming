# Python - Network #0

This project covers the basics of HTTP and networking: URLs, request
and response structure, headers, status codes, cookies, and how to
make HTTP requests from the command line using cURL.

## Learning Objectives
- What a URL is, and how to read one (scheme, domain, sub-domain,
  port, path, query string)
- What HTTP is, and what an HTTP request and response look like
- What HTTP headers are, and what the message body is
- What an HTTP request method is, and what a response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser

## Requirements
- Ubuntu 20.04 LTS
- Every Bash script is exactly 3 lines long (`wc -l` prints 3)
- Every Bash script starts with `#!/bin/bash`, followed by a comment
  explaining what it does
- Every curl command uses the `-s` (silent) option
- All files end with a new line and are executable

## Files
| File | Description |
|------|-------------|
| 0-body_size.sh | Print the size (in bytes) of a response body |
| 1-body.sh | Print the response body only for a 200 status |
| 2-delete.sh | Send a DELETE request and print the body |
| 3-methods.sh | List all HTTP methods a server accepts |
| 4-header.sh | Send a GET request with a custom header |
| 5-post_params.sh | Send a POST request with email/subject params |
