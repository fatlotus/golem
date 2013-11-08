#### Headhunter.d: Distributed Job Scheduling in 100 Lines

[![Build Status](https://travis-ci.org/fatlotus/headhunter.d.png?branch=master)](https://travis-ci.org/fatlotus/headhunter.d)

This project implements both ends of a lightweight job scheduling library for
Python (enqueueing and processing of requests).

To install on a current Ubuntu AMI:

```
$ sudo apt-get install python python-setuptools git && sudo easy_install pip
   ...
$ sudo pip install headhunter
$ sudo tee /etc/headhunter.yaml
amqp_server: $SERVER_IP
queue_name: $QUEUE_NAME
^D
$
```

##### License

Copyright (c) 2013 Jeremy Archer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.