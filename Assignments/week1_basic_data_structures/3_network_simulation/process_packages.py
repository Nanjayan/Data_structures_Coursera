# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # Implementation
        while len(self.finish_time)>0:
            if self.finish_time[0] <= request[0]:
                self.finish_time.remove(self.finish_time[0])
            else:
                break
            
        if self.size > len(self.finish_time):
            val = request[0] + request[1]
            if len(self.finish_time)==0:
                self.finish_time.append(val)
                return Response(False,request[0])
            else:
                last=self.finish_time[-1]
                if request[0]<last:
                    self.finish_time.append(last+request[1])
                    return Response(False,last)
                else:
                    self.finish_time.append(val)
                    return Response(False,request[0])
        else:
            return Response(True,request[0])
        

        

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
