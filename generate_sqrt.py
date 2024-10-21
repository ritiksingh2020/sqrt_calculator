import math
from threading import local

class GenearteSquareRoot:

    def __init__(self, data, mapping, vendor) -> None:
        self.data = data
        self.mapping = mapping
        self.vendor = vendor
        self.thread_local = local()

    def calculate_squareroot(self):
        key = self.mapping[self.vendor]["key"]
        self.thread_local.error_counter = 0
        self.thread_local.success_counter = 0
        ans = []
        
        for data in self.data:
            try:
                ans.append(math.sqrt(float(data[key])))
                self.thread_local.success_counter += 1
            except Exception as e:
                self.thread_local.error_counter += 1
                print(f"failure because of error {e} and failure counter {self.thread_local.error_counter} and data is {data[key]}")
                if self.thread_local.error_counter > 10:
                    print(f"Error count: {self.thread_local.error_counter}")
                    print(f"Success count: {self.thread_local.success_counter}")
                    print(f"Remaining count: {len(self.data) - (self.thread_local.error_counter + self.thread_local.success_counter)}")
                    print(f"Reason for failure: {str(e)}")
                    raise Exception("Too many errors")
                
        return ans

