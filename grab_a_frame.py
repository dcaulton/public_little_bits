#! /usr/bin/python
# grabs a single frame from a source file.
# it's assumed that the source file 
import datetime
import re
import sys

def parse_image_lines(input_filename='index.html',
                      output_filename='whatever.jpg'):
    boundary_re = re.compile('--BoundaryString')
    ifh = open(input_filename, 'r')
    ofh = open(output_filename, 'wb')
    line = ifh.readline()
    if boundary_re.match(line):
        print 'found starting boundary'
        line = ifh.readline() #Content-type: image/jpeg\r\n
        line = ifh.readline() # Content-Length:        1985\r\n
        line = ifh.readline() #   (empty line)

        while True:
            line = ifh.readline() 
            if boundary_re.match(line):
                print 'found ending boundary'
                ofh.close()
                return
            else:
                ofh.write(line)
    else:
        print 'could not find a boundary line'

def get_file_names():
    if len(sys.argv) > 1:
        input_filename = sys.argv[0]
    else:
        input_filename = 'index.html'

    if len(sys.argv) > 2:
        output_filename = sys.argv[1]
    else:
        output_filename = "{0}{1}".format(
            datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S'), '.jpg')
    return (input_filename, output_filename)

(input_filename, output_filename) = get_file_names()
parse_image_lines(input_filename, output_filename)
