#!/usr/bin/python

from pathlib import Path
import yaml
from frame.add_item import *
from manager.target_man import *


class ChangeUserNameMenu(object):
    def __init__(self, path_manager: object) :
        self.__pathMan       = path_manager

        frame_title  = 'Change user name'
        search_title = 'User name'
        search_item  = ''
        check_similarly_item = True
        self.__make_object = AddItemFrame(frame_title, search_title, search_item, check_similarly_item)
        self.__make_object.set_cancel_fn(lambda : print('CANCEL'))
        self.__make_object.set_add_fn(self.__change_user_name)
        self.__make_object.set_items(self.__get_user_names())

    def __call__(self):
        self.__make_object.run()

    def __change_user_name(self, name: str):
        self.__pathMan.set_user_name(name)
        self.__save()

    def __save(self) :
        # save default rating in yaml file
        names_yaml = """user_names : {}""".format(list(self.__make_object.get_items()))
        print(names_yaml)
        names = yaml.safe_load(names_yaml)

        with open(self.__pathMan.get_user_info_file(), 'w') as file :
            yaml.dump(names, file)

    def __get_user_names(self):
        if (Path(self.__pathMan.get_user_info_file()).is_file()) :
            with open(self.__pathMan.get_user_info_file()) as file :
                config_list = yaml.load(file, Loader=yaml.FullLoader)
            retVal = config_list['user_names']
            print('user_names {}'.format(config_list))
        else :
            retVal = []
        return retVal
