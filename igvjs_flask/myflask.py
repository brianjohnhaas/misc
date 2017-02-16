#!/usr/bin/env python


from flask import Flask, request, Response, session, g, redirect, url_for, abort, \
          render_template, flash, send_from_directory
import os, sys, re
import mimetypes

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/js/<path:path>')
def get_js(path):
    print sys.stderr.write("get_js: {}\n".format(path))
    return send_from_directory("js", path)


@app.route('/CSS/<path:path>')
def get_css(path):
    print sys.stderr.write("get_css: {}\n".format(path))
    return send_from_directory("css", path)


@app.route('/data/<path:path>')
def send_file_partial(path):
    """
      ############################################
      ## ** this entire routine was taken from:
      ## https://gist.github.com/lizhiwei/7885684
      ############################################

        Simple wrapper around send_file which handles HTTP 206 Partial Content
        (byte ranges)
        TODO: handle all send_file args, mirror send_file's error handling
        (if it has any)
     """

    sys.stderr.write("send_file_partial({})\n".format(path))
                                        
    range_header = request.headers.get('Range', None)
    if not range_header:
        return send_from_directory('data', path)

    sys.stderr.write("Range request on {}: {}\n".format(path, range_header))
    
    size = os.path.getsize("data/{}".format(path))
    byte1, byte2 = 0, None

    m = re.search('(\d+)-(\d*)', range_header)
    g = m.groups()
    
    if g[0]: byte1 = int(g[0])
    if g[1]: byte2 = int(g[1])
    
    length = size - byte1
    if byte2 is not None:
        length2 = byte2 - byte1
        if length2 < length:
            length = length2
    
    data = None
    with open("data/{}".format(path), 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    sys.stderr.write("byte request [{}]: {} - {}, size: {}\n".format( path, byte1, byte2, size))
    
    rv = Response(data,
                  206,
                  mimetype=mimetypes.guess_type("data/{}".format(path))[0],
                  direct_passthrough=True)
    rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))

    ## just in case, there's a note that states:
    ## Length calculation is wrong in this gist.    0-0 means 1 byte (at index 0).
    ## (and no correction was applied here yet)
    
    return rv


app.run(host='localhost', port=8085, debug=True)


