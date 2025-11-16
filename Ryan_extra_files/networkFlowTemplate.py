import sys

"""
Courtesy of Steven Halim, Felix Halim, Suhendry Effendy
CP4 Free Source Code Project (cpp/gnu++17, java/java11, py/python3, and ml/ocaml).
https://github.com/stevenhalim/cpbook-code/blob/master/ch8/maxflow.py
"""
from numbers import Number  # For type hints that accept int or float
from copy import deepcopy  # Used by .copy() to clone the structure
from collections import deque, defaultdict
import heapq

INF = float("inf")  # A convenient infinity value for flows/limits


class MaxFlow:
    def __init__(self, V: int):
        """
        Creates a new instance of the MaxFlow class. The general way you'll
        want to use this library is to create a new instance of the class,
        add edges, then call the `edmonds_karp` or `dinic` methods.
        While the library does support floats, be aware that it is not advised
        to use due to the potential for floating point errors, meaning small
        amounts of flow may be sent many times.

        Arguments:
            V: The number of vertices in the graph.

        Example:
            >>> mf = MaxFlow(3)
            >>> mf.add_edge(0, 1, 3)
            >>> mf.add_edge(0, 2, 3)
            >>> mf.add_edge(1, 2, 3)
            >>> mf.dinic(0, 2)  # or mf.edmonds_karp(0, 2)
            6
        """
        self.V = V  # store number of vertices
        self.EL = []  # Edge List: list of [to, capacity, flow]
        self.AL = [list() for _ in range(self.V)]  # Adjacency list of edge indices
        self.level = []  # BFS distance/level array
        self.last = []  # current-arc array for Dinic
        self.parents = []  # parent reconstruction for EK path: [parent, edge_index]
        self.has_been_run = (
            False  # guard to prevent re-running max-flow on a mutated graph
        )

    def BFS(self, s: int, t: int) -> bool:
        self.level = [-1] * self.V  # initialize all levels to -1 (unvisited)
        self.level[s] = 0  # source level is 0
        self.parents = [[-1, -1] for _ in range(self.V)]  # clear parent info
        q = deque([s])
        # q = [s]  # basic list as queue (pop(0) below); a deque would be faster
        while len(q) != 0:  # standard BFS loop
            u = q.popleft()
            # u = q[0]  # take front
            # q.pop(0)  # pop front (O(n), but fine for small instances)
            if u == t:  # early exit if sink reached
                break
            for idx in self.AL[u]:  # iterate all outgoing edges of u
                v, cap, flow = self.EL[idx]  # unpack edge triple
                if (
                    cap - flow > 0 and self.level[v] == -1
                ):  # residual capacity exists and v unvisited
                    self.level[v] = self.level[u] + 1  # set BFS level
                    q.append(v)  # enqueue v
                    self.parents[v] = [
                        u,
                        idx,
                    ]  # remember parent and which edge led to v
        return self.level[t] != -1  # return True if sink is reachable in residual graph

    def send_one_flow(self, s: int, t: int, f: Number = INF) -> Number:
        """
        Finds the minimum flow (bottleneck) along a path
        """
        if s == t:  # base case: reached source; return bottleneck accumulated
            return f
        u, idx = self.parents[t]  # parent u and edge index used to enter t
        _, cap, maxFlow = self.EL[idx]  # read capacity and current flow on that edge
        pushed = self.send_one_flow(
            s, u, min(f, cap - maxFlow)
        )  # recurse up; keep min with residual
        maxFlow += pushed  # add pushed amount to forward edge flow
        self.EL[idx][2] = maxFlow  # write back updated flow
        self.EL[idx ^ 1][
            2
        ] -= pushed  # subtract on reverse edge (increase reverse residual cap)
        return pushed  # return how much we actually pushed

    def DFS(self, u: int, t: int, f: Number = INF) -> Number:
        if u == t or f == 0:  # reached sink or no more flow possible
            return f
        for i in range(self.last[u], len(self.AL[u])):  # current-arc iteration
            self.last[u] = i  # remember where we are so we don’t retry earlier edges
            v, cap, flow = self.EL[self.AL[u][i]]  # access i-th outgoing edge of u
            if (
                self.level[v] != self.level[u] + 1
            ):  # enforce level graph property (Dinic)
                continue
            pushed = self.DFS(v, t, min(f, cap - flow))  # try to push further
            if pushed != 0:  # if we could push something through v
                flow += pushed
                self.EL[self.AL[u][i]][2] = flow  # update forward edge flow
                self.EL[self.AL[u][i] ^ 1][2] -= pushed  # update reverse edge flow
                return (
                    pushed  # return immediately (single blocking-flow path extension)
                )
        return 0  # no augmenting path from u within current level graph

    def add_edge(self, u: int, v: int, capacity: Number, directed: bool = True) -> None:
        """
        Adds an edge from `u` to `v` with capacity `w`. By default, the edge is
        directed, i.e. `u`->`v`. You can set `directed = False` to add it
        as an undirected edge `u`<->`v`.

        Arguments:
            `u`: The first vertex.
            `v`: The second vertex.
            `capacity`: The capacity of the edge.
            `directed`: Whether the edge is directed. True by default.

        Example:
            >>> mf = MaxFlow(3)
            >>> mf.add_edge(0, 1, 3)
            >>> mf.add_edge(2, 1, 3)
        """
        if u == v:  # ignore self-loops (not useful in standard max-flow)
            return
        self.EL.append(
            [v, capacity, 0]
        )  # forward edge u->v with given capacity, zero flow
        self.AL[u].append(len(self.EL) - 1)  # store its index in u's adjacency list
        self.EL.append([u, 0 if directed else capacity, 0])  # reverse edge v->u
        self.AL[v].append(
            len(self.EL) - 1
        )  # store reverse edge index in v's adjacency list

    def assert_has_not_already_been_run(self):
        if self.has_been_run:  # if a max-flow algorithm already ran on this object
            msg = (
                "Rerunning a max flow algorithm on the same graph will "
                + "result in incorrect behaviour. Please use .copy() "
                + "before you run any max flow algorithm if you need to "
                + "run multiple iterations"
            )
            raise Exception(msg)  # prevent accidental reuse of mutated residual state

        self.has_been_run = True  # mark as used going forward

    def edmonds_karp(self, s: int, t: int) -> Number:
        """
        Returns the max flow obtained by running Edmons-Karp algorithm.
        Modifies the graph in place.

        Arguments:
            `s`: The source vertex.
            `t`: The sink vertex.

        Returns:
            The max flow.
        """
        self.assert_has_not_already_been_run()  # guard

        mf = 0  # total max flow accumulator
        while self.BFS(s, t):  # as long as an augmenting path exists
            f = self.send_one_flow(
                s, t
            )  # send along the found shortest (in edges) path
            if f == 0:  # (should rarely be 0; safety)
                break
            mf += f  # accumulate flow
        return mf

    def dinic(self, s: int, t: int) -> Number:
        """
        Returns the max flow obtained by running Dinic's algorithm.
        Modifies the graph in place.

        Arguments:
            `s`: The source vertex.
            `t`: The sink vertex.

        Returns:
            The max flow.
        """
        self.assert_has_not_already_been_run()  # guard

        mf = 0  # total max flow accumulator
        while self.BFS(s, t):  # build level graph via BFS
            self.last = [0] * self.V  # reset current-arc pointers
            f = self.DFS(s, t)  # send blocking flow within this level graph
            while f != 0:  # keep sending until no more in this phase
                mf += f
                f = self.DFS(s, t)
        return mf

    def copy(self) -> "MaxFlow":
        """
        Returns a deep copy of the current instance. This is convenient for
        problems where you need to run MaxFlow multiple times on slightly
        different graphs, since the instance is destroyed after each max flow
        run.

        Example:
            >>> mf = MaxFlow(4)
            >>> mf.add_edge(0, 1, 3)
            >>> mf.add_edge(1, 2, 3)
            >>> for c in range(1, 4):
            >>>     mf_copy = mf.copy()
            >>>     mf_copy.add_edge(2, 3, c)
            >>>     res = mf_copy.dinic(0, 3)  # Will not modify mf
        """
        return deepcopy(self)  # deep clone of all lists (safe to reuse)

    def __repr__(self) -> str:
        el = self.EL[:10] + ["..."] if len(self.EL) > 10 else self.EL  # preview EL
        al = self.AL[:10] + ["..."] if len(self.AL) > 10 else self.AL  # preview AL
        el = ", ".join(map(str, el))  # stringify
        al = ", ".join(map(str, al))
        return f"MaxFlow(V={self.V}, EL=[{el}], AL=[{al}])"  # printable summary


if __name__ == "__main__":
    mf = MaxFlow(4)
    print(f"{mf}\t{mf.parents}")
    mf.add_edge(0, 1, 4)
    print(f"{mf}\t{mf.parents}")
    mf.add_edge(1, 2, 7)
    print(f"{mf}\t{mf.parents}")
    mf.add_edge(0, 3, 6)
    print(f"{mf}\t{mf.parents}")
    mf.add_edge(3, 2, 9)
    print(f"{mf}\t{mf.parents}")
    mf.edmonds_karp(0, 2)
    print(f"{mf}\t{mf.parents}")
