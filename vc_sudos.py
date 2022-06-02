#  Unitrix - UserBot
# Copyright (C) 2021-2022 UnitrixTeam
#
# This file is a part of < https://github.com/unitrixteam/>
# PLease read the GNU Affero General Public License in
# https://github.com/unitrixteam/unitrixuserbot/blob/main/LICENSE<>.


from .. import udB


def get_vcsudos():
    return udB.get_key("VC_SUDOS") or []


def is_vcsudo(id):
    return id in get_vcsudos()


def add_vcsudo(id):
    sudos = get_vcsudos()
    sudos.append(id)
    return udB.set_key("VC_SUDOS", sudos)


def del_vcsudo(id):
    if is_vcsudo(id):
        sudos = get_vcsudos()
        sudos.remove(id)
        return udB.set_key("VC_SUDOS", sudos)
