#!/usr/bin/env python

import graphviz as gv
import pltools.graph as plg

from introduction import users, friendships


def main():
    friends = gv.Graph(name="friends")
    friends.attr(layout="neato")
    friends.attr(rankdir="LR")
    friends.attr(rank="same")

    plg.nodes(friends, map(lambda u: u["name"], users))

    fs = set()
    for i in friendships:
        fs.add(frozenset(map(lambda e: users[e]["name"], i)))

    for i in fs:
        ii = tuple(i)
        friends.edge(ii[0], ii[1])

    plg.xdot(friends)


if __name__ == '__main__':
    main()
