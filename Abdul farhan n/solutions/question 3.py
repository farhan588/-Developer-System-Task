import heapq

def prim(n, graph):
     mst = []
    visited = [False] * n
    min_heap = [(0, 0)]  
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if weight > 0:
            mst.append((weight, u))
        for v, edge_weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v))
    return mst
