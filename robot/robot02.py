#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rg


class Robot:

    def act(self, game):
        ilu_wrogow = 0

        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) <= 1:
                    ilu_wrogow += 1

        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) <= 1:
                    if ilu_wrogow == 1 and self.hp > 10:
                        return['attack', poz]
                    else:
                        return['suicide']

        if self.location != rg.CENTER_POINT:
            return['move', rg.toward(self.location, rg.CENTER_POINT)]

        return['guard']
