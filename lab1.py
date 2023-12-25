def a_star_search(start, stop):
    open_set, closed_set, g, parents = {start}, set(), {start: 0}, {start: start}

    def heuristic(node):
        h_dist = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}
        return h_dist[node]

    def get_neighbours(node):
        return Graph_nodes.get(node, [])

    while open_set:
        n = min(open_set, key=lambda v: g[v] + heuristic(v))
        if n == stop or not Graph_nodes.get(n):
            pass
        else:
            for m, weight in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m], g[m] = n, g[n] + weight
                elif g[m] > g[n] + weight:
                    g[m], parents[m] = g[n] + weight, n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
        if not n:
            print('Path does not exist!')
            return None
        if n == stop:
            path = [n]
            while parents[n] != n:
                path.append(parents[n])
                n = parents[n]
            path.reverse()
            print('Path found:', path)
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

Graph_nodes = {'A': [('B', 6), ('F', 3)], 'B': [('C', 3), ('D', 2)], 'C': [('D', 1), ('E', 5)],
               'D': [('C', 1), ('E', 8)], 'E': [('I', 5), ('J', 5)], 'F': [('G', 1), ('H', 7)],
               'G': [('I', 3)], 'H': [('I', 2)], 'I': [('E', 5), ('J', 3)]}

a_star_search('A', 'J')
