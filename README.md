#### Headhunter.d: Distributed Job Scheduling in 100 Lines

This project implements both ends of a lightweight job scheduling library for Python. To use, place the code (the `golem` directory) and the `configuration.yaml` file in the same directory. What happens next is implementation-dependent, but I've provided a sample upstart configuration job for Debian-based systems.

To install on a current Ubuntu AMI:

```
$ sudo apt-get install python python-setuptools git
   ...
$ git clone https://www.github.com/fatlotus/headhunter.d.git
$ mv golem /usr/lib/python2.7/headhunter
$ cp /usr/lib/python2.7/headhunter/upstart_job /etc/init/headhunter.conf
```

Next, configure the Golem instance by editing `/usr/lib/python2.7/golem/configuration.yaml` --- you will need to change the AMQP server IP address as given in the file.

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