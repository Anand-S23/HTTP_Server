import os 

headers = {
    'Server': 'CrudeServer',
    'Content-Type': 'text/html',
}

status_codes = {
    200: 'OK',
    404: 'Not Found',
    501: 'Not Implemented',
}

def get_response_line(code):
    reason = status_codes[code]
    return f'HTTP/1.1 { code } { reason }\r\n'

def get_response_headers(extra_headers=None):
    headers_copy = headers.copy()

    if extra_headers:
        headers_copy.update(extra_headers)

    header = ''

    for h in headers_copy:
        header += f'{ h }: { headers_copy[h] }\r\n'

    return header

def render_html(file):
    if os.path.exists(file) and not os.path.isdir(file):
        response_line = get_response_line(200)
        response_headers = get_response_headers()

        with open(file, 'rb') as f:
            response_body = f.read().decode()
    else:
        response_line = get_response_line(404)
        response_headers = headers
        response_body = '<h1>404 Not Found</h1>'

    response = ''.join([response_line, response_headers, '\r\n', response_body])
    return response