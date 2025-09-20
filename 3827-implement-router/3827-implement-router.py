import collections
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets = collections.deque()
        self.packet_set = set()
        self.destination_timestamps = collections.defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.packet_set:
            return False

        if len(self.packets) >= self.memoryLimit:
            oldest_packet = self.packets.popleft()
            oldest_source, oldest_destination, oldest_timestamp = oldest_packet
            self.packet_set.remove(tuple(oldest_packet))

            dest_list = self.destination_timestamps[oldest_destination]

            if dest_list and dest_list[0] == oldest_timestamp:
                dest_list.pop(0)

            if not dest_list:
                del self.destination_timestamps[oldest_destination]

        self.packets.append([source, destination, timestamp])
        self.packet_set.add(packet)

        bisect.insort(self.destination_timestamps[destination], timestamp)
        
        return True

    def forwardPacket(self) -> list[int]:
        if not self.packets:
            return []

        packet_to_forward = self.packets.popleft()
        source, destination, timestamp = packet_to_forward
        
        self.packet_set.remove(tuple(packet_to_forward))

        dest_list = self.destination_timestamps[destination]
        if dest_list:
            dest_list.pop(0)
        if not dest_list:
            del self.destination_timestamps[destination]
            
        return packet_to_forward

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destination_timestamps:
            return 0
        
        timestamps = self.destination_timestamps[destination]

        start_index = bisect.bisect_left(timestamps, startTime)
        end_index = bisect.bisect_right(timestamps, endTime)
        
        return end_index - start_index
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)