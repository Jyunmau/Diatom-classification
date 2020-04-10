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
    def __init__(self, vdsr: dsr.DataSetReadInterface, vdr: dr.DataReadInterface, vimr: imr.ImageReadInterface,
                 vimf: imf.ImageFeature, vfr: fr.FeatureReadInterface,
                 vimc: imc.ImageClassifierInterface):
        self.data_set_read = vdsr
        self.data_read = vdr
        self.image_read = vimr
        self.image_feature = vimf
        self.feature_read = vfr
        self.image_classifier = vimc

    @abc.abstractmethod
    def do_flow(self):
        pass


class MainProcess(MainProcessInterface):

    def do_flow(self, is_feature_fetch: bool = False, is_train_model=False, is_predict=False):
        cls = ps.PathSome()
        if is_feature_fetch:
            img_it = self.data_read.get_images_iter(self.data_set_read)
            labels = self.data_read.get_labels(self.data_set_read)
            if not cls.is_file_exists(self.data_set_read.data_set_num, '', 'label'):
                np.savetxt(cls.fetch(self.data_set_read.data_set_num, '', 'label'), labels)
            self.image_feature.fetch_proc(img_it, self.image_read, self.data_set_read)
        elif is_train_model:
            self.image_classifier.fit()
        elif is_predict:
            self.image_classifier.predict()


if __name__ == '__main__':
    mp = MainProcess(dr.DataRead(dsr.DataSetRead(ps.PathSome())), imr.ImageRead(),
                     imf.ImageFeature(True, True, False, False, False, True), fr.FeatureRead(),
                     imc.ImageClassifier())
    mp.do_flow()
