import abc
import numpy as np

import core.path_some as ps
import core.data_preprocessing.data_set_read as dsr
import core.data_preprocessing.data_read as dr
import core.image_processing.image_read as imr
import core.feature_processing.image_feature as imf
import core.data_preprocessing.feature_read as fr
import core.classifier.image_classifier as imc


class MainProcessInterface(metaclass=abc.ABCMeta):
    def __init__(self, vdr: dr.DataReadInterface, vimr: imr.ImageReadInterface,
                 vimf: imf.ImageFeature, vfr: fr.FeatureReadInterface,
                 vimc: imc.ImageClassifierInterface):
        # self.data_set_read = vdsr vdsr: dsr.DataSetReadInterface,
        self.data_read = vdr
        self.image_read = vimr
        self.image_feature = vimf
        self.feature_read = vfr
        self.image_classifier = vimc
        self.data_set_num = None

    @abc.abstractmethod
    def do_flow(self):
        pass


class MainProcess(MainProcessInterface):
    def do_flow(self):
        img_it = self.data_read.get_images_iter()
        labels = self.data_read.get_labels()
        if not self.data_read.data_set.path_some.is_file_exists(self.data_set_num, '', 'label'):
            np.savetxt(self.data_read.data_set.path_some.fetch(self.data_set_num, '', 'label'), labels)
        self.image_feature.fetch_proc(img_it, self.image_read, self.data_read.data_set.data_set_num)


if __name__ == '__main__':
    mp = MainProcess(dr.DataRead(dsr.DataSetRead(ps.PathSome())), imr.ImageRead(),
                     imf.ImageFeature(True, True, False, False, False, True), fr.FeatureRead(),
                     imc.ImageClassifier())
    mp.do_flow()
