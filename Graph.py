screen_width = 480
screen_height = 480
gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize
import time

class Graph:
    #path = []

    def __init__(self):#, snake):
        self.graph = {}
        self.visited = set()
        #self.snake = snake

    def grid_to_graph(self):
        dx = [-gridsize, gridsize, 0, 0]
        dy = [0, 0, gridsize, -gridsize]
        
        for x in range(0, screen_width , gridsize):
            for y in range(0, screen_height , gridsize):
                self.graph[(x,y)] = []
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if xx < 0 or yy < 0:
                        continue
                    elif xx > screen_width - gridsize or yy > screen_height - gridsize:
                        continue
                    else:
                        if xx:
                            self.graph[(x,y)].append((xx, yy))
        return self.graph
        #print(self.graph)
                        #print((x,y), (xx, yy))
    

    def dfs(self, start, end, path=[]):
        #time.sleep(0.3)
        print(start)
        if start in self.visited:
            #print('Cycle')
            return None
        path = path + [start]
        self.visited.add(start)
        if start == end:
            return path
        
        for neighbor in self.graph[start]:
            #if neighbor in self.visited:
            #    return path # detect cycle
            if neighbor not in path:
                newpath = self.dfs(neighbor, end, path)
                if newpath: return newpath
        return None


    def rec_dfs(self, source, target, path = []):
        if source not in path:
            path.append(source)
            if source not in self.graph:
                return path
            if source == target:
                print('Equal')
                return path
            for n in self.graph[source]:
                path = self.rec_dfs(n, target, path)
        return path

    def dfs_shortest_path(self, start, end, path = []):
        if start in self.visited:
            print('Cycle')
            return None
        path = path + [start]
        self.visited.add(start)
        if start == end:
            return path
        
        shortest = None
        for neighbor in self.graph[start]:
            #if neighbor in self.visited:
            #    return path # detect cycle
            if neighbor not in path:
                newpath = self.dfs(neighbor, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


    def bfs(self, start, end):
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([start])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            print(node)
            # path found
            if node == end:
                return path
            if node in path:
                return None
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return None

    def get_visited(self):
        print(self.visited)