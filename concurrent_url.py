from concurrent.futures import ProcessPoolExecutor as PoolExecutor
import http.client
import socket
import multiprocessing

def get_it(url):
    try:
        # always set a timeout when you connect to an external server
        connection = http.client.HTTPConnection(url, timeout=2)

        connection.request("GET", "/")

        response = connection.getresponse()
        #print(response)
        #print(url)
        return response.read()
    except socket.timeout:
        # in a real world scenario you would probably do stuff if the
        # socket goes into timeout
        pass

urls = [
    "www.google.com",
    "www.youtube.com",
    "www.wikipedia.org",
    "www.reddit.com",
    "www.httpbin.org"
]*1000

max_workers = multiprocessing.cpu_count()

with PoolExecutor(max_workers) as executor:
    future =  executor.submit(get_it, urls)
    #print(Future.result())
