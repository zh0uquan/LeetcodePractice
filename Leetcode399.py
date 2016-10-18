import collections
import itertools


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # chrs = set(reduce(lambda x, y: x+y, equations))
        #
        # mappings = zip(equations, values)
        # mappings += [
        #                ([eq1[0], eq2[1]], val1 * val2)
        #                for eq1, val1 in mappings
        #                for eq2, val2 in mappings
        #                if eq1[1] == eq2[0]
        #             ]
        # mappings += [(eq[::-1], 1.0 / val) for eq, val in mappings]
        #
        # res = []
        # for q in queries:
        #     try:
        #         index = zip(*mappings)[0].index(q)
        #         res.append(zip(*mappings)[1][index])
        #     except ValueError:
        #         if all(ch in chrs for ch in q):
        #             res.append(1)
        #         else:
        #             res.append(-1)
        # return res

        # graph = collections.defaultdict(dict)
        # for eq, val in zip(equations, values):
        #     graph[eq[0]].update({eq[1]: val})
        #     graph[eq[1]].update({eq[0]: 1.0 / val})
        #
        # for node in list(graph):
        #     neighbours = list(graph[node])
        #     while neighbours:
        #         neighbour = neighbours.pop()
        #         for adj in list(graph[neighbour]):
        #             if adj not in graph[node]:
        #                 graph[node].update({adj: graph[node][neighbour] * graph[neighbour][adj]})
        #                 neighbours.append(adj)
        #
        # return [graph[q[0]][q[1]] if graph[q[0]].has_key(q[1]) else float(-1) for q in queries]

        graph = collections.defaultdict(dict)
        for (node, neighbour), val in zip(equations, values):
            graph[node][node] = graph[neighbour][neighbour] = 1.0
            graph[node][neighbour] = val
            graph[neighbour][node] = 1.0 / val

        for k, i, j in itertools.permutations(graph, 3):
            if k in graph[i] and j in graph[k]:
                graph[i][j] = graph[i][k] * graph[k][j]
        return [graph[node].get(neighbour, -1) for node, neighbour in queries]





if __name__ == '__main__':
    # equations = [["a", "b"], ["b", "c"]]
    # values = [2.0, 3.0]
    # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    print(Solution().calcEquation(equations, values, queries))
