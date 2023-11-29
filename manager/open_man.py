#!/usr/bin/python

from pathlib import Path


class OpenFilenameManager :
    def __init__(self, datasets) :
        self.selectFilenameFrame = None
        self.imageManager = None
        self.pathManager = None
        self.editManager = None
        self.datasets = datasets

    def save(self) :
        if self.pathManager.get_file_suffix() is not None :
            self.selectFilenameFrame.save_frame()

        if self.pathManager.get_filename() is not None :
            dest_file = self.pathManager.get_dest_filename()
            Path(dest_file).parent.mkdir(parents=True, exist_ok=True)
            print('dest_file {}'.format(dest_file))
            self.datasets.save_frame(dest_file)
            row_filename = self.pathManager.get_row_filename()
            if not Path(row_filename).is_file() :
                self.imageManager.save(row_filename)
            print('datasets {}'.format(self.datasets))

    def open(self, filename) :
        print("Selected file: {}".format(filename))
        self.pathManager.set_filename(filename)
        self.editManager.set_work_frame(filename)

        source_file = self.pathManager.get_source_filename()
        self.imageManager.read(source_file)

        dest_file = self.pathManager.get_dest_filename()
        if Path(dest_file).is_file() :
            print('True  -> dest_file {}'.format(dest_file))
            self.datasets.read_frame(dest_file)
        else :
            print('False -> dest_file {}'.format(dest_file))
            x, y = self.imageManager.get_image_size()
            self.datasets.new_frame(x, y)
        print('datasets {}'.format(self.datasets))
        self.editManager.show()

    def set_SelectFilenameFrame(self, selectFilenameFrame) :
        self.selectFilenameFrame = selectFilenameFrame

    def set_ImageManager(self, imageManager) :
        self.imageManager = imageManager

    def set_PathManager(self, pathManager) :
        self.pathManager = pathManager

    def set_EditManager(self, editManager) :
        self.editManager = editManager
